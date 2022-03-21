# -*- encoding: UTF-8 -*-
from cProfile import label
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

start_time = []
au01 = []
au02 = []
au04 = []
au05 = []
au45 = []

row = 2 #2
col = 3 #3

def main():
    f_20f1 = open('../dumpfiles/1712F2006.csv')
    d_f_20f1 = csv.reader(f_20f1)
    label_d_f_20f1 = next(d_f_20f1)
    f_20f2 = open('../dumpfiles/1712F2010.csv')
    d_f_20f2 = csv.reader(f_20f2)
    label_d_f_20f2 = next(d_f_20f2)
    f_20f3 = open('../dumpfiles/1712F2018.csv')
    d_f_20f3 = csv.reader(f_20f3)
    label_d_f_20f3 = next(d_f_20f3)
    f_20f4 = open('../dumpfiles/1712F2019.csv')
    d_f_20f4 = csv.reader(f_20f4)
    label_d_f_20f4 = next(d_f_20f4)

    f_20m1 = open('../dumpfiles/1712M2007.csv')
    d_f_20m1 = csv.reader(f_20m1)
    label_d_f_20m1 = next(d_f_20m1)
    f_20m2 = open('../dumpfiles/1712M2021.csv')
    d_f_20m2 = csv.reader(f_20m2)
    label_d_f_20m2 = next(d_f_20m2)
    f_20m3 = open('../dumpfiles/1712M2024.csv')
    d_f_20m3 = csv.reader(f_20m3)
    label_d_f_20m3 = next(d_f_20m3)
    f_20m4 = open('../dumpfiles/1712M2028.csv')
    d_f_20m4 = csv.reader(f_20m4)
    label_d_f_20m4 = next(d_f_20m4)
    f_20m5 = open('../dumpfiles/1712M2029.csv')
    d_f_20m5 = csv.reader(f_20m5)
    label_d_f_20m5 = next(d_f_20m5)

#    f_20f2_dataFrame = pd.read_csv('../dumpfiles/1712F2010.csv')

    e_20f1_int = pd.read_csv('../script/1712F2006_int_level.csv')
    e_20f2_int = pd.read_csv('../script/1712F2010_int_level.csv')
    e_20f3_int = pd.read_csv('../script/1712F2018_int_level.csv')
    e_20f4_int = pd.read_csv('../script/1712F2019_int_level.csv')
    e_20m1_int = pd.read_csv('../script/1712M2007_int_level.csv')
    e_20m2_int = pd.read_csv('../script/1712M2021_int_level.csv')
    e_20m3_int = pd.read_csv('../script/1712M2024_int_level.csv')
    e_20m4_int = pd.read_csv('../script/1712M2028_int_level.csv')
    e_20m5_int = pd.read_csv('../script/1712M2029_int_level.csv')
#    print(type(e_20m1_int))
#    print(e_20m1_int['0'])
#    list_e_20m1_int = e_20m1_int['0'].to_list()
#    print(len(list_e_20m1_int))


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

    startTime_DataFrame= pd.DataFrame(start_time)
    au01_DataFrame= pd.DataFrame(au01)
    au02_DataFrame= pd.DataFrame(au02)

    auInterest_DataFrame = pd.concat([startTime_DataFrame,au01_DataFrame,au02_DataFrame,e_20f1_int['0']],axis=1)
    auInterest_DataFrame = auInterest_DataFrame.set_axis(['start_time','AU01','AU02','interest_level'], axis=1)
    print(auInterest_DataFrame)

    negInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1')
    azAuInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1 & AU01 >= 0.5 | AU02 >= 0.5')

#    print(len(negInterest_DataFrame))
#    print(len(azAuInterest_DataFrame))
    print('Appearance rate of f1', float(len(azAuInterest_DataFrame)/len(negInterest_DataFrame)))
    
#    print(len(azAuInterest_DataFrame))
    plt.subplot(col, row, 1)
    plt.xlabel('time (ms)')
    plt.ylabel('Action Units | Interest Level')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
#    plt.plot(start_time, au04, label='AU04', marker='.')
#    plt.plot(start_time, au05, label='AU05', marker='.')
#    plt.plot(start_time, au45, label='AU45', marker='.')

#    print(len(start_time[1:]))

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

    startTime_DataFrame.drop(startTime_DataFrame.index, inplace=True)
    au01_DataFrame.drop(au01_DataFrame.index, inplace=True)
    au02_DataFrame.drop(au02_DataFrame.index, inplace=True)
    auInterest_DataFrame.drop(auInterest_DataFrame.index, inplace=True)
    negInterest_DataFrame.drop(negInterest_DataFrame.index, inplace=True)
    azAuInterest_DataFrame.drop(azAuInterest_DataFrame.index, inplace=True)

    for d_row in d_f_20f2:
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

#    print(e_20f2_int['0']

    startTime_DataFrame= pd.DataFrame(start_time)
    au01_DataFrame= pd.DataFrame(au01)
    au02_DataFrame= pd.DataFrame(au02)

    auInterest_DataFrame = pd.concat([startTime_DataFrame,au01_DataFrame,au02_DataFrame,e_20f2_int['0']],axis=1)
    auInterest_DataFrame = auInterest_DataFrame.set_axis(['start_time','AU01','AU02','interest_level'], axis=1)
    print(auInterest_DataFrame)

    negInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1')
    azAuInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1 & AU01 >= 0.5 | AU02 >= 0.5')

#    print(len(negInterest_DataFrame))
#    print(len(azAuInterest_DataFrame))
    print('Appearance rate of f2', float(len(azAuInterest_DataFrame)/len(negInterest_DataFrame)))
    
    #Plot
    plt.subplot(col, row, 2)#2
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
    plt.plot(start_time[0:], e_20f2_int['0'], label='interest_level', marker='.', color='grey')

#    plt.title('1712F2010')
    plt.ylim(-1.2,1.2)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)
    
    start_time.clear()
    au01.clear()
    au02.clear()
#    au04.clear()
#    au05.clear()
    au45.clear()

    startTime_DataFrame.drop(startTime_DataFrame.index, inplace=True)
    au01_DataFrame.drop(au01_DataFrame.index, inplace=True)
    au02_DataFrame.drop(au02_DataFrame.index, inplace=True)
    auInterest_DataFrame.drop(auInterest_DataFrame.index, inplace=True)
    negInterest_DataFrame.drop(negInterest_DataFrame.index, inplace=True)
    azAuInterest_DataFrame.drop(azAuInterest_DataFrame.index, inplace=True)


    for d_row in d_f_20f3:
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

    startTime_DataFrame= pd.DataFrame(start_time)
    au01_DataFrame= pd.DataFrame(au01)
    au02_DataFrame= pd.DataFrame(au02)

    auInterest_DataFrame = pd.concat([startTime_DataFrame,au01_DataFrame,au02_DataFrame,e_20f3_int['0']],axis=1)
    auInterest_DataFrame = auInterest_DataFrame.set_axis(['start_time','AU01','AU02','interest_level'], axis=1)
    print(auInterest_DataFrame)

    negInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1')
    azAuInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1 & AU01 >= 0.5 | AU02 >= 0.5')

#    print(len(negInterest_DataFrame))
#    print(len(azAuInterest_DataFrame))
    print('Appearance rate of f3', float(len(azAuInterest_DataFrame)/len(negInterest_DataFrame)))
    
    
    plt.subplot(col, row, 3)#3
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
    plt.plot(start_time[0:], e_20f3_int['0'], label='interest_level', marker='.', color='grey')

#    plt.title('1712F2018')
    plt.ylim(-1.2,1.2)
    plt.grid()
    plt.legend(loc='upper left', borderaxespad=0)

    start_time.clear()
    au01.clear()
    au02.clear()
#    au04.clear()
#    au05.clear()
    au45.clear()

    startTime_DataFrame.drop(startTime_DataFrame.index, inplace=True)
    au01_DataFrame.drop(au01_DataFrame.index, inplace=True)
    au02_DataFrame.drop(au02_DataFrame.index, inplace=True)
    auInterest_DataFrame.drop(auInterest_DataFrame.index, inplace=True)
    negInterest_DataFrame.drop(negInterest_DataFrame.index, inplace=True)
    azAuInterest_DataFrame.drop(azAuInterest_DataFrame.index, inplace=True)


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

    startTime_DataFrame= pd.DataFrame(start_time)
    au01_DataFrame= pd.DataFrame(au01)
    au02_DataFrame= pd.DataFrame(au02)

    auInterest_DataFrame = pd.concat([startTime_DataFrame,au01_DataFrame,au02_DataFrame,e_20f4_int['0']],axis=1)
    auInterest_DataFrame = auInterest_DataFrame.set_axis(['start_time','AU01','AU02','interest_level'], axis=1)
    print(auInterest_DataFrame)

    negInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1')
    azAuInterest_DataFrame = auInterest_DataFrame.query('interest_level == -1 & AU01 >= 0.5 | AU02 >= 0.5')

#    print(len(negInterest_DataFrame))
#    print(len(azAuInterest_DataFrame))
    print('Appearance rate of f4', float(len(azAuInterest_DataFrame)/len(negInterest_DataFrame)))
    
    
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

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
