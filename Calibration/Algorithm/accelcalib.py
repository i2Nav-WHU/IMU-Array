#! -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# the local gravity
G = 9.79359005747261

filepath = "../original data/Group1CalibrateData/ImuArray_1_1_IMU.bin"
path = '../original data/Group1CalibrateData/'
outpath = '../original data/CalibrateResult/'
data = np.fromfile(filepath).reshape(-1, 7)
dt = np.mean(np.diff(data[:, 0]))

# the stable time at each position
t1_sta = 80
t1_sta = np.where(data[:, 0] > t1_sta)[0][0]
t1_end = 200
t1_end = np.where(data[:, 0] > t1_end)[0][0]
t2_sta = 510
t2_sta = np.where(data[:, 0] > t2_sta)[0][0]
t2_end = 630
t2_end = np.where(data[:, 0] > t2_end)[0][0]
t3_sta = 930
t3_sta = np.where(data[:, 0] > t3_sta)[0][0]
t3_end = 1050
t3_end = np.where(data[:, 0] > t3_end)[0][0]
t4_sta = 1150
t4_sta = np.where(data[:, 0] > t4_sta)[0][0]
t4_end = 1270
t4_end = np.where(data[:, 0] > t4_end)[0][0]
t5_sta = 1320
t5_sta = np.where(data[:, 0] > t5_sta)[0][0]
t5_end = 1440
t5_end = np.where(data[:, 0] > t5_end)[0][0]
t6_sta = 1710
t6_sta = np.where(data[:, 0] > t6_sta)[0][0]
t6_end = 1830
t6_end = np.where(data[:, 0] > t6_end)[0][0]

# observations
Y = np.array([[0, 0, G], [0, -G, 0], [0, 0, -G], [0, G, 0], [G, 0, 0],
              [-G, 0, 0]])
Y = Y.T

# to perseve the calibration parameterss
scale = np.zeros([16, 12])

for i in range(1, 3):
    for j in range(1, 9):
        filename = 'ImuArray_' + str(i) + '_' + str(j) + '_IMU.bin'
        filepath = path + filename
        data = np.fromfile(filepath).reshape(-1, 7)

        # state vector
        pos_1 = np.mean(data[t1_sta:t1_end, 4:7], 0)
        pos_2 = np.mean(data[t2_sta:t2_end, 4:7], 0)
        pos_3 = np.mean(data[t3_sta:t3_end, 4:7], 0)
        pos_4 = np.mean(data[t4_sta:t4_end, 4:7], 0)
        pos_5 = np.mean(data[t5_sta:t5_end, 4:7], 0)
        pos_6 = np.mean(data[t6_sta:t6_end, 4:7], 0)

        H = np.array([
            np.append(pos_1, 1),
            np.append(pos_2, 1),
            np.append(pos_3, 1),
            np.append(pos_4, 1),
            np.append(pos_5, 1),
            np.append(pos_6, 1)
        ])
        H = H.T

        # the least sqare method
        temp1 = np.matmul(H, H.T)
        temp1 = np.linalg.inv(temp1)
        temp2 = np.matmul(Y, H.T)
        X = np.matmul(temp2, temp1)

        # bias = np.zeros([3, 1])
        # bias[:, 0] = X[0:3, 3]

        # perseve the parameters
        k = (i - 1) * 8 + j - 1
        scale[k, 0:3] = X[0, 0:3]
        scale[k, 3:6] = X[1, 0:3]
        scale[k, 6:9] = X[2, 0:3]
        scale[k, 9:12] = X[0:3, 3]

        # newdata = np.matmul(X[0:3, 0:3], (data[:, 4:7]).T) + bias
        # newdata = newdata.T
        print(filename)

# save file
txtpath = outpath + 'AccelParamGroup1.txt'
np.savetxt(txtpath, scale)
