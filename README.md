# Overview

Python code related to the paper *"Artifact Suppression in OPM-MEG for Parkinson’s Disease Patients with DBS Implants Using Oblique Projection-Based Extended Homogeneous Field Correction"*


# opHFC
For details related to `opHFC`, please refer to the paper: 


- [1] Wang F, Cao F, Ma Y, et al. Extended homogeneous field correction method based on oblique projection in OPM-MEG[J]. NeuroImage, 2025: 120991.
 [DOI: https://doi.org/10.1016/j.neuroimage.2024.120991](https://doi.org/10.1016/j.neuroimage.2024.120991)
- [2] Wang F, Cao F, An, N, et al. Artifact Suppression in OPM-MEG for Parkinson's Disease Patients with DBS Implants Using Oblique Projection-Based Extended Homogeneous Field Correction[J]. IEEE Journal of Biomedical and Health Informatics, 2025.

# Note
- `SSP` were implemented using functions [mne.compute_proj_raw](https://mne.tools/stable/generated/mne.compute_proj_raw.html#mne.compute_proj_raw) provided in the MNE-Python.
-  `HFC` were implemented using functions [mne.preprocessing.compute_proj_hfc](https://mne.tools/stable/generated/mne.preprocessing.compute_proj_hfc.html#mne.preprocessing.compute_proj_hfc) provided in the MNE-Python.
- The file `wfl_preproc_dssp.py` is a Python implementation of the `DSSP` [2] method.
- `AMM` was implemented using the spm_opm_amm.m function from the [SPM toolbox](https://github.com/spm/spm) in MATLAB.
- The file `wfl_preproc_opHFC.py` is a Python implementation of the `opHFC` [5] method.

# Quick start
Using the `opHFC` code requires leadfield matrix. To obtain the lead field matrix, please refer to the following steps：
- Using fwd = [mne.make_forward_solution(...)](https://mne.tools/stable/generated/mne.make_forward_solution.html#mne.make_forward_solution) function to calculate a forward solution for a subject.
- The leadfield matrix can be obtained using `LF = fwd["sol"]["data"]`.


## Example Code
```python
from wfl_preproc_opHFC import opHFC
raw = mne.io.read_raw_fif(raw_path)
raw_room = mne.io.read_raw_fif(raw_room_path)
# LF: leadfield matrix
# Nnoise: Number component of noise
# Nsignal: Number component of signal
# Nout: Number component of noise for oblique projection
# Nin: Number component of signal for oblique projection
# Nee: Number component for temporally extended
raw_opHFC = opHFC(raw=raw,
                  raw_room=raw_room,
                  leadfield=LF,
                  Nnoise=Nnoise,
                  Nsignal=Nsignal,
                  Nout=Nout,
                  Nin=Nin,
                  Nee=Nee)
```


# Cite

- [1] Uusitalo M A, Ilmoniemi R J. Signal-space projection method for separating MEG or EEG into components[J]. Medical & Biological Engineering & Computing, 1997, 35(2): 135-140.[DOI: https://doi.org/10.1007/BF02534144](https://doi.org/10.1007/BF02534144)
- [2] Sekihara K, Kawabata Y, Ushio S, et al. Dual signal subspace projection (DSSP): a novel algorithm for removing large interference in biomagnetic measurements[J]. Journal of Neural Engineering, 2016, 13(3): 036007.[DOI: https://doi.org/10.1088/1741-2560/13/3/036007](https://doi.org/10.1088/1741-2560/13/3/036007)
- [3] Tierney T M, Alexander N, Mellor S, et al. Modelling optically pumped magnetometer interference in MEG as a spatially homogeneous magnetic field[J]. NeuroImage, 2021, 244: 118484.[DOI: https://doi.org/10.1016/j.neuroimage.2021.118484](https://doi.org/10.1016/j.neuroimage.2021.118484)
- [4] Tierney T M, Seedat Z, St Pier K, et al. Adaptive multipole models of optically pumped magnetometer data[J]. Human Brain Mapping, 2024, 45(4): e26596.
- [5] Wang F, Cao F, Ma Y, et al. Extended homogeneous field correction method based on oblique projection in OPM-MEG[J]. NeuroImage, 2025: 120991.[DOI: https://doi.org/10.1016/j.neuroimage.2024.120991](https://doi.org/10.1016/j.neuroimage.2024.120991)





