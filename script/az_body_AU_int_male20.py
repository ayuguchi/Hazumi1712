# -*- encoding: UTF-8 -*-
import sys
import csv
from turtle import st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

#start_time = []
au01 = []
au02 = []
au04 = []
au05 = []
au45 = []

row = 2 #2
col = 3 #3

def main():
    d_20m1_dump = pd.read_csv('../dumpfiles/1712M2007.csv')
    d_20m2_dump = pd.read_csv('../dumpfiles/1712M2021.csv')
    d_20m3_dump = pd.read_csv('../dumpfiles/1712M2024.csv')
    d_20m4_dump = pd.read_csv('../dumpfiles/1712M2028.csv')
    d_20m5_dump = pd.read_csv('../dumpfiles/1712M2029.csv')

    e_20m1_int = pd.read_csv('../script/1712M2007_int_level.csv')
    e_20m2_int = pd.read_csv('../script/1712M2021_int_level.csv')
    e_20m3_int = pd.read_csv('../script/1712M2024_int_level.csv')
    e_20m4_int = pd.read_csv('../script/1712M2028_int_level.csv')
    e_20m5_int = pd.read_csv('../script/1712M2029_int_level.csv')

#    d_20f1_kinect = pd.read_csv('../kinect/1712F2006/Body/BodyData.csv')
#    d_20f2_kinect = pd.read_csv('../kinect/1712F2010/Body/BodyData.csv')
#    d_20f3_kinect = pd.read_csv('../kinect/1712F2018/Body/BodyData.csv')
#    d_20f4_kinect = pd.read_csv('../kinect/1712F2019/Body/BodyData.csv')

### M1
    start_time_m1 = d_20m1_dump['end(system)[ms]'].values
    au01_array_m1 = d_20m1_dump['AU01_c_mean'].values
    au02_array_m1 = d_20m1_dump['AU02_c_mean'].values
    head_vel_max_array_m1 = d_20m1_dump['Head_velocity_max'].values
    head_vel_max_array_m1 = head_vel_max_array_m1 * 10
#    shoulderRight_vel_max_array_f1 = d_20f1_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f1 = shoulderRight_vel_max_array_f1 * 10
#    shoulderLeft_vel_max_array_f1 = d_20f1_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f1 = shoulderLeft_vel_max_array_f1 * 10

    dif_au01_m1 = np.diff(au01_array_m1)
    dif_au02_m1 = np.diff(au02_array_m1)
#    dif_au45 = np.diff(au45_array)

    e_20m1_int = e_20m1_int.set_axis(['ID','interest_level'], axis=1)
    auHeadInterest_dump_m1 = pd.concat([d_20m1_dump['end(system)[ms]'],d_20m1_dump['AU01_c_mean'],d_20m1_dump['AU02_c_mean'],d_20m1_dump['Head_velocity_max'],e_20m1_int['interest_level']],axis=1)

    azAU_appear_m1 = auHeadInterest_dump_m1.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_m1 = auHeadInterest_dump_m1.query('Head_velocity_max > 0.075')
    azAU_Head_appear_m1 = azHead_appear_m1.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    negInterest_appear_m1 = auHeadInterest_dump_m1.query('interest_level == -1')
    posInterest_appear_m1 = auHeadInterest_dump_m1.query('interest_level == 1')

    negIntAzHead_appear_m1 = negInterest_appear_m1.query('Head_velocity_max > 0.075')
    posIntAzHead_appear_m1 = posInterest_appear_m1.query('Head_velocity_max > 0.075')

    negIntAzAU_Head_appear_m1 = negIntAzHead_appear_m1.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    posIntAzAU_Head_appear_m1 = posIntAzHead_appear_m1.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')

    print('AU appearance rate of m1', float(len(azAU_appear_m1)/len(auHeadInterest_dump_m1)))
    print('Head appearance rate of m1', float(len(azHead_appear_m1)/len(auHeadInterest_dump_m1)))
    print('AU_Head appearance rate of m1', float(len(azAU_Head_appear_m1)/len(auHeadInterest_dump_m1)))

    print('Head appearance rate of m1 in positive interest', float(len(posIntAzHead_appear_m1)/len(posInterest_appear_m1)))
    print('AU_Head appearance rate of m1 in positive interest', float(len(posIntAzAU_Head_appear_m1)/len(posInterest_appear_m1)))
    print('Head appearance rate of m1 in negative interest', float(len(negIntAzHead_appear_m1)/len(negInterest_appear_m1)))
    print('AU_Head appearance rate of m1 in negative interest', float(len(negIntAzAU_Head_appear_m1)/len(negInterest_appear_m1)))

    plt.subplot(col, row, 1)#1
    plt.xlabel('time (ms)', fontsize=9)
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level', fontsize=9)

    plt.plot(start_time_m1, au01_array_m1, label='AU01', marker='.')
    plt.plot(start_time_m1, au02_array_m1, label='AU02', marker='.')
    plt.plot(start_time_m1[1:], dif_au01_m1, label='Delta of AU01', marker='.')
    plt.plot(start_time_m1[1:], dif_au02_m1, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_m1, head_vel_max_array_m1, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f3, shoulderRight_vel_max_array_f3, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f3, shoulderLeft_vel_max_array_f3, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_m1, e_20m1_int['interest_level'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712M2007', fontsize=9)
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

### M2
    start_time_m2 = d_20m2_dump['end(system)[ms]'].values
    au01_array_m2 = d_20m2_dump['AU01_c_mean'].values
    au02_array_m2 = d_20m2_dump['AU02_c_mean'].values
    head_vel_max_array_m2 = d_20m2_dump['Head_velocity_max'].values
    head_vel_max_array_m2 = head_vel_max_array_m2 * 10
#    shoulderRight_vel_max_array_f2 = d_20f2_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f2 = shoulderRight_vel_max_array_f2 * 10
#    shoulderLeft_vel_max_array_f2 = d_20f2_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f2 = shoulderLeft_vel_max_array_f2 * 10

    dif_au01_m2 = np.diff(au01_array_m2)
    dif_au02_m2 = np.diff(au02_array_m2)
#    dif_au45 = np.diff(au45_array)
    
    e_20m2_int = e_20m2_int.set_axis(['ID','interest_level'], axis=1)
    auHeadInterest_dump_m2 = pd.concat([d_20m2_dump['end(system)[ms]'],d_20m2_dump['AU01_c_mean'],d_20m2_dump['AU02_c_mean'],d_20m2_dump['Head_velocity_max'],e_20m2_int['interest_level']],axis=1)

    azAU_appear_m2 = auHeadInterest_dump_m2.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_m2 = auHeadInterest_dump_m2.query('Head_velocity_max > 0.075')
    azAU_Head_appear_m2 = azHead_appear_m2.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    negInterest_appear_m2 = auHeadInterest_dump_m2.query('interest_level == -1')
    posInterest_appear_m2 = auHeadInterest_dump_m2.query('interest_level == 1')

    negIntAzHead_appear_m2 = negInterest_appear_m2.query('Head_velocity_max > 0.075')
    posIntAzHead_appear_m2 = posInterest_appear_m2.query('Head_velocity_max > 0.075')

    negIntAzAU_Head_appear_m2 = negIntAzHead_appear_m2.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    posIntAzAU_Head_appear_m2 = posIntAzHead_appear_m2.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')

    print('AU appearance rate of m2', float(len(azAU_appear_m2)/len(auHeadInterest_dump_m2)))
    print('Head appearance rate of m2', float(len(azHead_appear_m2)/len(auHeadInterest_dump_m2)))
    print('AU_Head appearance rate of m2', float(len(azAU_Head_appear_m2)/len(auHeadInterest_dump_m2)))

    print('Head appearance rate of m2 in positive interest', float(len(posIntAzHead_appear_m2)/len(posInterest_appear_m2)))
    print('AU_Head appearance rate of m2 in positive interest', float(len(posIntAzAU_Head_appear_m2)/len(posInterest_appear_m2)))
    print('Head appearance rate of m2 in negative interest', float(len(negIntAzHead_appear_m2)/len(negInterest_appear_m2)))
    print('AU_Head appearance rate of m2 in negative interest', float(len(negIntAzAU_Head_appear_m2)/len(negInterest_appear_m2)))

    plt.subplot(col, row, 2)#2
    plt.xlabel('time (ms)', fontsize=9)
#    plt.ylabel('Positions')
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level', fontsize=9)

    plt.plot(start_time_m2, au01_array_m2, label='AU01', marker='.')
    plt.plot(start_time_m2, au02_array_m2, label='AU02', marker='.')
    plt.plot(start_time_m2[1:], dif_au01_m2, label='Delta of AU01', marker='.')
    plt.plot(start_time_m2[1:], dif_au02_m2, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_m2, head_vel_max_array_m2, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f2, shoulderRight_vel_max_array_f2, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f2, shoulderLeft_vel_max_array_f2, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au04, label='dif_AU04', marker='.')
#    plt.plot(start_time[1:], dif_au05, label='dif_AU05', marker='.')
#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_m2, e_20m2_int['interest_level'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712M2021', fontsize=9)
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)
    

### M3
    start_time_m3 = d_20m3_dump['end(system)[ms]'].values
    au01_array_m3 = d_20m3_dump['AU01_c_mean'].values
    au02_array_m3 = d_20m3_dump['AU02_c_mean'].values
    head_vel_max_array_m3 = d_20m3_dump['Head_velocity_max'].values
    head_vel_max_array_m3 = head_vel_max_array_m3 * 10
#    shoulderRight_vel_max_array_f3 = d_20f3_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f3 = shoulderRight_vel_max_array_f3 * 10
#    shoulderLeft_vel_max_array_f3 = d_20f3_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f3 = shoulderLeft_vel_max_array_f3 * 10

    dif_au01_m3 = np.diff(au01_array_m3)
    dif_au02_m3 = np.diff(au02_array_m3)
#    dif_au45 = np.diff(au45_array)

    e_20m3_int = e_20m3_int.set_axis(['ID','interest_level'], axis=1)
    auHeadInterest_dump_m3 = pd.concat([d_20m3_dump['end(system)[ms]'],d_20m3_dump['AU01_c_mean'],d_20m3_dump['AU02_c_mean'],d_20m3_dump['Head_velocity_max'],e_20m3_int['interest_level']],axis=1)

    azAU_appear_m3 = auHeadInterest_dump_m3.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_m3 = auHeadInterest_dump_m3.query('Head_velocity_max > 0.075')
    azAU_Head_appear_m3 = azHead_appear_m3.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    negInterest_appear_m3 = auHeadInterest_dump_m3.query('interest_level == -1')
    posInterest_appear_m3 = auHeadInterest_dump_m3.query('interest_level == 1')

    negIntAzHead_appear_m3 = negInterest_appear_m3.query('Head_velocity_max > 0.075')
    posIntAzHead_appear_m3 = posInterest_appear_m3.query('Head_velocity_max > 0.075')

    negIntAzAU_Head_appear_m3 = negIntAzHead_appear_m3.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    posIntAzAU_Head_appear_m3 = posIntAzHead_appear_m3.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')

    print('AU appearance rate of m3', float(len(azAU_appear_m3)/len(auHeadInterest_dump_m3)))
    print('Head appearance rate of m3', float(len(azHead_appear_m3)/len(auHeadInterest_dump_m3)))
    print('AU_Head appearance rate of m3', float(len(azAU_Head_appear_m3)/len(auHeadInterest_dump_m3)))

    print('Head appearance rate of m3 in positive interest', float(len(posIntAzHead_appear_m3)/len(posInterest_appear_m3)))
    print('AU_Head appearance rate of m3 in positive interest', float(len(posIntAzAU_Head_appear_m3)/len(posInterest_appear_m3)))
    print('Head appearance rate of m3 in negative interest', float(len(negIntAzHead_appear_m3)/len(negInterest_appear_m3)))
    print('AU_Head appearance rate of m3 in negative interest', float(len(negIntAzAU_Head_appear_m3)/len(negInterest_appear_m3)))
    
    plt.subplot(col, row, 3)#3
    plt.xlabel('time (ms)', fontsize=9)
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level', fontsize=9)

    plt.plot(start_time_m3, au01_array_m3, label='AU01', marker='.')
    plt.plot(start_time_m3, au02_array_m3, label='AU02', marker='.')
    plt.plot(start_time_m3[1:], dif_au01_m3, label='Delta of AU01', marker='.')
    plt.plot(start_time_m3[1:], dif_au02_m3, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_m3, head_vel_max_array_m3, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f3, shoulderRight_vel_max_array_f3, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f3, shoulderLeft_vel_max_array_f3, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_m3, e_20m3_int['interest_level'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712M2024', fontsize=9)
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

### M4
    start_time_m4 = d_20m4_dump['end(system)[ms]'].values
    au01_array_m4 = d_20m4_dump['AU01_c_mean'].values
    au02_array_m4 = d_20m4_dump['AU02_c_mean'].values
    head_vel_max_array_m4 = d_20m4_dump['Head_velocity_max'].values
    head_vel_max_array_m4 = head_vel_max_array_m4 * 10
#    shoulderRight_vel_max_array_f3 = d_20f3_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f3 = shoulderRight_vel_max_array_f3 * 10
#    shoulderLeft_vel_max_array_f3 = d_20f3_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f3 = shoulderLeft_vel_max_array_f3 * 10

    dif_au01_m4 = np.diff(au01_array_m4)
    dif_au02_m4 = np.diff(au02_array_m4)
#    dif_au45 = np.diff(au45_array)

    e_20m4_int = e_20m4_int.set_axis(['ID','interest_level'], axis=1)
    auHeadInterest_dump_m4 = pd.concat([d_20m4_dump['end(system)[ms]'],d_20m4_dump['AU01_c_mean'],d_20m4_dump['AU02_c_mean'],d_20m4_dump['Head_velocity_max'],e_20m4_int['interest_level']],axis=1)

    azAU_appear_m4 = auHeadInterest_dump_m4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_m4 = auHeadInterest_dump_m4.query('Head_velocity_max > 0.075')
    azAU_Head_appear_m4 = azHead_appear_m4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    negInterest_appear_m4 = auHeadInterest_dump_m4.query('interest_level == -1')
    posInterest_appear_m4 = auHeadInterest_dump_m4.query('interest_level == 1')

    negIntAzHead_appear_m4 = negInterest_appear_m4.query('Head_velocity_max > 0.075')
    posIntAzHead_appear_m4 = posInterest_appear_m4.query('Head_velocity_max > 0.075')

    negIntAzAU_Head_appear_m4 = negIntAzHead_appear_m4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    posIntAzAU_Head_appear_m4 = posIntAzHead_appear_m4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')

    print('AU appearance rate of m4', float(len(azAU_appear_m4)/len(auHeadInterest_dump_m4)))
    print('Head appearance rate of m4', float(len(azHead_appear_m4)/len(auHeadInterest_dump_m4)))
    print('AU_Head appearance rate of m4', float(len(azAU_Head_appear_m4)/len(auHeadInterest_dump_m4)))

    print('Head appearance rate of m4 in positive interest', float(len(posIntAzHead_appear_m4)/len(posInterest_appear_m4)))
    print('AU_Head appearance rate of m4 in positive interest', float(len(posIntAzAU_Head_appear_m4)/len(posInterest_appear_m4)))
    print('Head appearance rate of m4 in negative interest', float(len(negIntAzHead_appear_m4)/len(negInterest_appear_m4)))
    print('AU_Head appearance rate of m4 in negative interest', float(len(negIntAzAU_Head_appear_m4)/len(negInterest_appear_m4)))

    plt.subplot(col, row, 4)#4
    plt.xlabel('time (ms)', fontsize=9)
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level', fontsize=9)

    plt.plot(start_time_m4, au01_array_m4, label='AU01', marker='.')
    plt.plot(start_time_m4, au02_array_m4, label='AU02', marker='.')
    plt.plot(start_time_m4[1:], dif_au01_m4, label='Delta of AU01', marker='.')
    plt.plot(start_time_m4[1:], dif_au02_m4, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_m4, head_vel_max_array_m4, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f3, shoulderRight_vel_max_array_f3, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f3, shoulderLeft_vel_max_array_f3, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_m4, e_20m4_int['interest_level'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712M2028', fontsize=9)
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

### M5
    start_time_m5 = d_20m5_dump['end(system)[ms]'].values
    au01_array_m5 = d_20m5_dump['AU01_c_mean'].values
    au02_array_m5 = d_20m5_dump['AU02_c_mean'].values
    head_vel_max_array_m5 = d_20m5_dump['Head_velocity_max'].values
    head_vel_max_array_m5 = head_vel_max_array_m5 * 10
#    shoulderRight_vel_max_array_f3 = d_20f3_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f3 = shoulderRight_vel_max_array_f3 * 10
#    shoulderLeft_vel_max_array_f3 = d_20f3_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f3 = shoulderLeft_vel_max_array_f3 * 10

    dif_au01_m5 = np.diff(au01_array_m5)
    dif_au02_m5 = np.diff(au02_array_m5)
#    dif_au45 = np.diff(au45_array)

    e_20m5_int = e_20m5_int.set_axis(['ID','interest_level'], axis=1)
    auHeadInterest_dump_m5 = pd.concat([d_20m5_dump['end(system)[ms]'],d_20m5_dump['AU01_c_mean'],d_20m5_dump['AU02_c_mean'],d_20m5_dump['Head_velocity_max'],e_20m5_int['interest_level']],axis=1)

    azAU_appear_m5 = auHeadInterest_dump_m5.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_m5 = auHeadInterest_dump_m5.query('Head_velocity_max > 0.075')
    azAU_Head_appear_m5 = azHead_appear_m1.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    negInterest_appear_m5 = auHeadInterest_dump_m5.query('interest_level == -1')
    posInterest_appear_m5 = auHeadInterest_dump_m5.query('interest_level == 1')

    negIntAzHead_appear_m5 = negInterest_appear_m5.query('Head_velocity_max > 0.075')
    posIntAzHead_appear_m5 = posInterest_appear_m5.query('Head_velocity_max > 0.075')

    negIntAzAU_Head_appear_m5 = negIntAzHead_appear_m5.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    posIntAzAU_Head_appear_m5 = posIntAzHead_appear_m5.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')

    print('AU appearance rate of m5', float(len(azAU_appear_m5)/len(auHeadInterest_dump_m5)))
    print('Head appearance rate of m5', float(len(azHead_appear_m5)/len(auHeadInterest_dump_m5)))
    print('AU_Head appearance rate of m5', float(len(azAU_Head_appear_m5)/len(auHeadInterest_dump_m5)))

    print('Head appearance rate of m5 in positive interest', float(len(posIntAzHead_appear_m5)/len(posInterest_appear_m5)))
    print('AU_Head appearance rate of m5 in positive interest', float(len(posIntAzAU_Head_appear_m5)/len(posInterest_appear_m5)))
    print('Head appearance rate of m5 in negative interest', float(len(negIntAzHead_appear_m5)/len(negInterest_appear_m5)))
    print('AU_Head appearance rate of m5 in negative interest', float(len(negIntAzAU_Head_appear_m5)/len(negInterest_appear_m5)))
    
    plt.subplot(col, row, 5)#4
    plt.xlabel('time (ms)', fontsize=9)
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level', fontsize=9)

    plt.plot(start_time_m5, au01_array_m5, label='AU01', marker='.')
    plt.plot(start_time_m5, au02_array_m5, label='AU02', marker='.')
    plt.plot(start_time_m5[1:], dif_au01_m5, label='Delta of AU01', marker='.')
    plt.plot(start_time_m5[1:], dif_au02_m5, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_m5, head_vel_max_array_m5, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f3, shoulderRight_vel_max_array_f3, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f3, shoulderLeft_vel_max_array_f3, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_m5, e_20m5_int['interest_level'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712M2029', fontsize=9)
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

#    plt.tight_layout()
    plt.show()

    print('Total AU appearance rate', float((len(azAU_appear_m1)+len(azAU_appear_m2)+len(azAU_appear_m3)+len(azAU_appear_m4)+len(azAU_appear_m5))/(len(d_20m1_dump)+len(d_20m2_dump)+len(d_20m3_dump)+len(d_20m4_dump)+len(d_20m5_dump))))
    print('Total Head appearance rate', float((len(azHead_appear_m1)+len(azHead_appear_m2)+len(azHead_appear_m3)+len(azHead_appear_m4)+len(azAU_appear_m5))/(len(d_20m1_dump)+len(d_20m2_dump)+len(d_20m3_dump)+len(d_20m4_dump)+len(d_20m5_dump))))
    print('Total AU_Head appearance rate', float((len(azAU_Head_appear_m1)+len(azAU_Head_appear_m2)+len(azAU_Head_appear_m3)+len(azAU_Head_appear_m4)+len(azAU_appear_m5))/(len(d_20m1_dump)+len(d_20m2_dump)+len(d_20m3_dump)+len(d_20m4_dump)+len(d_20m5_dump))))

    print('Total Head appearance rate in positive interest', float((len(posIntAzHead_appear_m1)+len(posIntAzHead_appear_m2)+len(posIntAzHead_appear_m3)+len(posIntAzHead_appear_m4)+len(posIntAzHead_appear_m5))/(len(posInterest_appear_m1)+len(posInterest_appear_m2)+len(posInterest_appear_m3)+len(posInterest_appear_m4)+len(posInterest_appear_m5))))
    print('Total AU_Head appearance rate in positive interest', float((len(posIntAzAU_Head_appear_m1)+len(posIntAzAU_Head_appear_m2)+len(posIntAzAU_Head_appear_m3)+len(posIntAzAU_Head_appear_m4)+len(posIntAzAU_Head_appear_m5))/(len(posInterest_appear_m1)+len(posInterest_appear_m2)+len(posInterest_appear_m3)+len(posInterest_appear_m4)+len(posIntAzAU_Head_appear_m5))))

    print('Total Head appearance rate in negative interest', float((len(negIntAzHead_appear_m1)+len(negIntAzHead_appear_m2)+len(negIntAzHead_appear_m3)+len(negIntAzHead_appear_m4)+len(negIntAzHead_appear_m5))/(len(negInterest_appear_m1)+len(negInterest_appear_m2)+len(negInterest_appear_m3)+len(negInterest_appear_m4)+len(negIntAzHead_appear_m5))))
    print('Total AU_Head appearance rate in negative interest', float((len(negIntAzAU_Head_appear_m1)+len(negIntAzAU_Head_appear_m2)+len(negIntAzAU_Head_appear_m3)+len(negIntAzAU_Head_appear_m4)+len(negIntAzAU_Head_appear_m5))/(len(negInterest_appear_m1)+len(negInterest_appear_m2)+len(negInterest_appear_m3)+len(negInterest_appear_m4)+len(negInterest_appear_m5))))



if __name__ == '__main__':
    main()