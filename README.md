# 🧠 Overview

This repository provides Python code accompanying the paper  
*“Artifact Suppression in OPM-MEG for Parkinson’s Disease Patients with DBS Implants Using Oblique Projection-Based Extended Homogeneous Field Correction.”*

The repository contains implementations of several interference suppression algorithms used in OPM-MEG, including **SSP**, **HFC**, **DSSP**, **AMM**, and the proposed **opHFC** method.

---

# ⚙️ opHFC

For detailed descriptions of the `opHFC` method, please refer to the following publications:

- [1] Wang F, Cao F, Ma Y, et al. *Extended homogeneous field correction method based on oblique projection in OPM-MEG.* **NeuroImage**, 2025: 120991.  
  [DOI: https://doi.org/10.1016/j.neuroimage.2024.120991](https://doi.org/10.1016/j.neuroimage.2024.120991)

- [2] Wang F, Cao F, An N, et al. *Artifact Suppression in OPM-MEG for Parkinson’s Disease Patients with DBS Implants Using Oblique Projection-Based Extended Homogeneous Field Correction.* **IEEE Journal of Biomedical and Health Informatics**, 2025.

---

# 📘 Notes

- **SSP** [[1]](#cite) was implemented using the MNE-Python function [`mne.compute_proj_raw`](https://mne.tools/stable/generated/mne.compute_proj_raw.html#mne.compute_proj_raw).  
- **HFC** [[3]](#cite) was implemented using the MNE-Python function [`mne.preprocessing.compute_proj_hfc`](https://mne.tools/stable/generated/mne.preprocessing.compute_proj_hfc.html#mne.preprocessing.compute_proj_hfc).  
- **DSSP** [[2]](#cite) was implemented in Python as `wfl_preproc_dssp.py`.  
- **AMM** [[4]](#cite) was implemented using the `spm_opm_amm.m` function from the [SPM toolbox](https://github.com/spm/spm) in MATLAB.  
- **opHFC** [[5]](#cite) was implemented in Python as `wfl_preproc_opHFC.py`.

---

# 🚀 Quick Start

Using the `opHFC` code requires a **lead field matrix**.  
You can generate it in MNE-Python by following these steps:

1. Compute the forward solution using  
   [`mne.make_forward_solution()`](https://mne.tools/stable/generated/mne.make_forward_solution.html#mne.make_forward_solution):  
   ```python
     fwd = mne.make_forward_solution(...)

2. Example Code
   ```python
    from wfl_preproc_opHFC import opHFC
    import mne
    
    raw = mne.io.read_raw_fif(raw_path)
    raw_room = mne.io.read_raw_fif(raw_room_path)
    
    # Parameters:
    # LF: Lead field matrix
    # Nnoise: Number of noise components
    # Nsignal: Number of signal components
    # Nout, Nin: Components for oblique projection
    # Nee: Number of temporally extended components
    
    raw_opHFC = opHFC(
        raw=raw,
        raw_room=raw_room,
        leadfield=LF,
        Nnoise=Nnoise,
        Nsignal=Nsignal,
        Nout=Nout,
        Nin=Nin,
        Nee=Nee
    )


# Cite

- [1] Uusitalo M A, Ilmoniemi R J. Signal-space projection method for separating MEG or EEG into components[J]. Medical & Biological Engineering & Computing, 1997, 35(2): 135-140.[DOI: https://doi.org/10.1007/BF02534144](https://doi.org/10.1007/BF02534144)
- [2] Sekihara K, Kawabata Y, Ushio S, et al. Dual signal subspace projection (DSSP): a novel algorithm for removing large interference in biomagnetic measurements[J]. Journal of Neural Engineering, 2016, 13(3): 036007.[DOI: https://doi.org/10.1088/1741-2560/13/3/036007](https://doi.org/10.1088/1741-2560/13/3/036007)
- [3] Tierney T M, Alexander N, Mellor S, et al. Modelling optically pumped magnetometer interference in MEG as a spatially homogeneous magnetic field[J]. NeuroImage, 2021, 244: 118484.[DOI: https://doi.org/10.1016/j.neuroimage.2021.118484](https://doi.org/10.1016/j.neuroimage.2021.118484)
- [4] Tierney T M, Seedat Z, St Pier K, et al. Adaptive multipole models of optically pumped magnetometer data[J]. Human Brain Mapping, 2024, 45(4): e26596.
- [5] Wang F, Cao F, Ma Y, et al. Extended homogeneous field correction method based on oblique projection in OPM-MEG[J]. NeuroImage, 2025: 120991.[DOI: https://doi.org/10.1016/j.neuroimage.2024.120991](https://doi.org/10.1016/j.neuroimage.2024.120991)





