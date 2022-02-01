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
    em1 = pd.read_csv('../elan/1712M2007.csv')
    em1_index = em1.set_index('sys_utterance')
    em1_int = em1_index['Int_HRI-i':'Int_TOH']

    em2 = pd.read_csv('../elan/1712M2021.csv')
    em2_index = em2.set_index('sys_utterance')
    em2_int = em2_index['Int_HRI-i':'Int_TOT']

    em3 = pd.read_csv('../elan/1712M2024.csv')
    em3_index = em3.set_index('sys_utterance')
    em3_int = em3_index['Int_HRI-i':'Int_JAI']

    em4 = pd.read_csv('../elan/1712M2028.csv')
    em4_index = em4.set_index('sys_utterance')
    em4_int = em4_index['Int_HRI-i':'Int_TOH']

    em5 = pd.read_csv('../elan/1712M2029.csv')
    em5_index = em5.set_index('sys_utterance')
    em5_int = em5_index['Int_HRI-i':'Int_TOT']

    em1_int_A = em1_index.loc['Int_HRI-i', :]
    em1_int_B = em1_index.loc['Int_HRI-n', :]
    em1_int_C = em1_index.loc['Int_KIT', :]
    em1_int_D = em1_index.loc['Int_OSA-k', :]
    em1_int_E = em1_index.loc['Int_OSA-n', :]
    em1_int_G = em1_index.loc['Int_TOH', :]
#    print(ef1_int_A)
#    print(ef1_int_B)
#    print(ef1_int_B)
#    print(ef1_int_C)
#    print(ef1_int_D)
#    print(ef1_int_E)

    em1_int_A = pd.DataFrame(em1_int_A)
    em1_int_A_ant = em1_int_A[['230.0',' これから「食べ物」について話しましょう！']]
    em1_int_B = pd.DataFrame(em1_int_B)
    em1_int_B_ant = em1_int_B[['230.0',' これから「食べ物」について話しましょう！']]
    em1_int_C = pd.DataFrame(em1_int_C)
    em1_int_C_ant = em1_int_C[['230.0',' これから「食べ物」について話しましょう！']]
    em1_int_D = pd.DataFrame(em1_int_D)
    em1_int_D_ant = em1_int_D[['230.0',' これから「食べ物」について話しましょう！']]
    em1_int_E = pd.DataFrame(em1_int_E)
    em1_int_E_ant = em1_int_E[['230.0',' これから「食べ物」について話しましょう！']]
    em1_int_G = pd.DataFrame(em1_int_G)
    em1_int_G_ant = em1_int_G[['230.0',' これから「食べ物」について話しましょう！']]

#    print(ef1_int_A.join(ef1_int_B, lsuffix='_HRI-i', rsuffix='_HRI-n'))
    em1_int_ant = em1_int_A_ant.merge(em1_int_B_ant, how='left', on='230.0', suffixes=('_HRI-i', '_HRI-n'))
    em1_int_ant = em1_int_ant.merge(em1_int_C_ant, how='left', on='230.0', suffixes=('_HRI-i', '_HRI-n'))
    em1_int_ant = em1_int_ant.merge(em1_int_D_ant, how='left', on='230.0', suffixes=('_KIT', '_OSA-k'))
    em1_int_ant = em1_int_ant.merge(em1_int_E_ant, how='left', on='230.0')
    em1_int_ant = em1_int_ant.merge(em1_int_G_ant, how='left', on='230.0', suffixes=('_OSA-n', '_TOH'))
    print(em1_int_ant)

    em1_int_ant_bool_o = (em1_int_ant == "o")
    em1_int_ant_bool_x = (em1_int_ant == "x")

    print('O Numbers of ef1:\n', em1_int_ant_bool_o.sum(axis='columns'))
    print('X Numbers of ef1:\n', em1_int_ant_bool_x.sum(axis='columns'))

    em1_int_ant_bool_o_num = em1_int_ant_bool_o.sum(axis='columns')
    em1_int_ant_bool_x_num = em1_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef1_int_ant_bool_num = pd.concat([ef1_int_ant_bool_o_num, ef1_int_ant_bool_x_num], axis='columns') 
#    print(ef1_int_ant_bool_num)
#    print( ef1_int_ant_bool_num[0] > ef1_int_ant_bool_num[1])
    print(em1_int_ant_bool_o_num > em1_int_ant_bool_x_num)
    em1_int_ant_bool = em1_int_ant_bool_o_num > em1_int_ant_bool_x_num

    em1_int_ant_score = em1_int_ant_bool.mask(em1_int_ant_bool==True, 1)
    em1_int_ant_score = em1_int_ant_score.mask(em1_int_ant_bool==False, -1)
    print(em1_int_ant_score)
    em1_int_ant_score.to_csv('./1712M2007_int_level.csv')

    plt.subplot(col, row, 1)
    plt.plot(em1_int_ant_score, marker='.')

    plt.title('1712M2007')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()


    em2_int_A = em2_index.loc['Int_HRI-i', :]
    em2_int_B = em2_index.loc['Int_HRI-n', :]
    em2_int_C = em2_index.loc['Int_TOT', :]
    
    em2_int_A = pd.DataFrame(em2_int_A)
    em2_int_A_ant = em2_int_A[['160.0',' これから「ゲーム」について話しましょう']]
    em2_int_B = pd.DataFrame(em2_int_B)
    em2_int_B_ant = em2_int_B[['160.0',' これから「ゲーム」について話しましょう']]
    em2_int_C = pd.DataFrame(em2_int_C)
    em2_int_C_ant = em2_int_C[['160.0',' これから「ゲーム」について話しましょう']]

    em2_int_ant = em2_int_A_ant.merge(em2_int_B_ant, how='left', on='160.0', suffixes=('_HRI-i', '_HRI-n'))
    em2_int_ant = em2_int_ant.merge(em2_int_C_ant, how='left', on='160.0', suffixes=('_HRI-i', '_HRI-n'))
    print(em2_int_ant)

    em2_int_ant_bool_o = (em2_int_ant == "o")
    em2_int_ant_bool_x = (em2_int_ant == "x")

#    print('O Numbers of ef2:\n', ef2_int_ant_bool_o.sum(axis='columns'))
#    print('X Numbers of ef2:\n', ef2_int_ant_bool_x.sum(axis='columns'))

    em2_int_ant_bool_o_num = em2_int_ant_bool_o.sum(axis='columns')
    em2_int_ant_bool_x_num = em2_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef2_int_ant_bool_num = pd.concat([ef2_int_ant_bool_o_num, ef2_int_ant_bool_x_num], axis='columns')
#    print(ef2_int_ant_bool_num)
    print(em2_int_ant_bool_o_num > em2_int_ant_bool_x_num)
    em2_int_ant_bool = em2_int_ant_bool_o_num > em2_int_ant_bool_x_num

    em2_int_ant_score = em2_int_ant_bool.mask(em2_int_ant_bool==True, 1)
    em2_int_ant_score = em2_int_ant_score.mask(em2_int_ant_bool==False, -1)
    print(em2_int_ant_score)
    em2_int_ant_score.to_csv('./1712M2021_int_level.csv')

    plt.subplot(col, row, 2)
    plt.plot(em2_int_ant_score, marker='.')

    plt.title('1712M2021')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()


    em3_int_A = em3_index.loc['Int_HRI-i', :]
    em3_int_B = em3_index.loc['Int_HRI-n', :]
    em3_int_C = em3_index.loc['Int_JAI', :]
    
    em3_int_A = pd.DataFrame(em3_int_A)
    em3_int_A_ant = em3_int_A[['155.0',' これから「アニメ・漫画」について話しましょう！']]
    em3_int_B = pd.DataFrame(em3_int_B)
    em3_int_B_ant = em3_int_B[['155.0',' これから「アニメ・漫画」について話しましょう！']]
    em3_int_C = pd.DataFrame(em3_int_C)
    em3_int_C_ant = em3_int_C[['155.0',' これから「アニメ・漫画」について話しましょう！']]

    em3_int_ant = em3_int_A_ant.merge(em3_int_B_ant, how='left', on='155.0', suffixes=('_HRI-i', '_HRI-n'))
    em3_int_ant = em3_int_ant.merge(em3_int_C_ant, how='left', on='155.0', suffixes=('_HRI-i', '_HRI-n'))
    print(em3_int_ant)

    em3_int_ant_bool_o = (em3_int_ant == "o")
    em3_int_ant_bool_x = (em3_int_ant == "x")

#    print('O Numbers of ef3:\n', ef3_int_ant_bool_o.sum(axis='columns'))
#    print('X Numbers of ef3:\n', ef3_int_ant_bool_x.sum(axis='columns'))

    em3_int_ant_bool_o_num = em3_int_ant_bool_o.sum(axis='columns')
    em3_int_ant_bool_x_num = em3_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef3_int_ant_bool_num = pd.concat([ef3_int_ant_bool_o_num, ef3_int_ant_bool_x_num], axis='columns')
#    print(ef3_int_ant_bool_num)

    print(em3_int_ant_bool_o_num > em3_int_ant_bool_x_num)
    em3_int_ant_bool = em3_int_ant_bool_o_num > em3_int_ant_bool_x_num

    em3_int_ant_score = em3_int_ant_bool.mask(em3_int_ant_bool==True, 1)
    em3_int_ant_score = em3_int_ant_score.mask(em3_int_ant_bool==False, -1)
    print(em3_int_ant_score)
    em3_int_ant_score.to_csv('./1712M2024_int_level.csv')

    plt.subplot(col, row, 3)
    plt.plot(em3_int_ant_score, marker='.')

    plt.title('1712M2024')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()


    em4_int_A = em4_index.loc['Int_HRI-i', :]
    em4_int_B = em4_index.loc['Int_HRI-n', :]
    em4_int_C = em4_index.loc['Int_KIT', :]
    em4_int_D = em4_index.loc['Int_OSA-k', :]
    em4_int_E = em4_index.loc['Int_OSA-n', :]
    em4_int_G = em4_index.loc['Int_TOH', :]

    em4_int_A = pd.DataFrame(em4_int_A)
    em4_int_A_ant = em4_int_A[['135.0',' これから「ゲーム」について話しましょう']]
    em4_int_B = pd.DataFrame(em4_int_B)
    em4_int_B_ant = em4_int_B[['135.0',' これから「ゲーム」について話しましょう']]
    em4_int_C = pd.DataFrame(em4_int_C)
    em4_int_C_ant = em4_int_C[['135.0',' これから「ゲーム」について話しましょう']]
    em4_int_D = pd.DataFrame(em4_int_D)
    em4_int_D_ant = em4_int_D[['135.0',' これから「ゲーム」について話しましょう']]
    em4_int_E = pd.DataFrame(em4_int_E)
    em4_int_E_ant = em4_int_E[['135.0',' これから「ゲーム」について話しましょう']]
    em4_int_G = pd.DataFrame(em4_int_G)
    em4_int_G_ant = em4_int_G[['135.0',' これから「ゲーム」について話しましょう']]

    em4_int_ant = em4_int_A_ant.merge(em4_int_B_ant, how='left', on='135.0', suffixes=('_HRI-i', '_HRI-n'))
    em4_int_ant = em4_int_ant.merge(em4_int_C_ant, how='left', on='135.0', suffixes=('_HRI-i', '_HRI-n'))
    em4_int_ant = em4_int_ant.merge(em4_int_D_ant, how='left', on='135.0', suffixes=('_KIT', '_OSA-k'))
    em4_int_ant = em4_int_ant.merge(em4_int_E_ant, how='left', on='135.0')
    em4_int_ant = em4_int_ant.merge(em4_int_G_ant, how='left', on='135.0', suffixes=('_OSA-n', '_TOH'))
    print(em4_int_ant)

    em4_int_ant_bool_o = (em4_int_ant == "o")
    em4_int_ant_bool_x = (em4_int_ant == "x")

#    print('O Numbers of ef4:\n', ef4_int_ant_bool_o.sum(axis='columns'))
#    print('X Numbers of ef4:\n', ef4_int_ant_bool_x.sum(axis='columns'))

    em4_int_ant_bool_o_num = em4_int_ant_bool_o.sum(axis='columns')
    em4_int_ant_bool_x_num = em4_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef4_int_ant_bool_num = pd.concat([ef4_int_ant_bool_o_num, ef4_int_ant_bool_x_num], axis='columns')
#    print(ef4_int_ant_bool_num)

    print(em4_int_ant_bool_o_num > em4_int_ant_bool_x_num)
    em4_int_ant_bool = em4_int_ant_bool_o_num > em4_int_ant_bool_x_num

    em4_int_ant_score = em4_int_ant_bool.mask(em4_int_ant_bool==True, 1)
    em4_int_ant_score = em4_int_ant_score.mask(em4_int_ant_bool==False, -1)
    print(em4_int_ant_score)
    em4_int_ant_score.to_csv('./1712M2028_int_level.csv')

    plt.subplot(col, row, 4)
    plt.plot(em3_int_ant_score, marker='.')

    plt.title('1712M2028')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
#    plt.legend()


    em5_int_A = em5_index.loc['Int_HRI-i', :]
    em5_int_B = em5_index.loc['Int_HRI-n', :]
    em5_int_C = em5_index.loc['Int_TOT', :]
    
    em5_int_A = pd.DataFrame(em5_int_A)
    em5_int_A_ant = em5_int_A[['170.0',' これから「アニメ・漫画」について話しましょう！']]
    em5_int_B = pd.DataFrame(em5_int_B)
    em5_int_B_ant = em5_int_B[['170.0',' これから「アニメ・漫画」について話しましょう！']]
    em5_int_C = pd.DataFrame(em5_int_C)
    em5_int_C_ant = em5_int_C[['170.0',' これから「アニメ・漫画」について話しましょう！']]

    em5_int_ant = em5_int_A_ant.merge(em5_int_B_ant, how='left', on='170.0', suffixes=('_HRI-i', '_HRI-n'))
    em5_int_ant = em5_int_ant.merge(em5_int_C_ant, how='left', on='170.0', suffixes=('_HRI-i', '_HRI-n'))
    print(em5_int_ant)

    em5_int_ant_bool_o = (em5_int_ant == "o")
    em5_int_ant_bool_x = (em5_int_ant == "x")

#    print('O Numbers of ef2:\n', ef2_int_ant_bool_o.sum(axis='columns'))
#    print('X Numbers of ef2:\n', ef2_int_ant_bool_x.sum(axis='columns'))

    em5_int_ant_bool_o_num = em5_int_ant_bool_o.sum(axis='columns')
    em5_int_ant_bool_x_num = em5_int_ant_bool_x.sum(axis='columns')
#    print(type(ef1_int_ant_bool_o_num))
#    ef2_int_ant_bool_num = pd.concat([ef2_int_ant_bool_o_num, ef2_int_ant_bool_x_num], axis='columns')
#    print(ef2_int_ant_bool_num)
    print(em5_int_ant_bool_o_num > em5_int_ant_bool_x_num)
    em5_int_ant_bool = em5_int_ant_bool_o_num > em5_int_ant_bool_x_num

    em5_int_ant_score = em5_int_ant_bool.mask(em5_int_ant_bool==True, 1)
    em5_int_ant_score = em5_int_ant_score.mask(em5_int_ant_bool==False, -1)
    print(em5_int_ant_score)
    em5_int_ant_score.to_csv('./1712M2029_int_level.csv')

    plt.subplot(col, row, 5)
    plt.plot(em5_int_ant_score, marker='.')

    plt.title('1712M2029')
    plt.ylabel('Interest Level')
    plt.ylim(-1.2, 1.2)
#    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()