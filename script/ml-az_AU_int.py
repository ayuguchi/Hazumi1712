# -*- encoding: UTF-8 -*-
#! python3
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
#import seaborn as sns

#start_time = []
#au01 = []
#au02 = []
#au04 = []
#au05 = []
#au45 = []

def main():
    d_20f1_dump = pd.read_csv('../dumpfiles/1712F2006.csv')
    d_20f2_dump = pd.read_csv('../dumpfiles/1712F2010.csv')
    d_20f3_dump = pd.read_csv('../dumpfiles/1712F2018.csv')
    d_20f4_dump = pd.read_csv('../dumpfiles/1712F2019.csv')

    d_30f1_dump = pd.read_csv('../dumpfiles/1712F3013.csv')
    d_30f2_dump = pd.read_csv('../dumpfiles/1712F3016.csv')
    d_30f3_dump = pd.read_csv('../dumpfiles/1712F3030.csv')

    d_40f1_dump = pd.read_csv('../dumpfiles/1712F4011.csv')
    d_40f2_dump = pd.read_csv('../dumpfiles/1712F4012.csv')
    d_40f3_dump = pd.read_csv('../dumpfiles/1712F4017.csv')
    d_40f4_dump = pd.read_csv('../dumpfiles/1712F4027.csv')

    d_50f1_dump = pd.read_csv('../dumpfiles/1712F5008.csv')
    d_50f2_dump = pd.read_csv('../dumpfiles/1712F5014.csv')
    d_50f3_dump = pd.read_csv('../dumpfiles/1712F5026.csv')

    d_20m1_dump = pd.read_csv('../dumpfiles/1712M2007.csv')
    d_20m2_dump = pd.read_csv('../dumpfiles/1712M2021.csv')
    d_20m3_dump = pd.read_csv('../dumpfiles/1712M2024.csv')
    d_20m4_dump = pd.read_csv('../dumpfiles/1712M2028.csv')
    d_20m5_dump = pd.read_csv('../dumpfiles/1712M2029.csv')

    d_30m1_dump = pd.read_csv('../dumpfiles/1712M3001.csv')
    d_30m2_dump = pd.read_csv('../dumpfiles/1712M3005.csv')
    d_30m3_dump = pd.read_csv('../dumpfiles/1712M3009.csv')

    d_40m1_dump = pd.read_csv('../dumpfiles/1712M4004.csv')
    d_40m2_dump = pd.read_csv('../dumpfiles/1712M4015.csv')
    d_40m3_dump = pd.read_csv('../dumpfiles/1712M4020.csv')
    d_40m4_dump = pd.read_csv('../dumpfiles/1712M4022.csv')
    d_40m5_dump = pd.read_csv('../dumpfiles/1712M4025.csv')

#    e_20f1_int = pd.read_csv('../script/1712F2006_int_level.csv')
#    e_20f2_int = pd.read_csv('../script/1712F2010_int_level.csv')
#    e_20f3_int = pd.read_csv('../script/1712F2018_int_level.csv')
#    e_20f4_int = pd.read_csv('../script/1712F2019_int_level.csv')

    data_num = ['20f1','20f2','20f3','20f4','30f1','30f2','30f3','40f1','40f2','40f3','40f4','50f1','50f2','50f3','20m1','20m2','20m3','20m4','20m5','30m1','30m2','30m3','40m1','40m2','40m3','40m4','40m5',]

#    for n in data_num:
    au01_array_ = d_20f1_dump['AU01_c_mean'].values
    au02_array_20f1 = d_20f1_dump['AU02_c_mean'].values
    au04_array_20f1 = d_20f1_dump['AU04_c_mean'].values
    au05_array_20f1 = d_20f1_dump['AU05_c_mean'].values
    au06_array_20f1 = d_20f1_dump['AU06_c_mean'].values
    au07_array_f1 = d_20f1_dump['AU07_c_mean'].values
    au09_array_f1 = d_20f1_dump['AU09_c_mean'].values
    au10_array_f1 = d_20f1_dump['AU10_c_mean'].values
    au12_array_f1 = d_20f1_dump['AU12_c_mean'].values
    au14_array_f1 = d_20f1_dump['AU14_c_mean'].values
    au15_array_f1 = d_20f1_dump['AU15_c_mean'].values
    au17_array_f1 = d_20f1_dump['AU17_c_mean'].values
    au20_array_f1 = d_20f1_dump['AU20_c_mean'].values
    au23_array_f1 = d_20f1_dump['AU23_c_mean'].values
    au25_array_f1 = d_20f1_dump['AU25_c_mean'].values
    au26_array_f1 = d_20f1_dump['AU26_c_mean'].values
    au28_array_f1 = d_20f1_dump['AU28_c_mean'].values
    au45_array_f1 = d_20f1_dump['AU45_c_mean'].values

'''
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

#    e_20f4_int = e_20f4_int.set_axis(['ID','interest_level'], axis=1)
#    auHeadInterest_dump_f4 = pd.concat([d_20f4_dump['end(system)[ms]'],d_20f4_dump['AU01_c_mean'],d_20f4_dump['AU02_c_mean'],d_20f4_dump['Head_velocity_max'],e_20f4_int['interest_level']],axis=1)

#    azAU_appear_f4 = auHeadInterest_dump_f4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
#    azHead_appear_f4 = auHeadInterest_dump_f4.query('Head_velocity_max > 0.075')
#    azAU_Head_appear_f4 = azHead_appear_f4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
#    negInterest_appear_f4 = auHeadInterest_dump_f4.query('interest_level == -1')
#    posInterest_appear_f4 = auHeadInterest_dump_f4.query('interest_level == 1')

#    negIntAzHead_appear_f4 = negInterest_appear_f4.query('Head_velocity_max > 0.075')
#    posIntAzHead_appear_f4 = posInterest_appear_f4.query('Head_velocity_max > 0.075')

#    negIntAzAU_Head_appear_f4 = negIntAzHead_appear_f4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')
#    posIntAzAU_Head_appear_f4 = posIntAzHead_appear_f4.query('AU01_c_mean >= 0.5 | AU02_c_mean >= 0.5')

#    print('AU appearance rate of f4', float(len(azAU_appear_f4)/len(auHeadInterest_dump_f4)))
#    print('Head appearance rate of f4', float(len(azHead_appear_f4)/len(auHeadInterest_dump_f4)))
#    print('AU_Head appearance rate of f4', float(len(azAU_Head_appear_f4)/len(auHeadInterest_dump_f4)))

#    print('Head appearance rate of f4 in positive interest', float(len(posIntAzHead_appear_f4)/len(posInterest_appear_f4)))
#    print('AU_Head appearance rate of f4 in positive interest', float(len(posIntAzAU_Head_appear_f4)/len(posInterest_appear_f4)))
#    print('Head appearance rate of f4 in negative interest', float(len(negIntAzHead_appear_f4)/len(negInterest_appear_f4)))
#    print('AU_Head appearance rate of f4 in negative interest', float(len(negIntAzAU_Head_appear_f4)/len(negInterest_appear_f4)))
#    plt.subplot(col, row, 4)#4
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
    plt.plot(start_time_f4, e_20f4_int['interest_level'], label='Interest Level', marker='.', color='grey', linestyle = "--")

    plt.title('1712F2019')
    plt.ylim(-1.2,4.0)
#    plt.xlim(100000, 1200000)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

#    plt.tight_layout()
    plt.show()

#    print('Total AU appearance rate', float((len(azAU_appear_f1)+len(azAU_appear_f2)+len(azAU_appear_f3)+len(azAU_appear_f4))/(len(d_20f1_dump)+len(d_20f2_dump)+len(d_20f3_dump)+len(d_20f4_dump))))
#    print('Total Head appearance rate', float((len(azHead_appear_f1)+len(azHead_appear_f2)+len(azHead_appear_f3)+len(azHead_appear_f4))/(len(d_20f1_dump)+len(d_20f2_dump)+len(d_20f3_dump)+len(d_20f4_dump))))
#    print('Total AU_Head appearance rate', float((len(azAU_Head_appear_f1)+len(azAU_Head_appear_f2)+len(azAU_Head_appear_f3)+len(azAU_Head_appear_f4))/(len(d_20f1_dump)+len(d_20f2_dump)+len(d_20f3_dump)+len(d_20f4_dump))))

#    print('Total Head appearance rate in positive interest', float((len(posIntAzHead_appear_f1)+len(posIntAzHead_appear_f2)+len(posIntAzHead_appear_f3)+len(posIntAzHead_appear_f4))/(len(posInterest_appear_f1)+len(posInterest_appear_f2)+len(posInterest_appear_f3)+len(posInterest_appear_f4))))
#    print('Total AU_Head appearance rate in positive interest', float((len(posIntAzAU_Head_appear_f1)+len(posIntAzAU_Head_appear_f2)+len(posIntAzAU_Head_appear_f3)+len(posIntAzAU_Head_appear_f4))/(len(posInterest_appear_f1)+len(posInterest_appear_f2)+len(posInterest_appear_f3)+len(posInterest_appear_f4))))

#    print('Total Head appearance rate in negative interest', float((len(negIntAzHead_appear_f1)+len(negIntAzHead_appear_f2)+len(negIntAzHead_appear_f3)+len(negIntAzHead_appear_f4))/(len(negInterest_appear_f1)+len(negInterest_appear_f2)+len(negInterest_appear_f3)+len(negInterest_appear_f4))))
#    print('Total AU_Head appearance rate in negative interest', float((len(negIntAzAU_Head_appear_f1)+len(negIntAzAU_Head_appear_f2)+len(negIntAzAU_Head_appear_f3)+len(negIntAzAU_Head_appear_f4))/(len(negInterest_appear_f1)+len(negInterest_appear_f2)+len(negInterest_appear_f3)+len(negInterest_appear_f4))))
'''


if __name__ == '__main__':
    main()