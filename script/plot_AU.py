# -*- encoding: UTF-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import csv

start_time = []
au01 = []
au02 = []
au04 = []
au05 = []
au45 = []

def main():
    f = open('../dumpfiles/1712F2006.csv')
    data = csv.reader(f)
    label_data = next(data)
#    print(type(data))
    for row in data:
        print(row)
#        start = float(row[1])
        start_time.append(float(row[1]))
        au01.append(float(row[1420]))
        au02.append(float(row[1421]))
        au04.append(float(row[1422]))
        au05.append(float(row[1423]))
        au45.append(float(row[1437]))
    
    plt.xlabel('time')
    plt.ylabel('Action Units')

    plt.plot(start_time, au01, label='AU01')
    plt.plot(start_time, au02, label='AU02')
    plt.plot(start_time, au04, label='AU04')
    plt.plot(start_time, au05, label='AU05')
    plt.plot(start_time, au45, label='AU45')
    plt.grid()
    plt.show()

    f.close()

if __name__ == '__main__':
    main()