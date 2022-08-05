# MyPredict
 This repository contains the supporting code for the Roessingh Research & Development-MyLeg database for activity prediction (MyPredict). This database consists of 55 subjects measured in 85 measurement moments. The measurement data are stored in seperate HDF5 files per subject. This repository aims to provide code to facilitate the loading and processing of the data from this database.
 
[MyPredict 1](https://doi.org/10.4121/20418720)  
10 able-bodied subjects (sex: 7m, 3f; age: 24±2 years; weight: 77±10 kg; height: 183±9cm) 

[MyPredict 2](https://doi.org/10.4121/20418687)  
35 able-bodied subjects (sex: 14m, 21f; age: 23±2 years; weight: 73±11 kg; height: 179±9 cm)

[MyPredict 3](https://doi.org/10.4121/20430741)  
10 able-bodied subjects (sex: 4m, 6f; age: 24±2 years; weight: 71±9 kg; height: 174±6 cm)  

## File structure
Each dataset (MyPredict 1-3) exists of seperate HDF5 files per subject. Each HDF5 file consists of the following structure. Herein is Day_X the measurement day (X: 1-4), Trial_YY the trial containing measurement data (YY: 01-..), MVC the Maximum Voluntary Contraction  (if applicable), uTrial_ZZ the unlabeled trials (ZZ: 01-.., if applicable), Meta contains the subject meta data.
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
