# -*- coding:utf-8 -*-

import numpy as np
import math as m

WIE = 15.0 / 3600
lat = 30.53
w_en = WIE * m.cos(lat * m.pi / 180)
w_eu = WIE * m.sin(lat * m.pi / 180)
w_ew = 0
wie = np.array([w_en, -w_ew, -w_eu])

filepath = "../original data/Group1CalibrateData/ImuArray_1_1_IMU.bin"
path = '../original data/Group1CalibrateData/'
outpath = "../Group1CalibrateResult/"
data = np.fromfile(filepath).reshape(-1, 7)

# the moment of the rotation movement
t1_sta = 265
t1_sta = np.where(data[:, 0] > t1_sta)[0][0]
t1_end = 325
t1_end = np.where(data[:, 0] > t1_end)[0][0]
t2_sta = 385
t2_sta = np.where(data[:, 0] > t2_sta)[0][0]
t2_end = 445
t2_end = np.where(data[:, 0] > t2_end)[0][0]
t3_sta = 710
t3_sta = np.where(data[:, 0] > t3_sta)[0][0]
t3_end = 770
t3_end = np.where(data[:, 0] > t3_end)[0][0]
t4_sta = 800
t4_sta = np.where(data[:, 0] > t4_sta)[0][0]
t4_end = 860
t4_end = np.where(data[:, 0] > t4_end)[0][0]
t5_sta = 1480
t5_sta = np.where(data[:, 0] > t5_sta)[0][0]
t5_end = 1540
t5_end = np.where(data[:, 0] > t5_end)[0][0]
t6_sta = 1575
t6_sta = np.where(data[:, 0] > t6_sta)[0][0]
t6_end = 1635
t6_end = np.where(data[:, 0] > t6_end)[0][0]

t_totle = 60
table_angle = 1440

earth_angle = w_eu * t_totle  # too small compared to 1440 and measurement noise, can be ignored

# observations
Y = np.array([[0, 0, -table_angle], [0, 0, table_angle], 
              [0, table_angle, 0], [0, -table_angle, 0], 
              [-table_angle, 0, 0], [table_angle, 0, 0]])
Y = Y.T

# to preserve the calibration parameters
scale = np.zeros([16, 12])

# calibrate an IMU per cycle
for i in range(1, 3):
    for j in range(1, 9):
        filename = 'ImuArray_' + str(i) + '_' + str(j) + '_IMU.bin'
        filepath = path + filename
        data = np.fromfile(filepath).reshape(-1, 7)

        # state vector
        angle_1 = sum(data[t1_sta:t1_end, 1:4] * np.mean(np.diff(data[t1_sta:t1_end, 0])))
        angle_2 = sum(data[t2_sta:t2_end, 1:4] * np.mean(np.diff(data[t2_sta:t2_end, 0])))
        angle_3 = sum(data[t3_sta:t3_end, 1:4] * np.mean(np.diff(data[t3_sta:t3_end, 0])))
        angle_4 = sum(data[t4_sta:t4_end, 1:4] * np.mean(np.diff(data[t4_sta:t4_end, 0])))
        angle_5 = sum(data[t5_sta:t5_end, 1:4] * np.mean(np.diff(data[t5_sta:t5_end, 0])))
        angle_6 = sum(data[t6_sta:t6_end, 1:4] * np.mean(np.diff(data[t6_sta:t6_end, 0])))

        H = np.array([np.append(angle_1, 1), np.append(angle_2, 1), np.append(angle_3, 1),
                      np.append(angle_4, 1), np.append(angle_5, 1), np.append(angle_6, 1)])
        H = H.T

        # the least square method
        temp1 = np.matmul(H, H.T)
        temp1 = np.linalg.inv(temp1)
        temp2 = np.matmul(Y, H.T)
        X = np.matmul(temp2, temp1)

        # perserve the parameters
        k = (i - 1) * 8 + j - 1
        bias = X[0:3, 3] / t_totle
        scale[k, 0:3] = X[0, 0:3]
        scale[k, 3:6] = X[1, 0:3]
        scale[k, 6:9] = X[2, 0:3]
        scale[k, 9:12] = bias[0:3]

        # newdata = np.matmul(X[0:3, 0:3] * (data[:, 1:4]).T) + bias
        # newdata = newdata.T
        print(filename)

# save calibration parameters
txtpath = outpath + 'GyrosParamGroup1.txt'
np.savetxt(txtpath, scale)
