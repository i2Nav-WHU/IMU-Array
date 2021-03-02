#!/usr/bin/python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'

path = '../original data/Group1CalibrateData/'
filename = 'ImuArray_1_3_IMU.bin'
filepath = path + filename

gyros_param_path = '../original data/CalibrateResult/GyrosParamGroup1.txt'
accel_param_path = '../original data/CalibrateResult/AccelParamGroup1.txt'

imu = np.fromfile(filepath).reshape(-1, 7)
dt = np.mean(np.diff(imu[:, 0]))

fig1 = plt.figure(filename[:-4] + 'gyros1')
plt.title('Gyroscope uncomponsated')
plt.xlabel('Time[s]')
plt.ylabel('angle velocity[deg/s]')
plt.plot(imu[:, 0], imu[:, 1], label='x', color='blue')
plt.plot(imu[:, 0], imu[:, 2], label='y', color='green')
plt.plot(imu[:, 0], imu[:, 3], label='z', color='red')
plt.legend()
plt.grid()
plt.tight_layout()

fig2 = plt.figure(filename[:-4] + 'accel1')
plt.title('Accelrometer uncomponsated')
plt.xlabel('Time[s]')
plt.ylabel(r'acceleration[$m/s^2$]')
plt.plot(imu[:, 0], imu[:, 4], label='x', color='blue')
plt.plot(imu[:, 0], imu[:, 5], label='y', color='green')
plt.plot(imu[:, 0], imu[:, 6], label='z', color='red')
plt.legend()
plt.grid()
plt.tight_layout()

g_param = np.loadtxt(gyros_param_path)
a_param = np.loadtxt(accel_param_path)
i = int(filename[9])
j = int(filename[11])
k = (i - 1) * 8 + j

Ka = np.zeros([3, 3])
bias = np.zeros([3, 1])
Ka[0, :] = g_param[k-1, 0:3]
Ka[1, :] = g_param[k-1, 3:6]
Ka[2, :] = g_param[k-1, 6:9]
bias[:, 0] = g_param[k-1, 9:12]
imu[:, 1:4] = (np.matmul(Ka, np.transpose(imu[:, 1:4])) + bias).T

Ka = np.zeros([3, 3])
bias = np.zeros([3, 1])
Ka[0, :] = a_param[k-1, 0:3]
Ka[1, :] = a_param[k-1, 3:6]
Ka[2, :] = a_param[k-1, 6:9]
bias[:, 0] = a_param[k-1, 9:12]
imu[:, 4:7] = (np.matmul(Ka, np.transpose(imu[:, 4:7])) + bias).T

fig3 = plt.figure(filename[:-4] + 'gyros2')
plt.title('Gyroscope compensated')
plt.xlabel('Time[s]')
plt.ylabel('angle velocity[deg/s]')
plt.plot(imu[:, 0], imu[:, 1], label='x', color='blue')
plt.plot(imu[:, 0], imu[:, 2], label='y', color='green')
plt.plot(imu[:, 0], imu[:, 3], label='z', color='red')
plt.legend()
plt.grid()
plt.tight_layout()

fig4 = plt.figure(filename[:-4] + 'accel2')
plt.title('Accelrometer compensated')
plt.xlabel('Time[s]')
plt.ylabel(r'acceleration[$m/s^2$]')
plt.plot(imu[:, 0], imu[:, 4], label='x', color='blue')
plt.plot(imu[:, 0], imu[:, 5], label='y', color='green')
plt.plot(imu[:, 0], imu[:, 6], label='z', color='red')
plt.legend()
plt.grid()
plt.tight_layout()

plt.show()
