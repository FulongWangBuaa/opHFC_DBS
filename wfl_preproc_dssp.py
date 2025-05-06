# %%
import numpy as np
import matplotlib.pyplot as plt
import copy
from scipy import linalg

import mne
from mne.fixes import _safe_svd
from mne.io.pick import _picks_to_idx

def on_press(event):
    if event.button == 1:
        return event.xdata, event.ydata

click_x = None
click_y = None
def onclick(event):
    global click_x, click_y
    if event.button == 1:  # 点击鼠标左键
        click_x = event.xdata
        click_y = event.ydata
        # print(f"鼠标点击位置：({click_x}, {click_y})")

def get_click_position(y,title,linestyle='-',marker='o'):
    global click_x, click_y
    fig, ax = plt.subplots()
    ax.plot(y,linestyle=linestyle,marker=marker)
    ax.set_title(title)
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    while click_x is None or click_y is None:
        plt.pause(0.1)
    fig.canvas.mpl_disconnect(cid)
    x = click_x
    click_x = None
    click_y = None
    plt.close(fig)
    return int(np.floor(x)+1)

def _orth_overwrite(A):
    """Create a slightly more efficient 'orth'."""
    # adapted from scipy/linalg/decomp_svd.py
    check_disable = dict(check_finite=False)
    u, s = _safe_svd(A, full_matrices=False, **check_disable)[:2]
    M, N = A.shape
    eps = np.finfo(float).eps
    tol = max(M, N) * np.amax(s) * eps
    num = np.sum(s > tol, dtype=int)
    return u[:, :num]

def dssp(raw, leadfield,picks=None, Nspace='interactive',
         Nout=None,Nin=None,Nee=None,st_correlation=0.98):
    if Nout is not None and Nin is not None and Nee is not None:
         flag = 1
    elif st_correlation is None:
        if Nout is None and Nin is None and Nee is None:
            raise ValueError('Need to specify st_correlation or Nout, Nin, Nee')
    else:
        if st_correlation < 0 or st_correlation > 1:
            raise ValueError('st_correlation must be between 0 and 1')
        else:
            flag = 0
    
    picks = _picks_to_idx(raw.info, picks, exclude=())
    picks_good, picks_bad = list(), list()  # these are indices into picks
    for ii, pi in enumerate(picks):
        if raw.ch_names[pi] in raw.info["bads"]:
            picks_bad.append(ii)
        else:
            picks_good.append(ii)
    picks_good = np.array(picks_good, int)
    picks_bad = np.array(picks_bad, int)

    Nc = len(picks_good)

    data_signal_all = raw.get_data()

    B = data_signal_all[picks_good,:]

    # Gram matrix of leadfield matrix
    leadfield = leadfield[picks_good,:]
    # eigen decomposition of the Gram matrix, matrix describing the spatial components
    FF_T = np.dot(leadfield,leadfield.T)
    # # S：特征值   U：特征向量
    # S,U = np.linalg.eigh(FF_T)
    U,S,Vh = _safe_svd(FF_T, full_matrices=False)

    Sspace  = abs(S)
    sorted_Sspace = np.sort(Sspace)[::-1]
    iorder = np.argsort(Sspace)[::-1]
    Sspace = sorted_Sspace
    U = U[:,iorder]

    # select vectors to use
    if Nspace is None:
        ttext = 'enter the spatial dimension: '
        Nspace = int(input(ttext))
    elif isinstance(Nspace, str) and Nspace == 'interactive':
        Nspace = get_click_position(np.log10(Sspace),title='Nsapce')
    elif isinstance(Nspace, str) and Nspace == 'all':
        eps = np.finfo(float).eps
        Nspace = len(np.where(Sspace/Sspace[0]>1e5*eps)[0])
    print('Using %d spatial dimensions' % Nspace)

    # spatial subspace projector
    Us = U[:, :Nspace]
    proj = np.dot(Us, Us.T)

    # Bin and Bout creations
    B_in = np.dot(proj, B)
    B_out = np.dot(np.eye(proj.shape[0],proj.shape[1])-proj, B)
    
    if flag == 1:
        # Fieldtrip 方法

        # interference rejection by removing
        # the common temporal subspace of the two subspaces
        U_in,Sexp2_in,Vh_in = _safe_svd(B_in, full_matrices=False)
        U_out,Sexp2_out,Vh_out = _safe_svd(B_out, full_matrices=False)
        
        # select vectors to use
        if Nin is None:
            ttext = 'enter the spatial dimension for the inside field: '
            Nout = int(input(ttext))
        elif isinstance(Nin, str) and Nin == 'interactive':
            Nin = get_click_position(np.log10(Sexp2_in),title='Nin')
        elif isinstance(Nin, str) and Nin == 'all':
            eps = np.finfo(float).eps
            Nin = len(np.where(Sexp2_in/Sexp2_in[0]>1e5*eps)[0])
        print('Using %d spatial dimensions' % Nin)

        # select vectors to use
        if Nout is None:
            ttext = 'enter the spatial dimension for the outside field: '
            Nout = int(input(ttext))
        elif isinstance(Nout, str) and Nout == 'interactive':
            Nout = get_click_position(np.log10(Sexp2_out),title='Nout')
        elif isinstance(Nout, str) and Nout == 'all':
            eps = np.finfo(float).eps
            Nout = len(np.where(Sexp2_out/Sexp2_out[0]>1e5*eps)[0])
        print('Using %d spatial dimensions' % Nout)

        V_in = Vh_in.T
        V_out = Vh_out.T

        Q_in = V_in[:,:Nin]
        Q_out = V_out[:,:Nout]
        # common temporal subspace
        C = np.dot(Q_in.T,Q_out)
        
        # Compute angles between subspace and which bases to keep
        U_intersec,Sexp2_intersec,Vh_intersec = _safe_svd(C, full_matrices=False)

        if isinstance(Nee, str) and Nee == 'auto':
            raise ValueError('automatic determination of intersection dimension is not supported')
        elif isinstance(Nee, str) and Nee == 'interactive':
            Nee = get_click_position(np.log10(Sexp2_intersec),title='Nee')
        elif Nee < 1:
            # treat a numeric value < 1 as a threshold
            Nee = len(np.where(Sexp2_intersec >= Nee)[0])
        print('Using %d spatial dimensions' % Nee)

        G = np.dot(Q_in, U_intersec)
        # G = np.dot(Q_out, Vh_intersec.T)
        G = G[:,:Nee]
        Bclean = B - np.dot(np.dot(B, G), G.T)

    elif flag == 0:
        # MNE 方法
        check_disable = dict(check_finite=False)
        data_int = copy.deepcopy(B_in)
        data_res =  copy.deepcopy(B_out)

        n = np.linalg.norm(data_int)
        n = 1.0 if n == 0 else n  # all-zero data should gracefully continue
        data_int = _orth_overwrite((data_int / n).T)
        n = np.linalg.norm(data_res)
        n = 1.0 if n == 0 else n
        data_res = _orth_overwrite((data_res / n).T)

        Q_int = linalg.qr(data_int, overwrite_a=True, mode="economic", **check_disable)[0].T
        Q_res = linalg.qr(data_res, overwrite_a=True, mode="economic", **check_disable)[0]
        C_mat = np.dot(Q_int, Q_res)
        del Q_int
        S_intersect, Vh_intersect = _safe_svd(C_mat, full_matrices=False, **check_disable)[1:]
        del C_mat
        intersect_mask = S_intersect >= st_correlation
        del S_intersect
        Vh_intersect = Vh_intersect[intersect_mask].T
        t_proj = np.dot(Q_res, Vh_intersect)

        Bclean = B - np.dot(np.dot(B, t_proj), t_proj.T)

    raw_clean = raw.copy()
    raw_clean._data[picks_good,:] = Bclean

    return raw_clean

