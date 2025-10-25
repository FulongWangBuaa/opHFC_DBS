# Overview

Python code related to the paper *"Artifact Suppression in OPM-MEG for Parkinson’s Disease Patients with DBS Implants Using Oblique Projection-Based Extended Homogeneous Field Correction"*


# opHFC
For details related to `opHFC`, please refer to the paper: 


- [1] Wang F, Cao F, Ma Y, et al. Extended homogeneous field correction method based on oblique projection in OPM-MEG[J]. NeuroImage, 2025: 120991.
 [DOI: https://doi.org/10.1016/j.neuroimage.2024.120991](https://doi.org/10.1016/j.neuroimage.2024.120991)
- [2] Wang F, Cao F, An, N, et al. Artifact Suppression in OPM-MEG for Parkinson's Disease Patients with DBS Implants Using Oblique Projection-Based Extended Homogeneous Field Correction[J]. IEEE Journal of Biomedical and Health Informatics, 2025.

# Other methods
SSP and HFC: The SSP and HFC methods were implemented using functions provided in the MNE-Python
DSSP: wfl_preproc_dssp.py
AMM: The AMM method was implemented using the spm_opm_amm.m function from the SPM toolbox in MATLAB.
opHFC: wfl_preproc_opHFC.py

# Cite

- [1] Uusitalo M A, Ilmoniemi R J. Signal-space projection method for separating MEG or EEG into components[J]. Medical & Biological Engineering & Computing, 1997, 35(2): 135-140.[DOI: https://doi.org/10.1007/BF02534144](https://doi.org/10.1007/BF02534144)
- [2] Sekihara K, Kawabata Y, Ushio S, et al. Dual signal subspace projection (DSSP): a novel algorithm for removing large interference in biomagnetic measurements[J]. Journal of Neural Engineering, 2016, 13(3): 036007.[DOI: https://doi.org/10.1088/1741-2560/13/3/036007](https://doi.org/10.1088/1741-2560/13/3/036007)
- [3] Tierney T M, Alexander N, Mellor S, et al. Modelling optically pumped magnetometer interference in MEG as a spatially homogeneous magnetic field[J]. NeuroImage, 2021, 244: 118484.[DOI: https://doi.org/10.1016/j.neuroimage.2021.118484](https://doi.org/10.1016/j.neuroimage.2021.118484)
- [4] Tierney T M, Seedat Z, St Pier K, et al. Adaptive multipole models of optically pumped magnetometer data[J]. Human Brain Mapping, 2024, 45(4): e26596.
- [5] Wang F, Cao F, Ma Y, et al. Extended homogeneous field correction method based on oblique projection in OPM-MEG[J]. NeuroImage, 2025: 120991.[DOI: https://doi.org/10.1016/j.neuroimage.2024.120991](https://doi.org/10.1016/j.neuroimage.2024.120991)





