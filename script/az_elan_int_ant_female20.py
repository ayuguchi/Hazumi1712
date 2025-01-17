# -*- encoding: UTF-8 -*-
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

row = 2
col = 3

def main():
#    f_20f1 = open('../dumpfiles/1712F2006.csv')
    ef1 = pd.read_csv('../elan/1712F2006.csv')
    ef1_index = ef1.set_index('sys_utterance')
    ef1_int = ef1_index['Int_HRI-i':'Int_TOH']

    ef2 = pd.read_csv('../elan/1712F2010.csv')
    ef2_index = ef2.set_index('sys_utterance')
    ef2_int = ef2_index['Int_HRI-i':'Int_TOT']

    ef3 = pd.read_csv('../elan/1712F2018.csv')
    ef3_index = ef3.set_index('sys_utterance')
    ef3_int = ef3_index['Int_HRI-i':'Int_JAI']

    ef4 = pd.read_csv('../elan/1712F2019.csv')
    ef4_index = ef4.set_index('sys_utterance')
    ef4_int = ef4_index['Int_HRI-i':'Int_TOH']
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

    ef1_int_ant_bool_o = (ef1_int_ant == "o")
    ef1_int_ant_bool_x = (ef1_int_ant == "x")

    print('O Numbers of ef1:\n', ef1_int_ant_bool_o.sum(axis='columns'))
    print('X Numbers of ef1:\n', ef1_int_ant_bool_x.sum(axis='columns'))

    ef1_int_ant_bool_o_num = ef1_int_ant_bool_o.sum(axis='columns')
    ef1_int_ant_bool_x_num = ef1_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef1_int_ant_bool_num = pd.concat([ef1_int_ant_bool_o_num, ef1_int_ant_bool_x_num], axis='columns') 
#    print(ef1_int_ant_bool_num)
#    print( ef1_int_ant_bool_num[0] > ef1_int_ant_bool_num[1])
    print(ef1_int_ant_bool_o_num > ef1_int_ant_bool_x_num)
    ef1_int_ant_bool = ef1_int_ant_bool_o_num > ef1_int_ant_bool_x_num

    ef1_int_ant_score = ef1_int_ant_bool.mask(ef1_int_ant_bool==True, 1)
    ef1_int_ant_score = ef1_int_ant_score.mask(ef1_int_ant_bool==False, -1)
    print(ef1_int_ant_score)
    ef1_int_ant_score.to_csv('./1712F2006_int_level.csv')

    plt.subplot(col, row, 1)
    plt.plot(ef1_int_ant_score, marker='.')

    plt.title('1712F2006')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()


    ef2_int_A = ef2_index.loc['Int_HRI-i', :]
    ef2_int_B = ef2_index.loc['Int_HRI-n', :]
    ef2_int_C = ef2_index.loc['Int_TOT', :]
    
    ef2_int_A = pd.DataFrame(ef2_int_A)
    ef2_int_A_ant = ef2_int_A[['143.0',' これから「ゲーム」について話しましょう']]
    ef2_int_B = pd.DataFrame(ef2_int_B)
    ef2_int_B_ant = ef2_int_B[['143.0',' これから「ゲーム」について話しましょう']]
    ef2_int_C = pd.DataFrame(ef2_int_C)
    ef2_int_C_ant = ef2_int_C[['143.0',' これから「ゲーム」について話しましょう']]

    ef2_int_ant = ef2_int_A_ant.merge(ef2_int_B_ant, how='left', on='143.0', suffixes=('_HRI-i', '_HRI-n'))
    ef2_int_ant = ef2_int_ant.merge(ef2_int_C_ant, how='left', on='143.0', suffixes=('_HRI-i', '_HRI-n'))
    print(ef2_int_ant)

    ef2_int_ant_bool_o = (ef2_int_ant == "o")
    ef2_int_ant_bool_x = (ef2_int_ant == "x")

#    print('O Numbers of ef2:\n', ef2_int_ant_bool_o.sum(axis='columns'))
#    print('X Numbers of ef2:\n', ef2_int_ant_bool_x.sum(axis='columns'))

    ef2_int_ant_bool_o_num = ef2_int_ant_bool_o.sum(axis='columns')
    ef2_int_ant_bool_x_num = ef2_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef2_int_ant_bool_num = pd.concat([ef2_int_ant_bool_o_num, ef2_int_ant_bool_x_num], axis='columns')
#    print(ef2_int_ant_bool_num)
    print(ef2_int_ant_bool_o_num > ef2_int_ant_bool_x_num)
    ef2_int_ant_bool = ef2_int_ant_bool_o_num > ef2_int_ant_bool_x_num

    ef2_int_ant_score = ef2_int_ant_bool.mask(ef2_int_ant_bool==True, 1)
    ef2_int_ant_score = ef2_int_ant_score.mask(ef2_int_ant_bool==False, -1)
    print(ef2_int_ant_score)
    ef2_int_ant_score.to_csv('./1712F2010_int_level.csv')

    plt.subplot(col, row, 2)
    plt.plot(ef2_int_ant_score, marker='.')

    plt.title('1712F2010')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()


    ef3_int_A = ef3_index.loc['Int_HRI-i', :]
    ef3_int_B = ef3_index.loc['Int_HRI-n', :]
    ef3_int_C = ef3_index.loc['Int_JAI', :]
    
    ef3_int_A = pd.DataFrame(ef3_int_A)
    ef3_int_A_ant = ef3_int_A[['136.0',' これから「アニメ・漫画」について話しましょう！']]
    ef3_int_B = pd.DataFrame(ef3_int_B)
    ef3_int_B_ant = ef3_int_B[['136.0',' これから「アニメ・漫画」について話しましょう！']]
    ef3_int_C = pd.DataFrame(ef3_int_C)
    ef3_int_C_ant = ef3_int_C[['136.0',' これから「アニメ・漫画」について話しましょう！']]

    ef3_int_ant = ef3_int_A_ant.merge(ef3_int_B_ant, how='left', on='136.0', suffixes=('_HRI-i', '_HRI-n'))
    ef3_int_ant = ef3_int_ant.merge(ef3_int_C_ant, how='left', on='136.0', suffixes=('_HRI-i', '_HRI-n'))
    print(ef3_int_ant)

    ef3_int_ant_bool_o = (ef3_int_ant == "o")
    ef3_int_ant_bool_x = (ef3_int_ant == "x")

#    print('O Numbers of ef3:\n', ef3_int_ant_bool_o.sum(axis='columns'))
#    print('X Numbers of ef3:\n', ef3_int_ant_bool_x.sum(axis='columns'))

    ef3_int_ant_bool_o_num = ef3_int_ant_bool_o.sum(axis='columns')
    ef3_int_ant_bool_x_num = ef3_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef3_int_ant_bool_num = pd.concat([ef3_int_ant_bool_o_num, ef3_int_ant_bool_x_num], axis='columns')
#    print(ef3_int_ant_bool_num)

    print(ef3_int_ant_bool_o_num > ef3_int_ant_bool_x_num)
    ef3_int_ant_bool = ef3_int_ant_bool_o_num > ef3_int_ant_bool_x_num

    ef3_int_ant_score = ef3_int_ant_bool.mask(ef3_int_ant_bool==True, 1)
    ef3_int_ant_score = ef3_int_ant_score.mask(ef3_int_ant_bool==False, -1)
    print(ef3_int_ant_score)
    ef3_int_ant_score.to_csv('./1712F2018_int_level.csv')

    plt.subplot(col, row, 3)
    plt.plot(ef3_int_ant_score, marker='.')

    plt.title('1712F2018')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()


    ef4_int_A = ef4_index.loc['Int_HRI-i', :]
    ef4_int_B = ef4_index.loc['Int_HRI-n', :]
    ef4_int_C = ef4_index.loc['Int_KIT', :]
    ef4_int_D = ef4_index.loc['Int_OSA-k', :]
    ef4_int_E = ef4_index.loc['Int_OSA-n', :]
    ef4_int_G = ef4_index.loc['Int_TOH', :]

    ef4_int_A = pd.DataFrame(ef4_int_A)
    ef4_int_A_ant = ef4_int_A[['150.0',' これから「アニメ・漫画」について話しましょう！']]
    ef4_int_B = pd.DataFrame(ef4_int_B)
    ef4_int_B_ant = ef4_int_B[['150.0',' これから「アニメ・漫画」について話しましょう！']]
    ef4_int_C = pd.DataFrame(ef4_int_C)
    ef4_int_C_ant = ef4_int_C[['150.0',' これから「アニメ・漫画」について話しましょう！']]
    ef4_int_D = pd.DataFrame(ef4_int_D)
    ef4_int_D_ant = ef4_int_D[['150.0',' これから「アニメ・漫画」について話しましょう！']]
    ef4_int_E = pd.DataFrame(ef4_int_E)
    ef4_int_E_ant = ef4_int_E[['150.0',' これから「アニメ・漫画」について話しましょう！']]
    ef4_int_G = pd.DataFrame(ef4_int_G)
    ef4_int_G_ant = ef4_int_G[['150.0',' これから「アニメ・漫画」について話しましょう！']]

    ef4_int_ant = ef4_int_A_ant.merge(ef4_int_B_ant, how='left', on='150.0', suffixes=('_HRI-i', '_HRI-n'))
    ef4_int_ant = ef4_int_ant.merge(ef4_int_C_ant, how='left', on='150.0', suffixes=('_HRI-i', '_HRI-n'))
    ef4_int_ant = ef4_int_ant.merge(ef4_int_D_ant, how='left', on='150.0', suffixes=('_KIT', '_OSA-k'))
    ef4_int_ant = ef4_int_ant.merge(ef4_int_E_ant, how='left', on='150.0')
    ef4_int_ant = ef4_int_ant.merge(ef4_int_G_ant, how='left', on='150.0', suffixes=('_OSA-n', '_TOH'))
    print(ef4_int_ant)

    ef4_int_ant_bool_o = (ef4_int_ant == "o")
    ef4_int_ant_bool_x = (ef4_int_ant == "x")

#    print('O Numbers of ef4:\n', ef4_int_ant_bool_o.sum(axis='columns'))
#    print('X Numbers of ef4:\n', ef4_int_ant_bool_x.sum(axis='columns'))

    ef4_int_ant_bool_o_num = ef4_int_ant_bool_o.sum(axis='columns')
    ef4_int_ant_bool_x_num = ef4_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef4_int_ant_bool_num = pd.concat([ef4_int_ant_bool_o_num, ef4_int_ant_bool_x_num], axis='columns')
#    print(ef4_int_ant_bool_num)

    print(ef4_int_ant_bool_o_num > ef4_int_ant_bool_x_num)
    ef4_int_ant_bool = ef4_int_ant_bool_o_num > ef4_int_ant_bool_x_num

    ef4_int_ant_score = ef4_int_ant_bool.mask(ef4_int_ant_bool==True, 1)
    ef4_int_ant_score = ef4_int_ant_score.mask(ef4_int_ant_bool==False, -1)
    print(ef4_int_ant_score)
    ef4_int_ant_score.to_csv('./1712F2019_int_level.csv')

    plt.subplot(col, row, 4)
    plt.plot(ef3_int_ant_score, marker='.')

    plt.title('1712F2019')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()