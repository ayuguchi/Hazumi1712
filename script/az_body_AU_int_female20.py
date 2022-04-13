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
col = 2 #3

def main():
    d_20f1_dump = pd.read_csv('../dumpfiles/1712F2006.csv')
    d_20f2_dump = pd.read_csv('../dumpfiles/1712F2010.csv')
    d_20f3_dump = pd.read_csv('../dumpfiles/1712F2018.csv')
    d_20f4_dump = pd.read_csv('../dumpfiles/1712F2019.csv')

    e_20f1_int = pd.read_csv('../script/1712F2006_int_level.csv')
    e_20f2_int = pd.read_csv('../script/1712F2010_int_level.csv')
    e_20f3_int = pd.read_csv('../script/1712F2018_int_level.csv')
    e_20f4_int = pd.read_csv('../script/1712F2019_int_level.csv')

    d_20f1_kinect = pd.read_csv('../kinect/1712F2006/Body/BodyData.csv')
    d_20f2_kinect = pd.read_csv('../kinect/1712F2010/Body/BodyData.csv')
    d_20f3_kinect = pd.read_csv('../kinect/1712F2018/Body/BodyData.csv')
    d_20f4_kinect = pd.read_csv('../kinect/1712F2019/Body/BodyData.csv')

### F1
    start_time_f1 = d_20f1_dump['end(system)[ms]'].values
    au01_array_f1 = d_20f1_dump['AU01_c_mean'].values
    au02_array_f1 = d_20f1_dump['AU02_c_mean'].values
    head_vel_max_array_f1 = d_20f1_dump['Head_velocity_max'].values
    head_vel_max_array_f1 = head_vel_max_array_f1 * 10
#    shoulderRight_vel_max_array_f1 = d_20f1_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f1 = shoulderRight_vel_max_array_f1 * 10
#    shoulderLeft_vel_max_array_f1 = d_20f1_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f1 = shoulderLeft_vel_max_array_f1 * 10

    dif_au01_f1 = np.diff(au01_array_f1)
    dif_au02_f1 = np.diff(au02_array_f1)
#    dif_au45 = np.diff(au45_array)

    azAU_appear_f1 = d_20f1_dump.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_f1 = d_20f1_dump.query('Head_velocity_max > 0.075')
    azAU_Head_appear_f1 = azHead_appear_f1.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    print('AU appearance rate of f1', float(len(azAU_appear_f1)/len(d_20f1_dump)))
    print('Head appearance rate of f1', float(len(azHead_appear_f1)/len(d_20f1_dump)))
    print('AU_Head appearance rate of f1', float(len(azAU_Head_appear_f1)/len(d_20f1_dump)))
    
    plt.subplot(col, row, 1)#1
    plt.xlabel('time (ms)')
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level')

    plt.plot(start_time_f1, au01_array_f1, label='AU01', marker='.')
    plt.plot(start_time_f1, au02_array_f1, label='AU02', marker='.')
    plt.plot(start_time_f1[1:], dif_au01_f1, label='Delta of AU01', marker='.')
    plt.plot(start_time_f1[1:], dif_au02_f1, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_f1, head_vel_max_array_f1, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f3, shoulderRight_vel_max_array_f3, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f3, shoulderLeft_vel_max_array_f3, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_f1, e_20f1_int['0'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712F2006')
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

### F2
    start_time_f2 = d_20f2_dump['end(system)[ms]'].values
    au01_array_f2 = d_20f2_dump['AU01_c_mean'].values
    au02_array_f2 = d_20f2_dump['AU02_c_mean'].values
    head_vel_max_array_f2 = d_20f2_dump['Head_velocity_max'].values
    head_vel_max_array_f2 = head_vel_max_array_f2 * 10
    shoulderRight_vel_max_array_f2 = d_20f2_dump['ShoulderRight_velocity_max'].values
    shoulderRight_vel_max_array_f2 = shoulderRight_vel_max_array_f2 * 10
    shoulderLeft_vel_max_array_f2 = d_20f2_dump['ShoulderLeft_velocity_max'].values
    shoulderLeft_vel_max_array_f2 = shoulderLeft_vel_max_array_f2 * 10

    dif_au01_f2 = np.diff(au01_array_f2)
    dif_au02_f2 = np.diff(au02_array_f2)
#    dif_au45 = np.diff(au45_array)

    azAU_appear_f2 = d_20f2_dump.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_f2 = d_20f2_dump.query('Head_velocity_max > 0.075')
    azAU_Head_appear_f2 = azHead_appear_f2.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    print('AU appearance rate of f2', float(len(azAU_appear_f2)/len(d_20f2_dump)))
    print('Head appearance rate of f2', float(len(azHead_appear_f2)/len(d_20f2_dump)))
    print('AU_Head appearance rate of f2', float(len(azAU_Head_appear_f2)/len(d_20f2_dump)))

    plt.subplot(col, row, 2)#2
    plt.xlabel('time (ms)')
#    plt.ylabel('Positions')
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level')

    plt.plot(start_time_f2, au01_array_f2, label='AU01', marker='.')
    plt.plot(start_time_f2, au02_array_f2, label='AU02', marker='.')
    plt.plot(start_time_f2[1:], dif_au01_f2, label='Delta of AU01', marker='.')
    plt.plot(start_time_f2[1:], dif_au02_f2, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_f2, head_vel_max_array_f2, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f2, shoulderRight_vel_max_array_f2, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f2, shoulderLeft_vel_max_array_f2, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au04, label='dif_AU04', marker='.')
#    plt.plot(start_time[1:], dif_au05, label='dif_AU05', marker='.')
#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_f2, e_20f2_int['0'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712F2010')
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)
    

### F3
    start_time_f3 = d_20f3_dump['end(system)[ms]'].values
    au01_array_f3 = d_20f3_dump['AU01_c_mean'].values
    au02_array_f3 = d_20f3_dump['AU02_c_mean'].values
    head_vel_max_array_f3 = d_20f3_dump['Head_velocity_max'].values
    head_vel_max_array_f3 = head_vel_max_array_f3 * 10
#    shoulderRight_vel_max_array_f3 = d_20f3_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f3 = shoulderRight_vel_max_array_f3 * 10
#    shoulderLeft_vel_max_array_f3 = d_20f3_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f3 = shoulderLeft_vel_max_array_f3 * 10

    dif_au01_f3 = np.diff(au01_array_f3)
    dif_au02_f3 = np.diff(au02_array_f3)
#    dif_au45 = np.diff(au45_array)

    azAU_appear_f3 = d_20f3_dump.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_f3 = d_20f3_dump.query('Head_velocity_max > 0.075')
    azAU_Head_appear_f3 = azHead_appear_f3.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    print('AU appearance rate of f3', float(len(azAU_appear_f3)/len(d_20f3_dump)))
    print('Head appearance rate of f3', float(len(azHead_appear_f3)/len(d_20f3_dump)))
    print('AU_Head appearance rate of f3', float(len(azAU_Head_appear_f3)/len(d_20f3_dump)))
    
    plt.subplot(col, row, 3)#3
    plt.xlabel('time (ms)')
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level')

    plt.plot(start_time_f3, au01_array_f3, label='AU01', marker='.')
    plt.plot(start_time_f3, au02_array_f3, label='AU02', marker='.')
    plt.plot(start_time_f3[1:], dif_au01_f3, label='Delta of AU01', marker='.')
    plt.plot(start_time_f3[1:], dif_au02_f3, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_f3, head_vel_max_array_f3, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f3, shoulderRight_vel_max_array_f3, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f3, shoulderLeft_vel_max_array_f3, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_f3, e_20f3_int['0'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712F2018')
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

### F4
    start_time_f4 = d_20f4_dump['end(system)[ms]'].values
    au01_array_f4 = d_20f4_dump['AU01_c_mean'].values
    au02_array_f4 = d_20f4_dump['AU02_c_mean'].values
    head_vel_max_array_f4 = d_20f4_dump['Head_velocity_max'].values
    head_vel_max_array_f4 = head_vel_max_array_f4 * 10
#    shoulderRight_vel_max_array_f3 = d_20f3_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f3 = shoulderRight_vel_max_array_f3 * 10
#    shoulderLeft_vel_max_array_f3 = d_20f3_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f3 = shoulderLeft_vel_max_array_f3 * 10

    dif_au01_f4 = np.diff(au01_array_f4)
    dif_au02_f4 = np.diff(au02_array_f4)
#    dif_au45 = np.diff(au45_array)

    azAU_appear_f4 = d_20f4_dump.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    azHead_appear_f4 = d_20f4_dump.query('Head_velocity_max > 0.075')
    azAU_Head_appear_f4 = azHead_appear_f4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
    print('AU appearance rate of f4', float(len(azAU_appear_f4)/len(d_20f4_dump)))
    print('Head appearance rate of f4', float(len(azHead_appear_f4)/len(d_20f4_dump)))
    print('AU_Head appearance rate of f4', float(len(azAU_Head_appear_f4)/len(d_20f4_dump)))
    
    plt.subplot(col, row, 4)#4
    plt.xlabel('time (ms)')
    plt.ylabel('AUs | Velocity (10*cm/s) | Interest Level')

    plt.plot(start_time_f4, au01_array_f4, label='AU01', marker='.')
    plt.plot(start_time_f4, au02_array_f4, label='AU02', marker='.')
    plt.plot(start_time_f4[1:], dif_au01_f4, label='Delta of AU01', marker='.')
    plt.plot(start_time_f4[1:], dif_au02_f4, label='Delta of AU02', marker='.')

#    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
    plt.plot(start_time_f4, head_vel_max_array_f4, label='Max of Head Velocity', marker='.')
#    plt.plot(start_time_f3, shoulderRight_vel_max_array_f3, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
#    plt.plot(start_time_f3, shoulderLeft_vel_max_array_f3, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time_f4, e_20f4_int['0'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712F2019')
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

    plt.tight_layout()
    plt.show()

    print('Total AU appearance rate', float((len(azAU_appear_f1)+len(azAU_appear_f2)+len(azAU_appear_f3)+len(azAU_appear_f4))/(len(d_20f1_dump)+len(d_20f2_dump)+len(d_20f3_dump)+len(d_20f4_dump))))
    print('Total Head appearance rate of f4', float((len(azHead_appear_f1)+len(azHead_appear_f2)+len(azHead_appear_f3)+len(azHead_appear_f4))/(len(d_20f1_dump)+len(d_20f2_dump)+len(d_20f3_dump)+len(d_20f4_dump))))
    print('Total AU_Head appearance rate of f4', float((len(azAU_Head_appear_f1)+len(azAU_Head_appear_f2)+len(azAU_Head_appear_f3)+len(azAU_Head_appear_f4))/(len(d_20f1_dump)+len(d_20f2_dump)+len(d_20f3_dump)+len(d_20f4_dump))))


if __name__ == '__main__':
    main()