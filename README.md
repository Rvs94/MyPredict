# MyPredict
This repository contains the supporting code for the Roessingh Research & Development-MyLeg database for activity prediction ([MyPredict]([https://doi.org/10.4121/c.6128343])(https://doi.org/10.4121/20418720)). This database consists of 55 subjects measured in 85 measurement moments. The measurement data are stored in seperate HDF5 files per subject. This repository aims to provide code to facilitate the loading and processing of the data from this database. This database contains lower body kinematics and EMG during gait-related activities such as level-ground walking, stair/ramp climbing and sit/stance. 
 
MyPredict 1
10 able-bodied subjects (sex: 7m, 3f; age: 24±2 years; weight: 77±10 kg; height: 183±9cm)  
1 measurement day (Day 1)

MyPredict 2
35 able-bodied subjects (sex: 14m, 21f; age: 23±2 years; weight: 73±11 kg; height: 179±9 cm)  
1 measurement day (Day 1)

MyPredict 3
10 able-bodied subjects (sex: 4m, 6f; age: 24±2 years; weight: 71±9 kg; height: 174±6 cm)  
4 measurement days (Day 1, 2, 3, 7)

## File structure
Each dataset (MyPredict 1-3) exists of seperate HDF5 files per subject. Each HDF5 file consists of the following structure. Herein is Day_X the measurement day (X: 1-4), Trial_YY the trial containing measurement data (YY: 01-..), MVC the Maximum Voluntary Contraction  (if applicable), NoLabel_ZZ the unlabeled trials (ZZ: 01-.., if applicable), Meta contains the subject meta data.
```
MyPredict 1
├── MP101.hdf5
| ├── Day_X
| | ├── Trial_YY
| | | ├── Acc_Right_Thigh
| | | ├── ...
| | ├── (MVC)
| | └── (NoLabel_ZZ)
| └── Meta
├── MP102.hdf5
...
```
## Code & Labels
The folder 'code' contains an example script on how to load the MyPredict data sets. It requires python 3.x, matplotlib and [h5py](https://www.h5py.org/). The gait related activities in the data are labelled as follows:
|     Label    |     Definition                                                |
|--------------|---------------------------------------------------------------|
|     -2       |     Between tracks                                            |
|     -1       |     Error in data                                             |
|     0        |     Sitting                                                   |
|     1        |     Standing                                                  |
|     2        |     Walking                                                   |
|     2.1      |     Turn (around axes)                                        |
|     3        |     Ascending   stairs                                        |
|     4        |     Descending stairs                                         |
|     5        |     Ascending a   ramp                                        |
|     6        |     Descending a ramp                                         |
|     7        |     Walking on   uneven terrain                               |
|     7.1      |     Walking on uneven terrain (grass)                         |
|     7.2      |     Walking on   uneven terrain (for track 3, middle part)    |
|     7.3      |     Walking on uneven terrain (for track 3, last part)        |
|     8.1      |     Diagonal step   in front left                             |
|     8.2      |     Diagonal step in front right                              |
|     8.3      |     Diagonal step   backwards right                           |
|     8.4      |     Diagonal step backwards left                              |
|     8.5      |     Small steps in   front                                    |
|     8.6      |     Small steps to the right                                  |
|     8.7      |     Small steps   backwards                                   |
|     8.8      |     Small steps to the left                                   |
|     9        |     Laying down                                               |


