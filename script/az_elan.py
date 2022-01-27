# -*- encoding: UTF-8 -*-
from cProfile import label
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
#    f_20f1 = open('../dumpfiles/1712F2006.csv')
    ef1 = pd.read_csv('../elan/1712F2006.csv')
    ef1_index = ef1.set_index('sys_utterance')
    ef1_int = ef1_index['Int_HRI-i':'Int_TOH']
#    print(ef1_int) 

    ef1_int_A = ef1_index.loc['Int_HRI-i', :]
    ef1_int_B = ef1_index.loc['Int_HRI-n', :]
    ef1_int_C = ef1_index.loc['Int_KIT', :]
    ef1_int_D = ef1_index.loc['Int_OSA-k', :]
    ef1_int_E = ef1_index.loc['Int_OSA-n', :]
    ef1_int_G = ef1_index.loc['Int_TOH', :]
#    print(ef1_int_A)
#    print(ef1_int_B)
#    print(ef1_int_B)
#    print(ef1_int_C)
#    print(ef1_int_D)
#    print(ef1_int_E)

    ef1_int_A = pd.DataFrame(ef1_int_A)
    ef1_int_A_ant = ef1_int_A[['165.0',' これから「ドラマ」の話をしましょう！']]
    ef1_int_B = pd.DataFrame(ef1_int_B)
    ef1_int_B_ant = ef1_int_B[['165.0',' これから「ドラマ」の話をしましょう！']]
    ef1_int_C = pd.DataFrame(ef1_int_C)
    ef1_int_C_ant = ef1_int_C[['165.0',' これから「ドラマ」の話をしましょう！']]
    ef1_int_D = pd.DataFrame(ef1_int_D)
    ef1_int_D_ant = ef1_int_D[['165.0',' これから「ドラマ」の話をしましょう！']]
    ef1_int_E = pd.DataFrame(ef1_int_E)
    ef1_int_E_ant = ef1_int_E[['165.0',' これから「ドラマ」の話をしましょう！']]
    ef1_int_G = pd.DataFrame(ef1_int_G)
    ef1_int_G_ant = ef1_int_G[['165.0',' これから「ドラマ」の話をしましょう！']]

#    print(ef1_int_A.join(ef1_int_B, lsuffix='_HRI-i', rsuffix='_HRI-n'))
    ef1_int_ant = ef1_int_A_ant.merge(ef1_int_B_ant, how='left', on='165.0', suffixes=('_HRI-i', '_HRI-n'))
    ef1_int_ant = ef1_int_ant.merge(ef1_int_C_ant, how='left', on='165.0', suffixes=('_HRI-i', '_HRI-n'))
    ef1_int_ant = ef1_int_ant.merge(ef1_int_D_ant, how='left', on='165.0', suffixes=('_KIT', '_OSA-k'))
    ef1_int_ant = ef1_int_ant.merge(ef1_int_E_ant, how='left', on='165.0')
    ef1_int_ant = ef1_int_ant.merge(ef1_int_G_ant, how='left', on='165.0', suffixes=('_OSA-n', '_TOH'))
    print(ef1_int_ant)

    
    '''
    for d_row in d_f_20f4:
        start_time.append(float(d_row[1]))
        au01.append(float(d_row[1420]))
        au02.append(float(d_row[1421]))
        au04.append(float(d_row[1422]))
        au05.append(float(d_row[1423]))
        au45.append(float(d_row[1437]))

    au01_array = np.array(au01)
    au02_array = np.array(au02)
    au04_array = np.array(au04)
    au05_array = np.array(au05)
    au45_array = np.array(au45)

    dif_au01 = np.diff(au01_array)
    dif_au02 = np.diff(au02_array)
    dif_au04 = np.diff(au04_array)
    dif_au05 = np.diff(au05_array)
    dif_au45 = np.diff(au45_array)
    
    plt.subplot(col, row, 4)
    plt.xlabel('time')
    plt.ylabel('Action Units')

#    plt.plot(start_time, au01, label='AU01', marker='.')
#    plt.plot(start_time, au02, label='AU02', marker='.')
#    plt.plot(start_time, au04, label='AU04', marker='.')
#    plt.plot(start_time, au05, label='AU05', marker='.')
#    plt.plot(start_time, au45, label='AU45', marker='.')

    plt.plot(start_time[1:], dif_au01, label='dif_AU01', marker='.')
    plt.plot(start_time[1:], dif_au02, label='dif_AU02', marker='.')
    plt.plot(start_time[1:], dif_au04, label='dif_AU04', marker='.')
    plt.plot(start_time[1:], dif_au05, label='dif_AU05', marker='.')
    plt.plot(start_time[1:], dif_au45, label='dif_AU45', marker='.')

    plt.title('1712F2019')
    plt.ylim(-0.9,0.9)
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

if __name__ == '__main__':
    main()