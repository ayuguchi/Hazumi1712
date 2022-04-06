# -*- encoding: UTF-8 -*-
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation
#import seaborn as sns

#start_time = []
au01 = []
au02 = []
au04 = []
au05 = []
au45 = []

row = 1 #2
col = 2 #3

def main():
#    f_20f1 = open('../dumpfiles/1712F2006.csv')
#    d_f_20f1 = csv.reader(f_20f1)
#    label_d_f_20f1 = next(d_f_20f1)
#    f_20f2 = open('../dumpfiles/1712F2010.csv')
#    d_f_20f2 = csv.reader(f_20f2)
#    label_d_f_20f2 = next(d_f_20f2)
#    f_20f3 = open('../dumpfiles/1712F2018.csv')
#    d_f_20f3 = csv.reader(f_20f3)
#    label_d_f_20f3 = next(d_f_20f3)
#    f_20f4 = open('../dumpfiles/1712F2019.csv')
#    d_f_20f4 = csv.reader(f_20f4)
#    label_d_f_20f4 = next(d_f_20f4)

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

    '''
    for d_row in d_f_20f1:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
#        au04.append(float(d_row[1422]))
#        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))

    au01_array = np.array(au01)
    au02_array = np.array(au02)
#    au04_array = np.array(au04)
#    au05_array = np.array(au05)
    au45_array = np.array(au45)

    dif_au01 = np.diff(au01_array)
    dif_au02 = np.diff(au02_array)
#    dif_au04 = np.diff(au04_array)
#    dif_au05 = np.diff(au05_array)
    dif_au45 = np.diff(au45_array)
#    print(len(au45_array))
#    print(dif_au45)
#    print(len(dif_au45))

    plt.subplot(col, row, 1)
    plt.xlabel('time (ms)')
    plt.ylabel('Action Units | Interest Level')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
#    plt.plot(start_time, au04, label='AU04', marker='.')
#    plt.plot(start_time, au05, label='AU05', marker='.')
#    plt.plot(start_time, au45, label='AU45', marker='.')

    print(len(start_time[1:]))

    plt.plot(start_time[1:], dif_au01, label='dif_AU01', marker='.')
    plt.plot(start_time[1:], dif_au02, label='dif_AU02', marker='.')
#    plt.plot(start_time[1:], dif_au04, label='dif_AU04', marker='.')
#    plt.plot(start_time[1:], dif_au05, label='dif_AU05', marker='.')
#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time[0:], e_20f1_int['0'], label='interest_level', marker='.', color='grey')

    plt.title('1712F2006')
    plt.ylim(-1.2,1.2)
    plt.grid()
#    plt.legend()
    plt.legend(loc='best', borderaxespad=0)


    start_time.clear()
    au01.clear()
    au02.clear()
#    au04.clear()
#    au05.clear()
    au45.clear()
    '''

### F2
#    start_time_f2 = d_20f2_dump['end(system)[ms]'].values
#    au01_array_f2 = d_20f2_dump['AU01_c_mean'].values
#    au02_array_f2 = d_20f2_dump['AU02_c_mean'].values
#    head_vel_max_array_f2 = d_20f2_dump['Head_velocity_max'].values
#    head_vel_max_array_f2 = head_vel_max_array_f2 * 10
#    shoulderRight_vel_max_array_f2 = d_20f2_dump['ShoulderRight_velocity_max'].values
#    shoulderRight_vel_max_array_f2 = shoulderRight_vel_max_array_f2 * 10
#    shoulderLeft_vel_max_array_f2 = d_20f2_dump['ShoulderLeft_velocity_max'].values
#    shoulderLeft_vel_max_array_f2 = shoulderLeft_vel_max_array_f2 * 10

#    head_pos_x_array_f2 = d_20f2_kinect['Head_X'].values
#    head_pos_y_array_f2 = d_20f2_kinect['Head_Y'].values
#    head_pos_z_array_f2 = d_20f2_kinect['Head_Z'].values

    head_pos_array_f2 = d_20f2_kinect[['Head_X', 'Head_Y', 'Head_Z']].values
#    print(head_pos_array_f2)

#    neck_pos_x_array_f2 = d_20f2_kinect['Neck_X'].values
#    neck_pos_y_array_f2 = d_20f2_kinect['Neck_Y'].values
#    neck_pos_z_array_f2 = d_20f2_kinect['Neck_Z'].values

    neck_pos_array_f2 = d_20f2_kinect[['Neck_X', 'Neck_Y', 'Neck_Z']].values
#    print(neck_pos_array_f2)

    head_vec_array_f2 = head_pos_array_f2 - neck_pos_array_f2
    print(head_vec_array_f2)


#    dif_au01_f2 = np.diff(au01_array_f2)
#    dif_au02_f2 = np.diff(au02_array_f2)
#    dif_au45 = np.diff(au45_array)

    plt.subplot(col, row, 1)#2
    plt.xlabel('time (ms)')
    plt.ylabel('Positions')
#    plt.ylabel('Action Units | Velocity (10*cm/s)')

#    plt.plot(start_time_f2, au01_array_f2, label='AU01', marker='.')
#    plt.plot(start_time_f2, au02_array_f2, label='AU02', marker='.')
#    plt.plot(start_time_f2[1:], dif_au01_f2, label='Delta of AU01', marker='.')
#    plt.plot(start_time_f2[1:], dif_au02_f2, label='Delta of AU02', marker='.')

##    plt.plot(d_20f2_dump['end(system)[ms]'], d_20f2_dump['Head_velocity_mean'], label='Mean of Head Velocity', marker='.')
#    plt.plot(start_time_f2, head_vel_max_array_f2, label='Max of Head Velocity', marker='.')
##    plt.plot(start_time_f2, shoulderRight_vel_max_array_f2, label='Max of Sholder Right Velocity', marker='.', linestyle = "dashed")
##    plt.plot(start_time_f2, shoulderLeft_vel_max_array_f2, label='Max of Sholder Left Velocity', marker='.', linestyle = "dashed")

    plt.plot(d_20f2_kinect['SysTime'], d_20f2_kinect['Head_X'], label='Head_X', marker='.')
    plt.plot(d_20f2_kinect['SysTime'], d_20f2_kinect['Head_Y'], label='Head_Y', marker='.')
    plt.plot(d_20f2_kinect['SysTime'], d_20f2_kinect['Head_Z'], label='Head_Y', marker='.')

    plt.plot(d_20f2_kinect['SysTime'], d_20f2_kinect['Neck_X'], label='Head_X', marker='.')
    plt.plot(d_20f2_kinect['SysTime'], d_20f2_kinect['Neck_Y'], label='Head_Y', marker='.')
    plt.plot(d_20f2_kinect['SysTime'], d_20f2_kinect['Neck_Z'], label='Head_Y', marker='.')

#    plt.plot(start_time[1:], dif_au04, label='dif_AU04', marker='.')
#    plt.plot(start_time[1:], dif_au05, label='dif_AU05', marker='.')
#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
#    plt.plot(start_time_f2, e_20f2_int['0'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712F2010')
#    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)
    

### F3
    start_time_f3 = d_20f3_dump['end(system)[ms]'].values
    au01_array_f3 = d_20f3_dump['AU01_c_mean'].values
    au02_array_f3 = d_20f3_dump['AU02_c_mean'].values
    head_vel_max_array_f3 = d_20f3_dump['Head_velocity_max'].values
    head_vel_max_array_f3 = head_vel_max_array_f3 * 10
    shoulderRight_vel_max_array_f3 = d_20f3_dump['ShoulderRight_velocity_max'].values
    shoulderRight_vel_max_array_f3 = shoulderRight_vel_max_array_f3 * 10
    shoulderLeft_vel_max_array_f3 = d_20f3_dump['ShoulderLeft_velocity_max'].values
    shoulderLeft_vel_max_array_f3 = shoulderLeft_vel_max_array_f3 * 10

    dif_au01_f3 = np.diff(au01_array_f3)
    dif_au02_f3 = np.diff(au02_array_f3)
#    dif_au45 = np.diff(au45_array)
    
    plt.subplot(col, row, 2)#3
    plt.xlabel('time (ms)')
    plt.ylabel('Action Units | Velocity (10*cm/s)')

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

    '''
    for d_row in d_f_20f4:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
#        au04.append(float(d_row[1422]))
#        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))

    au01_array = np.array(au01)
    au02_array = np.array(au02)
#    au04_array = np.array(au04)
#    au05_array = np.array(au05)
    au45_array = np.array(au45)

    dif_au01 = np.diff(au01_array)
    dif_au02 = np.diff(au02_array)
#    dif_au04 = np.diff(au04_array)
#    dif_au05 = np.diff(au05_array)
    dif_au45 = np.diff(au45_array)
    
    plt.subplot(col, row, 4)
    plt.xlabel('time (ms)')
    plt.ylabel('Action Units | Interest Level')

    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
#    plt.plot(start_time, au45, label='AU45', marker='.')

    plt.plot(start_time[1:], dif_au01, label='dif_AU01', marker='.')
    plt.plot(start_time[1:], dif_au02, label='dif_AU02', marker='.')
#    plt.plot(start_time[1:], dif_au04, label='dif_AU04', marker='.')
#    plt.plot(start_time[1:], dif_au05, label='dif_AU05', marker='.')
#    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')
    plt.plot(start_time[0:], e_20f4_int['0'], label='interest_level', marker='.', color='grey')

    plt.title('1712F2019')
    plt.ylim(-1.2,1.2)
    plt.grid()
    plt.legend(loc='upper right', borderaxespad=0)

    start_time.clear()
    au01.clear()
    au02.clear()
#    au04.clear()
#    au05.clear()
    au45.clear()
    '''
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()