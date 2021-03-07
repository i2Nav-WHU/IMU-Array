files contain in this folder:



### Folder:

#### \CalibrationParam:

 Calibration result of the first IMU array



#### \Group1CompensatedData: 

The measurement of each IMU and the IMU array after conpensation for calibration parameters

binary files, 7 columns of "double" data: time(s), Gryos_x[rad], Gyros_y[rad], Gyros_z[rad], Accel_x[m/s], Accel_y[m/s], Accel_z[m/s]



#### \Group1OriginData: 

The raw measurement of each IMU in incremental form

binary files, 7 columns of "double" data: time(s), Gryos_x[rad], Gyros_y[rad], Gyros_z[rad], Accel_x[m/s], Accel_y[m/s], Accel_z[m/s]



### Docs:

#### ErrorParameter.txt:

 ARW, VRW, BG and BA parameters used in Integrated Navigation Solution

The antenna lever-arm of the first IMU array.



#### gnss_group1.txt: 

GNSS positioning result, Obtained from the differential operation of the base station and the rover

7 columns text file: time(s), latitude(deg)， longitude(deg), height(m), std_n(m), std_e(m), std_u(m)



#### LC_OUTAGE30S.err: 

the IMU array's navigation error with 30s GNSS outage 

10 columns text file: 

time(s), north_err, east_err, down_err(m), vel_n_err(m/s),vel_e_err(m/s),vel_d_err(m/s) ,roll_err(deg),  pitch_err(deg), yaw_err(deg)



#### LC_OUTAGE30S.nav: 

the IMU array's navigation error with 30s GNSS outage

11 columns text file:

week(set to 0), time(s), latitude(deg), longitude(deg), height(m), vel_n(m/s), vel_e(m/s), vel_d(m/s), roll(deg), pitch(deg), yaw(deg)



#### ReadMe.md: 

this file



#### RefNavResult: 

Reference navigation result, combine the inertial measurement value of Leador-A15 and the GNSS positioning result through the Rauch-Tung-Striebel smoother

11 columns text file:

week(set to 0), time(s), latitude(deg), longitude(deg), height(m), vel_n(m/s), vel_e(m/s), vel_d(m/s), roll(deg), pitch(deg), yaw(deg)



#### vehicle_bank1_rms_summary.xlsx: 

Plane position error of each IMU in the first IMU array at three different outage start times