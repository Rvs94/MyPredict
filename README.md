# MyPredict
 This repository contains the supporting code for the Roessingh Research & Development-MyLeg database for activity prediction (MyPredict). This database consists of 55 subjects measured in 85 measurement moments. The measurement data are stored in seperate HDF5 files per subject. This repository aims to provide code to facilitate the loading and processing of the data from this database.
 
[MyPredict 1](doi.org/10.4121/20418720)  
[MyPredict 2](doi.org/10.4121/20418687)  
[MyPredict 3](doi.org/10.4121/20430741)  

## File structure
Each dataset (MyPredict 1-3) exists of seperate HDF5 files per subject. Each HDF5 file consists of the following structure. Herein is Day_X the measurement day (X: 1-4), Trial_YY the trial containing measurement data (YY: 01-..), MVC the Maximum Voluntary Contraction  (if applicable), uTrial_ZZ the unlabeled trials (ZZ: 01-.., if applicable). Meta contains the subject meta data, which can be found in [meta_data](doc/220805_MyPredict_MetaData.pdf) as well.
```
MyPredict 1
├── MP101.hdf5
| ├── Day_X
| | ├── Trial_YY
| | | ├── Acc_Right_Thigh
| | | ├── ...
| | ├── (MVC)
| | └── (uTrial_ZZ)
| └── Meta
├── MP102.hdf5
...
```
## Code
