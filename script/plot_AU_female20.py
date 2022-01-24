# -*- encoding: UTF-8 -*-
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

start_time = []
au01 = []
au02 = []
au04 = []
au05 = []
au45 = []

row = 2
col = 3

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

    for d_row in d_f_20f1:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))

    plt.subplot(col, row, 1)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712F2006')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()
#    plt.show()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()


    for d_row in d_f_20f2:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 2)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712F2010')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()


    for d_row in d_f_20f3:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 3)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712F2018')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()


    for d_row in d_f_20f4:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 4)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712F2019')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()

    plt.tight_layout()
    plt.show()
'''
    for d_row in d_f_20m1:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 5)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712M2007')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()

    for d_row in d_f_20m2:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 6)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712M2021')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()

    for d_row in d_f_20m3:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 7)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712F2024')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()

    for d_row in d_f_20m4:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 8)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712M2028')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()

    for d_row in d_f_20m5:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))
    
    plt.subplot(col, row, 9)
    plt.xlabel('time')
    plt.ylabel('Action Units')
    plt.plot(start_time, au01, label='AU01', marker='.')
    plt.plot(start_time, au02, label='AU02', marker='.')
    plt.plot(start_time, au04, label='AU04', marker='.')
    plt.plot(start_time, au05, label='AU05', marker='.')
    plt.plot(start_time, au45, label='AU45', marker='.')
    plt.title('1712M2029')
    plt.ylim(0.0,1.0)
    plt.grid()
    plt.legend()

    start_time.clear()
    au01.clear()
    au02.clear()
    au04.clear()
    au05.clear()
    au45.clear()
'''

if __name__ == '__main__':
    main()