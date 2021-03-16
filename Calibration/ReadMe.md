Files in this folder:



#### Group1_ref_data.bin:

The reference truth value of acceleration and angular velocity during Group 1 calibration. In this file, 'nan' represents that we can not determine the reference value at that time.





### \Algorithm:

 calibration pargram

#### accelcalib.py:

Accelrometer calibration code written by python.



#### gyroscalib.py: 

Gyroscope calibration code written by python.



#### calibrae_plot.py:

 Plot the IMU measurement before and after conpensating for calibration parameter.





### \Group1CompendatedData:

The measurement of 16 IMUs after compensating for calibration parameters.





### \Group1CalibrationResult: 

calibration result of accelrometer and gyroscope
The result file contains 16 lines, and each line an IMU's parameter of the IMU array.
Each line has 12 values, the first nine are the nine values in the coefficient matrix, and the last three are the constant zero offsets of the three axes.





### \original data: 

the raw IMU observation in 
The files contain in this subfolder are 7 columns of binary files, all of which are "double" type data.
The 7 columns of data are:
time(s), Gyro_x(deg/s) , Gyro_y(deg/s), Guro_z(deg/s), Accel_x(m/s^2), Accel_y(m/s^2), Accel_z(m/s^2)

 

