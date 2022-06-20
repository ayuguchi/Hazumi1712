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

#    data_num = ['20f1','20f2','20f3','20f4','30f1','30f2','30f3','40f1','40f2','40f3','40f4','50f1','50f2','50f3','20m1','20m2','20m3','20m4','20m5','30m1','30m2','30m3','40m1','40m2','40m3','40m4','40m5',]

    au_array_20f1 = pd.concat([d_20f1_dump['AU01_c_mean'], d_20f1_dump['AU02_c_mean'], d_20f1_dump['AU04_c_mean'], d_20f1_dump['AU05_c_mean'], d_20f1_dump['AU06_c_mean'], d_20f1_dump['AU07_c_mean'], d_20f1_dump['AU09_c_mean'], d_20f1_dump['AU10_c_mean'], d_20f1_dump['AU12_c_mean'], d_20f1_dump['AU14_c_mean'], d_20f1_dump['AU15_c_mean'], d_20f1_dump['AU17_c_mean'], d_20f1_dump['AU20_c_mean'], d_20f1_dump['AU23_c_mean'], d_20f1_dump['AU25_c_mean'], d_20f1_dump['AU26_c_mean'], d_20f1_dump['AU28_c_mean'], d_20f1_dump['AU45_c_mean']], axis=1)

    au_array_20f2 = pd.concat([d_20f2_dump['AU01_c_mean'], d_20f2_dump['AU02_c_mean'], d_20f2_dump['AU04_c_mean'], d_20f2_dump['AU05_c_mean'], d_20f2_dump['AU06_c_mean'], d_20f2_dump['AU07_c_mean'], d_20f2_dump['AU09_c_mean'], d_20f2_dump['AU10_c_mean'], d_20f2_dump['AU12_c_mean'], d_20f2_dump['AU14_c_mean'], d_20f2_dump['AU15_c_mean'], d_20f2_dump['AU17_c_mean'], d_20f2_dump['AU20_c_mean'], d_20f2_dump['AU23_c_mean'], d_20f2_dump['AU25_c_mean'], d_20f2_dump['AU26_c_mean'], d_20f2_dump['AU28_c_mean'], d_20f2_dump['AU45_c_mean']], axis=1)

    au_array_20f3 = pd.concat([d_20f3_dump['AU01_c_mean'], d_20f3_dump['AU02_c_mean'], d_20f3_dump['AU04_c_mean'], d_20f3_dump['AU05_c_mean'], d_20f3_dump['AU06_c_mean'], d_20f3_dump['AU07_c_mean'], d_20f3_dump['AU09_c_mean'], d_20f3_dump['AU10_c_mean'], d_20f3_dump['AU12_c_mean'], d_20f3_dump['AU14_c_mean'], d_20f3_dump['AU15_c_mean'], d_20f3_dump['AU17_c_mean'], d_20f3_dump['AU20_c_mean'], d_20f3_dump['AU23_c_mean'], d_20f3_dump['AU25_c_mean'], d_20f3_dump['AU26_c_mean'], d_20f3_dump['AU28_c_mean'], d_20f3_dump['AU45_c_mean']], axis=1)

    au_array_20f4 = pd.concat([d_20f4_dump['AU01_c_mean'], d_20f4_dump['AU02_c_mean'], d_20f4_dump['AU04_c_mean'], d_20f4_dump['AU05_c_mean'], d_20f4_dump['AU06_c_mean'], d_20f4_dump['AU07_c_mean'], d_20f4_dump['AU09_c_mean'], d_20f4_dump['AU10_c_mean'], d_20f4_dump['AU12_c_mean'], d_20f4_dump['AU14_c_mean'], d_20f4_dump['AU15_c_mean'], d_20f4_dump['AU17_c_mean'], d_20f4_dump['AU20_c_mean'], d_20f4_dump['AU23_c_mean'], d_20f4_dump['AU25_c_mean'], d_20f4_dump['AU26_c_mean'], d_20f4_dump['AU28_c_mean'], d_20f4_dump['AU45_c_mean']], axis=1)


    au_array_30f1 = pd.concat([d_30f1_dump['AU01_c_mean'], d_30f1_dump['AU02_c_mean'], d_30f1_dump['AU04_c_mean'], d_30f1_dump['AU05_c_mean'], d_30f1_dump['AU06_c_mean'], d_30f1_dump['AU07_c_mean'], d_30f1_dump['AU09_c_mean'], d_30f1_dump['AU10_c_mean'], d_30f1_dump['AU12_c_mean'], d_30f1_dump['AU14_c_mean'], d_30f1_dump['AU15_c_mean'], d_30f1_dump['AU17_c_mean'], d_30f1_dump['AU20_c_mean'], d_30f1_dump['AU23_c_mean'], d_30f1_dump['AU25_c_mean'], d_30f1_dump['AU26_c_mean'], d_30f1_dump['AU28_c_mean'], d_30f1_dump['AU45_c_mean']], axis=1)

    au_array_30f2 = pd.concat([d_30f2_dump['AU01_c_mean'], d_30f2_dump['AU02_c_mean'], d_30f2_dump['AU04_c_mean'], d_30f2_dump['AU05_c_mean'], d_30f2_dump['AU06_c_mean'], d_30f2_dump['AU07_c_mean'], d_30f2_dump['AU09_c_mean'], d_30f2_dump['AU10_c_mean'], d_30f2_dump['AU12_c_mean'], d_30f2_dump['AU14_c_mean'], d_30f2_dump['AU15_c_mean'], d_30f2_dump['AU17_c_mean'], d_30f2_dump['AU20_c_mean'], d_30f2_dump['AU23_c_mean'], d_30f2_dump['AU25_c_mean'], d_30f2_dump['AU26_c_mean'], d_30f2_dump['AU28_c_mean'], d_30f2_dump['AU45_c_mean']], axis=1)

    au_array_30f3 = pd.concat([d_30f3_dump['AU01_c_mean'], d_30f3_dump['AU02_c_mean'], d_30f3_dump['AU04_c_mean'], d_30f3_dump['AU05_c_mean'], d_30f3_dump['AU06_c_mean'], d_30f3_dump['AU07_c_mean'], d_30f3_dump['AU09_c_mean'], d_30f3_dump['AU10_c_mean'], d_30f3_dump['AU12_c_mean'], d_30f3_dump['AU14_c_mean'], d_30f3_dump['AU15_c_mean'], d_30f3_dump['AU17_c_mean'], d_30f3_dump['AU20_c_mean'], d_30f3_dump['AU23_c_mean'], d_30f3_dump['AU25_c_mean'], d_30f3_dump['AU26_c_mean'], d_30f3_dump['AU28_c_mean'], d_30f3_dump['AU45_c_mean']], axis=1)


    au_array_40f1 = pd.concat([d_40f1_dump['AU01_c_mean'], d_40f1_dump['AU02_c_mean'], d_40f1_dump['AU04_c_mean'], d_40f1_dump['AU05_c_mean'], d_40f1_dump['AU06_c_mean'], d_40f1_dump['AU07_c_mean'], d_40f1_dump['AU09_c_mean'], d_40f1_dump['AU10_c_mean'], d_40f1_dump['AU12_c_mean'], d_40f1_dump['AU14_c_mean'], d_40f1_dump['AU15_c_mean'], d_40f1_dump['AU17_c_mean'], d_40f1_dump['AU20_c_mean'], d_40f1_dump['AU23_c_mean'], d_40f1_dump['AU25_c_mean'], d_40f1_dump['AU26_c_mean'], d_40f1_dump['AU28_c_mean'], d_40f1_dump['AU45_c_mean']], axis=1)

    au_array_40f2 = pd.concat([d_40f2_dump['AU01_c_mean'], d_40f2_dump['AU02_c_mean'], d_40f2_dump['AU04_c_mean'], d_40f2_dump['AU05_c_mean'], d_40f2_dump['AU06_c_mean'], d_40f2_dump['AU07_c_mean'], d_40f2_dump['AU09_c_mean'], d_40f2_dump['AU10_c_mean'], d_40f2_dump['AU12_c_mean'], d_40f2_dump['AU14_c_mean'], d_40f2_dump['AU15_c_mean'], d_40f2_dump['AU17_c_mean'], d_40f2_dump['AU20_c_mean'], d_40f2_dump['AU23_c_mean'], d_40f2_dump['AU25_c_mean'], d_40f2_dump['AU26_c_mean'], d_40f2_dump['AU28_c_mean'], d_40f2_dump['AU45_c_mean']], axis=1)

    au_array_40f3 = pd.concat([d_40f3_dump['AU01_c_mean'], d_40f3_dump['AU02_c_mean'], d_40f3_dump['AU04_c_mean'], d_40f3_dump['AU05_c_mean'], d_40f3_dump['AU06_c_mean'], d_40f3_dump['AU07_c_mean'], d_40f3_dump['AU09_c_mean'], d_40f3_dump['AU10_c_mean'], d_40f3_dump['AU12_c_mean'], d_40f3_dump['AU14_c_mean'], d_40f3_dump['AU15_c_mean'], d_40f3_dump['AU17_c_mean'], d_40f3_dump['AU20_c_mean'], d_40f3_dump['AU23_c_mean'], d_40f3_dump['AU25_c_mean'], d_40f3_dump['AU26_c_mean'], d_40f3_dump['AU28_c_mean'], d_40f3_dump['AU45_c_mean']], axis=1)

    au_array_40f4 = pd.concat([d_40f4_dump['AU01_c_mean'], d_40f4_dump['AU02_c_mean'], d_40f4_dump['AU04_c_mean'], d_40f4_dump['AU05_c_mean'], d_40f4_dump['AU06_c_mean'], d_40f4_dump['AU07_c_mean'], d_40f4_dump['AU09_c_mean'], d_40f4_dump['AU10_c_mean'], d_40f4_dump['AU12_c_mean'], d_40f4_dump['AU14_c_mean'], d_40f4_dump['AU15_c_mean'], d_40f4_dump['AU17_c_mean'], d_40f4_dump['AU20_c_mean'], d_40f4_dump['AU23_c_mean'], d_40f4_dump['AU25_c_mean'], d_40f4_dump['AU26_c_mean'], d_40f4_dump['AU28_c_mean'], d_40f4_dump['AU45_c_mean']], axis=1)


    au_array_50f1 = pd.concat([d_50f1_dump['AU01_c_mean'], d_50f1_dump['AU02_c_mean'], d_50f1_dump['AU04_c_mean'], d_50f1_dump['AU05_c_mean'], d_50f1_dump['AU06_c_mean'], d_50f1_dump['AU07_c_mean'], d_50f1_dump['AU09_c_mean'], d_50f1_dump['AU10_c_mean'], d_50f1_dump['AU12_c_mean'], d_50f1_dump['AU14_c_mean'], d_50f1_dump['AU15_c_mean'], d_50f1_dump['AU17_c_mean'], d_50f1_dump['AU20_c_mean'], d_50f1_dump['AU23_c_mean'], d_50f1_dump['AU25_c_mean'], d_50f1_dump['AU26_c_mean'], d_50f1_dump['AU28_c_mean'], d_50f1_dump['AU45_c_mean']], axis=1)

    au_array_50f2 = pd.concat([d_50f2_dump['AU01_c_mean'], d_50f2_dump['AU02_c_mean'], d_50f2_dump['AU04_c_mean'], d_50f2_dump['AU05_c_mean'], d_50f2_dump['AU06_c_mean'], d_50f2_dump['AU07_c_mean'], d_50f2_dump['AU09_c_mean'], d_50f2_dump['AU10_c_mean'], d_50f2_dump['AU12_c_mean'], d_50f2_dump['AU14_c_mean'], d_50f2_dump['AU15_c_mean'], d_50f2_dump['AU17_c_mean'], d_50f2_dump['AU20_c_mean'], d_50f2_dump['AU23_c_mean'], d_50f2_dump['AU25_c_mean'], d_50f2_dump['AU26_c_mean'], d_50f2_dump['AU28_c_mean'], d_50f2_dump['AU45_c_mean']], axis=1)

    au_array_50f3 = pd.concat([d_50f3_dump['AU01_c_mean'], d_50f3_dump['AU02_c_mean'], d_50f3_dump['AU04_c_mean'], d_50f3_dump['AU05_c_mean'], d_50f3_dump['AU06_c_mean'], d_50f3_dump['AU07_c_mean'], d_50f3_dump['AU09_c_mean'], d_50f3_dump['AU10_c_mean'], d_50f3_dump['AU12_c_mean'], d_50f3_dump['AU14_c_mean'], d_50f3_dump['AU15_c_mean'], d_50f3_dump['AU17_c_mean'], d_50f3_dump['AU20_c_mean'], d_50f3_dump['AU23_c_mean'], d_50f3_dump['AU25_c_mean'], d_50f3_dump['AU26_c_mean'], d_50f3_dump['AU28_c_mean'], d_50f3_dump['AU45_c_mean']], axis=1)


    au_array_20m1 = pd.concat([d_20m1_dump['AU01_c_mean'], d_20m1_dump['AU02_c_mean'], d_20m1_dump['AU04_c_mean'], d_20m1_dump['AU05_c_mean'], d_20m1_dump['AU06_c_mean'], d_20m1_dump['AU07_c_mean'], d_20m1_dump['AU09_c_mean'], d_20m1_dump['AU10_c_mean'], d_20m1_dump['AU12_c_mean'], d_20m1_dump['AU14_c_mean'], d_20m1_dump['AU15_c_mean'], d_20m1_dump['AU17_c_mean'], d_20m1_dump['AU20_c_mean'], d_20m1_dump['AU23_c_mean'], d_20m1_dump['AU25_c_mean'], d_20m1_dump['AU26_c_mean'], d_20m1_dump['AU28_c_mean'], d_20m1_dump['AU45_c_mean']], axis=1) 

    au_array_20m2 = pd.concat([d_20m2_dump['AU01_c_mean'], d_20m2_dump['AU02_c_mean'], d_20m2_dump['AU04_c_mean'], d_20m2_dump['AU05_c_mean'], d_20m2_dump['AU06_c_mean'], d_20m2_dump['AU07_c_mean'], d_20m2_dump['AU09_c_mean'], d_20m2_dump['AU10_c_mean'], d_20m2_dump['AU12_c_mean'], d_20m2_dump['AU14_c_mean'], d_20m2_dump['AU15_c_mean'], d_20m2_dump['AU17_c_mean'], d_20m2_dump['AU20_c_mean'], d_20m2_dump['AU23_c_mean'], d_20m2_dump['AU25_c_mean'], d_20m2_dump['AU26_c_mean'], d_20m2_dump['AU28_c_mean'], d_20m2_dump['AU45_c_mean']], axis=1)    

    au_array_20m3 = pd.concat([d_20m3_dump['AU01_c_mean'], d_20m3_dump['AU02_c_mean'], d_20m3_dump['AU04_c_mean'], d_20m3_dump['AU05_c_mean'], d_20m3_dump['AU06_c_mean'], d_20m3_dump['AU07_c_mean'], d_20m3_dump['AU09_c_mean'], d_20m3_dump['AU10_c_mean'], d_20m3_dump['AU12_c_mean'], d_20m3_dump['AU14_c_mean'], d_20m3_dump['AU15_c_mean'], d_20m3_dump['AU17_c_mean'], d_20m3_dump['AU20_c_mean'], d_20m3_dump['AU23_c_mean'], d_20m3_dump['AU25_c_mean'], d_20m3_dump['AU26_c_mean'], d_20m3_dump['AU28_c_mean'], d_20m3_dump['AU45_c_mean']], axis=1)

    au_array_20m4 = pd.concat([d_20m4_dump['AU01_c_mean'], d_20m4_dump['AU02_c_mean'], d_20m4_dump['AU04_c_mean'], d_20m4_dump['AU05_c_mean'], d_20m4_dump['AU06_c_mean'], d_20m4_dump['AU07_c_mean'], d_20m4_dump['AU09_c_mean'], d_20m4_dump['AU10_c_mean'], d_20m4_dump['AU12_c_mean'], d_20m4_dump['AU14_c_mean'], d_20m4_dump['AU15_c_mean'], d_20m4_dump['AU17_c_mean'], d_20m4_dump['AU20_c_mean'], d_20m4_dump['AU23_c_mean'], d_20m4_dump['AU25_c_mean'], d_20m4_dump['AU26_c_mean'], d_20m4_dump['AU28_c_mean'], d_20m4_dump['AU45_c_mean']], axis=1)

    au_array_20m5 = pd.concat([d_20m5_dump['AU01_c_mean'], d_20m5_dump['AU02_c_mean'], d_20m5_dump['AU04_c_mean'], d_20m5_dump['AU05_c_mean'], d_20m5_dump['AU06_c_mean'], d_20m5_dump['AU07_c_mean'], d_20m5_dump['AU09_c_mean'], d_20m5_dump['AU10_c_mean'], d_20m5_dump['AU12_c_mean'], d_20m5_dump['AU14_c_mean'], d_20m5_dump['AU15_c_mean'], d_20m5_dump['AU17_c_mean'], d_20m5_dump['AU20_c_mean'], d_20m5_dump['AU23_c_mean'], d_20m5_dump['AU25_c_mean'], d_20m5_dump['AU26_c_mean'], d_20m5_dump['AU28_c_mean'], d_20m5_dump['AU45_c_mean']], axis=1)


    au_array_30m1 = pd.concat([d_30m1_dump['AU01_c_mean'], d_30m1_dump['AU02_c_mean'], d_30m1_dump['AU04_c_mean'], d_30m1_dump['AU05_c_mean'], d_30m1_dump['AU06_c_mean'], d_30m1_dump['AU07_c_mean'], d_30m1_dump['AU09_c_mean'], d_30m1_dump['AU10_c_mean'], d_30m1_dump['AU12_c_mean'], d_30m1_dump['AU14_c_mean'], d_30m1_dump['AU15_c_mean'], d_30m1_dump['AU17_c_mean'], d_30m1_dump['AU20_c_mean'], d_30m1_dump['AU23_c_mean'], d_30m1_dump['AU25_c_mean'], d_30m1_dump['AU26_c_mean'], d_30m1_dump['AU28_c_mean'], d_30m1_dump['AU45_c_mean']], axis=1)

    au_array_30m2 = pd.concat([d_30m2_dump['AU01_c_mean'], d_30m2_dump['AU02_c_mean'], d_30m2_dump['AU04_c_mean'], d_30m2_dump['AU05_c_mean'], d_30m2_dump['AU06_c_mean'], d_30m2_dump['AU07_c_mean'], d_30m2_dump['AU09_c_mean'], d_30m2_dump['AU10_c_mean'], d_30m2_dump['AU12_c_mean'], d_30m2_dump['AU14_c_mean'], d_30m2_dump['AU15_c_mean'], d_30m2_dump['AU17_c_mean'], d_30m2_dump['AU20_c_mean'], d_30m2_dump['AU23_c_mean'], d_30m2_dump['AU25_c_mean'], d_30m2_dump['AU26_c_mean'], d_30m2_dump['AU28_c_mean'], d_30m2_dump['AU45_c_mean']], axis=1)

    au_array_30m3 = pd.concat([d_30m3_dump['AU01_c_mean'], d_30m3_dump['AU02_c_mean'], d_30m3_dump['AU04_c_mean'], d_30m3_dump['AU05_c_mean'], d_30m3_dump['AU06_c_mean'], d_30m3_dump['AU07_c_mean'], d_30m3_dump['AU09_c_mean'], d_30m3_dump['AU10_c_mean'], d_30m3_dump['AU12_c_mean'], d_30m3_dump['AU14_c_mean'], d_30m3_dump['AU15_c_mean'], d_30m3_dump['AU17_c_mean'], d_30m3_dump['AU20_c_mean'], d_30m3_dump['AU23_c_mean'], d_30m3_dump['AU25_c_mean'], d_30m3_dump['AU26_c_mean'], d_30m3_dump['AU28_c_mean'], d_30m3_dump['AU45_c_mean']], axis=1)


    au_array_40m1 = pd.concat([d_40m1_dump['AU01_c_mean'], d_40m1_dump['AU02_c_mean'], d_40m1_dump['AU04_c_mean'], d_40m1_dump['AU05_c_mean'], d_40m1_dump['AU06_c_mean'], d_40m1_dump['AU07_c_mean'], d_40m1_dump['AU09_c_mean'], d_40m1_dump['AU10_c_mean'], d_40m1_dump['AU12_c_mean'], d_40m1_dump['AU14_c_mean'], d_40m1_dump['AU15_c_mean'], d_40m1_dump['AU17_c_mean'], d_40m1_dump['AU20_c_mean'], d_40m1_dump['AU23_c_mean'], d_40m1_dump['AU25_c_mean'], d_40m1_dump['AU26_c_mean'], d_40m1_dump['AU28_c_mean'], d_40m1_dump['AU45_c_mean']], axis=1) 

    au_array_40m2 = pd.concat([d_40m2_dump['AU01_c_mean'], d_40m2_dump['AU02_c_mean'], d_40m2_dump['AU04_c_mean'], d_40m2_dump['AU05_c_mean'], d_40m2_dump['AU06_c_mean'], d_40m2_dump['AU07_c_mean'], d_40m2_dump['AU09_c_mean'], d_40m2_dump['AU10_c_mean'], d_40m2_dump['AU12_c_mean'], d_40m2_dump['AU14_c_mean'], d_40m2_dump['AU15_c_mean'], d_40m2_dump['AU17_c_mean'], d_40m2_dump['AU20_c_mean'], d_40m2_dump['AU23_c_mean'], d_40m2_dump['AU25_c_mean'], d_40m2_dump['AU26_c_mean'], d_40m2_dump['AU28_c_mean'], d_40m2_dump['AU45_c_mean']], axis=1)    

    au_array_40m3 = pd.concat([d_40m3_dump['AU01_c_mean'], d_40m3_dump['AU02_c_mean'], d_40m3_dump['AU04_c_mean'], d_40m3_dump['AU05_c_mean'], d_40m3_dump['AU06_c_mean'], d_40m3_dump['AU07_c_mean'], d_40m3_dump['AU09_c_mean'], d_40m3_dump['AU10_c_mean'], d_40m3_dump['AU12_c_mean'], d_40m3_dump['AU14_c_mean'], d_40m3_dump['AU15_c_mean'], d_40m3_dump['AU17_c_mean'], d_40m3_dump['AU20_c_mean'], d_40m3_dump['AU23_c_mean'], d_40m3_dump['AU25_c_mean'], d_40m3_dump['AU26_c_mean'], d_40m3_dump['AU28_c_mean'], d_40m3_dump['AU45_c_mean']], axis=1)

    au_array_40m4 = pd.concat([d_40m4_dump['AU01_c_mean'], d_40m4_dump['AU02_c_mean'], d_40m4_dump['AU04_c_mean'], d_40m4_dump['AU05_c_mean'], d_40m4_dump['AU06_c_mean'], d_40m4_dump['AU07_c_mean'], d_40m4_dump['AU09_c_mean'], d_40m4_dump['AU10_c_mean'], d_40m4_dump['AU12_c_mean'], d_40m4_dump['AU14_c_mean'], d_40m4_dump['AU15_c_mean'], d_40m4_dump['AU17_c_mean'], d_40m4_dump['AU20_c_mean'], d_40m4_dump['AU23_c_mean'], d_40m4_dump['AU25_c_mean'], d_40m4_dump['AU26_c_mean'], d_40m4_dump['AU28_c_mean'], d_40m4_dump['AU45_c_mean']], axis=1)

    au_array_40m5 = pd.concat([d_40m5_dump['AU01_c_mean'], d_40m5_dump['AU02_c_mean'], d_40m5_dump['AU04_c_mean'], d_40m5_dump['AU05_c_mean'], d_40m5_dump['AU06_c_mean'], d_40m5_dump['AU07_c_mean'], d_40m5_dump['AU09_c_mean'], d_40m5_dump['AU10_c_mean'], d_40m5_dump['AU12_c_mean'], d_40m5_dump['AU14_c_mean'], d_40m5_dump['AU15_c_mean'], d_40m5_dump['AU17_c_mean'], d_40m5_dump['AU20_c_mean'], d_40m5_dump['AU23_c_mean'], d_40m5_dump['AU25_c_mean'], d_40m5_dump['AU26_c_mean'], d_40m5_dump['AU28_c_mean'], d_40m5_dump['AU45_c_mean']], axis=1)


    int_ant_array_20f1 = pd.concat([d_20f1_dump['IN1'], d_20f1_dump['IN2'], d_20f1_dump['IN3'], d_20f1_dump['IN4'], d_20f1_dump['IN5'], d_20f1_dump['IN6']], axis=1)
    int_ant_array_20f2 = pd.concat([d_20f2_dump['IN1'], d_20f2_dump['IN2'], d_20f2_dump['IN3'], d_20f2_dump['IN4'], d_20f2_dump['IN5'], d_20f2_dump['IN6']], axis=1)
    int_ant_array_20f3 = pd.concat([d_20f3_dump['IN1'], d_20f3_dump['IN2'], d_20f3_dump['IN3'], d_20f3_dump['IN4'], d_20f3_dump['IN5'], d_20f3_dump['IN6']], axis=1)
    int_ant_array_20f4 = pd.concat([d_20f4_dump['IN1'], d_20f4_dump['IN2'], d_20f4_dump['IN3'], d_20f4_dump['IN4'], d_20f4_dump['IN5'], d_20f4_dump['IN6']], axis=1)

    int_ant_array_30f1 = pd.concat([d_30f1_dump['IN1'], d_30f1_dump['IN2'], d_30f1_dump['IN3'], d_30f1_dump['IN4'], d_30f1_dump['IN5'], d_30f1_dump['IN6']], axis=1)
    int_ant_array_30f2 = pd.concat([d_30f2_dump['IN1'], d_30f2_dump['IN2'], d_30f2_dump['IN3'], d_30f2_dump['IN4'], d_30f2_dump['IN5'], d_30f2_dump['IN6']], axis=1)
    int_ant_array_30f3 = pd.concat([d_30f3_dump['IN1'], d_30f3_dump['IN2'], d_30f3_dump['IN3'], d_30f3_dump['IN4'], d_30f3_dump['IN5'], d_30f3_dump['IN6']], axis=1)

    int_ant_array_40f1 = pd.concat([d_40f1_dump['IN1'], d_40f1_dump['IN2'], d_40f1_dump['IN3'], d_40f1_dump['IN4'], d_40f1_dump['IN5'], d_40f1_dump['IN6']], axis=1)
    int_ant_array_40f2 = pd.concat([d_40f2_dump['IN1'], d_40f2_dump['IN2'], d_40f2_dump['IN3'], d_40f2_dump['IN4'], d_40f2_dump['IN5'], d_40f2_dump['IN6']], axis=1)
    int_ant_array_40f3 = pd.concat([d_40f3_dump['IN1'], d_40f3_dump['IN2'], d_40f3_dump['IN3'], d_40f3_dump['IN4'], d_40f3_dump['IN5'], d_40f3_dump['IN6']], axis=1)
    int_ant_array_40f4 = pd.concat([d_40f4_dump['IN1'], d_40f4_dump['IN2'], d_40f4_dump['IN3'], d_40f4_dump['IN4'], d_40f4_dump['IN5'], d_40f4_dump['IN6']], axis=1)

    int_ant_array_50f1 = pd.concat([d_50f1_dump['IN1'], d_50f1_dump['IN2'], d_50f1_dump['IN3'], d_50f1_dump['IN4'], d_50f1_dump['IN5'], d_50f1_dump['IN6']], axis=1)
    int_ant_array_50f2 = pd.concat([d_50f2_dump['IN1'], d_50f2_dump['IN2'], d_50f2_dump['IN3'], d_50f2_dump['IN4'], d_50f2_dump['IN5'], d_50f2_dump['IN6']], axis=1)
    int_ant_array_50f3 = pd.concat([d_50f3_dump['IN1'], d_50f3_dump['IN2'], d_50f3_dump['IN3'], d_50f3_dump['IN4'], d_50f3_dump['IN5'], d_50f3_dump['IN6']], axis=1)

    int_ant_array_20m1 = pd.concat([d_20m1_dump['IN1'], d_20m1_dump['IN2'], d_20m1_dump['IN3'], d_20m1_dump['IN4'], d_20m1_dump['IN5'], d_20m1_dump['IN6']], axis=1)
    int_ant_array_20m2 = pd.concat([d_20m2_dump['IN1'], d_20m2_dump['IN2'], d_20m2_dump['IN3'], d_20m2_dump['IN4'], d_20m2_dump['IN5'], d_20m2_dump['IN6']], axis=1)
    int_ant_array_20m3 = pd.concat([d_20m3_dump['IN1'], d_20m3_dump['IN2'], d_20m3_dump['IN3'], d_20m3_dump['IN4'], d_20m3_dump['IN5'], d_20m3_dump['IN6']], axis=1)
    int_ant_array_20m4 = pd.concat([d_20m4_dump['IN1'], d_20m4_dump['IN2'], d_20m4_dump['IN3'], d_20m4_dump['IN4'], d_20m4_dump['IN5'], d_20m4_dump['IN6']], axis=1)
    int_ant_array_20m5 = pd.concat([d_20m5_dump['IN1'], d_20m5_dump['IN2'], d_20m5_dump['IN3'], d_20m5_dump['IN4'], d_20m5_dump['IN5'], d_20m5_dump['IN6']], axis=1)

    int_ant_array_30m1 = pd.concat([d_30m1_dump['IN1'], d_30m1_dump['IN2'], d_30m1_dump['IN3'], d_30m1_dump['IN4'], d_30m1_dump['IN5'], d_30m1_dump['IN6']], axis=1)
    int_ant_array_30m2 = pd.concat([d_30m2_dump['IN1'], d_30m2_dump['IN2'], d_30m2_dump['IN3'], d_30m2_dump['IN4'], d_30m2_dump['IN5'], d_30m2_dump['IN6']], axis=1)
    int_ant_array_30m3 = pd.concat([d_30m3_dump['IN1'], d_30m3_dump['IN2'], d_30m3_dump['IN3'], d_30m3_dump['IN4'], d_30m3_dump['IN5'], d_30m3_dump['IN6']], axis=1)

    int_ant_array_40m1 = pd.concat([d_40m1_dump['IN1'], d_40m1_dump['IN2'], d_40m1_dump['IN3'], d_40m1_dump['IN4'], d_40m1_dump['IN5'], d_40m1_dump['IN6']], axis=1)
    int_ant_array_40m2 = pd.concat([d_40m2_dump['IN1'], d_40m2_dump['IN2'], d_40m2_dump['IN3'], d_40m2_dump['IN4'], d_40m2_dump['IN5'], d_40m2_dump['IN6']], axis=1)
    int_ant_array_40m3 = pd.concat([d_40m3_dump['IN1'], d_40m3_dump['IN2'], d_40m3_dump['IN3'], d_40m3_dump['IN4'], d_40m3_dump['IN5'], d_40m3_dump['IN6']], axis=1)
    int_ant_array_40m4 = pd.concat([d_40m4_dump['IN1'], d_40m4_dump['IN2'], d_40m4_dump['IN3'], d_40m4_dump['IN4'], d_40m4_dump['IN5'], d_40m4_dump['IN6']], axis=1)
    int_ant_array_40m5 = pd.concat([d_40m5_dump['IN1'], d_40m5_dump['IN2'], d_40m5_dump['IN3'], d_40m5_dump['IN4'], d_40m5_dump['IN5'], d_40m5_dump['IN6']], axis=1)


    int_ant_array_20f1_bool_o = (int_ant_array_20f1 == "o")
    int_ant_array_20f1_bool_x = (int_ant_array_20f1 == "x")
    int_ant_array_20f1_bool_o_num = int_ant_array_20f1_bool_o.sum(axis='columns')
    int_ant_array_20f1_bool_x_num = int_ant_array_20f1_bool_x.sum(axis='columns')
    int_ant_array_20f1_bool = int_ant_array_20f1_bool_o_num > int_ant_array_20f1_bool_x_num
    int_ant_array_20f1_score = int_ant_array_20f1_bool.mask(int_ant_array_20f1_bool==True, 1)
    int_ant_array_20f1_score = int_ant_array_20f1_score.mask(int_ant_array_20f1_bool==False, 0)

    int_ant_array_20f2_bool_o = (int_ant_array_20f2 == "o")
    int_ant_array_20f2_bool_x = (int_ant_array_20f2 == "x")
    int_ant_array_20f2_bool_o_num = int_ant_array_20f2_bool_o.sum(axis='columns')
    int_ant_array_20f2_bool_x_num = int_ant_array_20f2_bool_x.sum(axis='columns')
    int_ant_array_20f2_bool = int_ant_array_20f2_bool_o_num > int_ant_array_20f2_bool_x_num 
    int_ant_array_20f2_score = int_ant_array_20f2_bool.mask(int_ant_array_20f2_bool==True, 1)
    int_ant_array_20f2_score = int_ant_array_20f2_score.mask(int_ant_array_20f2_bool==False, 0)

    int_ant_array_20f3_bool_o = (int_ant_array_20f3 == "o")
    int_ant_array_20f3_bool_x = (int_ant_array_20f3 == "x")
    int_ant_array_20f3_bool_o_num = int_ant_array_20f3_bool_o.sum(axis='columns')
    int_ant_array_20f3_bool_x_num = int_ant_array_20f3_bool_x.sum(axis='columns')
    int_ant_array_20f3_bool = int_ant_array_20f3_bool_o_num > int_ant_array_20f3_bool_x_num
    int_ant_array_20f3_score = int_ant_array_20f3_bool.mask(int_ant_array_20f3_bool==True, 1)
    int_ant_array_20f3_score = int_ant_array_20f3_score.mask(int_ant_array_20f3_bool==False, 0)

    int_ant_array_20f4_bool_o = (int_ant_array_20f4 == "o")
    int_ant_array_20f4_bool_x = (int_ant_array_20f4 == "x")
    int_ant_array_20f4_bool_o_num = int_ant_array_20f4_bool_o.sum(axis='columns')
    int_ant_array_20f4_bool_x_num = int_ant_array_20f4_bool_x.sum(axis='columns')
    int_ant_array_20f4_bool = int_ant_array_20f4_bool_o_num > int_ant_array_20f4_bool_x_num
    int_ant_array_20f4_score = int_ant_array_20f4_bool.mask(int_ant_array_20f4_bool==True, 1)
    int_ant_array_20f4_score = int_ant_array_20f4_score.mask(int_ant_array_20f4_bool==False, 0)

    
    int_ant_array_30f1_bool_o = (int_ant_array_30f1 == "o")
    int_ant_array_30f1_bool_x = (int_ant_array_30f1 == "x")
    int_ant_array_30f1_bool_o_num = int_ant_array_30f1_bool_o.sum(axis='columns')
    int_ant_array_30f1_bool_x_num = int_ant_array_30f1_bool_x.sum(axis='columns')
    int_ant_array_30f1_bool = int_ant_array_30f1_bool_o_num > int_ant_array_30f1_bool_x_num
    int_ant_array_30f1_score = int_ant_array_30f1_bool.mask(int_ant_array_30f1_bool==True, 1)
    int_ant_array_30f1_score = int_ant_array_30f1_score.mask(int_ant_array_30f1_bool==False, 0)

    int_ant_array_30f2_bool_o = (int_ant_array_30f2 == "o")
    int_ant_array_30f2_bool_x = (int_ant_array_30f2 == "x")
    int_ant_array_30f2_bool_o_num = int_ant_array_30f2_bool_o.sum(axis='columns')
    int_ant_array_30f2_bool_x_num = int_ant_array_30f2_bool_x.sum(axis='columns')
    int_ant_array_30f2_bool = int_ant_array_30f2_bool_o_num > int_ant_array_30f2_bool_x_num 
    int_ant_array_30f2_score = int_ant_array_30f2_bool.mask(int_ant_array_30f2_bool==True, 1)
    int_ant_array_30f2_score = int_ant_array_30f2_score.mask(int_ant_array_30f2_bool==False, 0)

    int_ant_array_30f3_bool_o = (int_ant_array_30f3 == "o")
    int_ant_array_30f3_bool_x = (int_ant_array_30f3 == "x")
    int_ant_array_30f3_bool_o_num = int_ant_array_30f3_bool_o.sum(axis='columns')
    int_ant_array_30f3_bool_x_num = int_ant_array_30f3_bool_x.sum(axis='columns')
    int_ant_array_30f3_bool = int_ant_array_30f3_bool_o_num > int_ant_array_30f3_bool_x_num
    int_ant_array_30f3_score = int_ant_array_30f3_bool.mask(int_ant_array_30f3_bool==True, 1)
    int_ant_array_30f3_score = int_ant_array_30f3_score.mask(int_ant_array_30f3_bool==False, 0)


    int_ant_array_40f1_bool_o = (int_ant_array_40f1 == "o")
    int_ant_array_40f1_bool_x = (int_ant_array_40f1 == "x")
    int_ant_array_40f1_bool_o_num = int_ant_array_40f1_bool_o.sum(axis='columns')
    int_ant_array_40f1_bool_x_num = int_ant_array_40f1_bool_x.sum(axis='columns')
    int_ant_array_40f1_bool = int_ant_array_40f1_bool_o_num > int_ant_array_40f1_bool_x_num
    int_ant_array_40f1_score = int_ant_array_40f1_bool.mask(int_ant_array_40f1_bool==True, 1)
    int_ant_array_40f1_score = int_ant_array_40f1_score.mask(int_ant_array_40f1_bool==False, 0)

    int_ant_array_40f2_bool_o = (int_ant_array_40f2 == "o")
    int_ant_array_40f2_bool_x = (int_ant_array_40f2 == "x")
    int_ant_array_40f2_bool_o_num = int_ant_array_40f2_bool_o.sum(axis='columns')
    int_ant_array_40f2_bool_x_num = int_ant_array_40f2_bool_x.sum(axis='columns')
    int_ant_array_40f2_bool = int_ant_array_40f2_bool_o_num > int_ant_array_40f2_bool_x_num 
    int_ant_array_40f2_score = int_ant_array_40f2_bool.mask(int_ant_array_40f2_bool==True, 1)
    int_ant_array_40f2_score = int_ant_array_40f2_score.mask(int_ant_array_40f2_bool==False, 0)

    int_ant_array_40f3_bool_o = (int_ant_array_40f3 == "o")
    int_ant_array_40f3_bool_x = (int_ant_array_40f3 == "x")
    int_ant_array_40f3_bool_o_num = int_ant_array_40f3_bool_o.sum(axis='columns')
    int_ant_array_40f3_bool_x_num = int_ant_array_40f3_bool_x.sum(axis='columns')
    int_ant_array_40f3_bool = int_ant_array_40f3_bool_o_num > int_ant_array_40f3_bool_x_num
    int_ant_array_40f3_score = int_ant_array_40f3_bool.mask(int_ant_array_40f3_bool==True, 1)
    int_ant_array_40f3_score = int_ant_array_40f3_score.mask(int_ant_array_40f3_bool==False, 0)

    int_ant_array_40f4_bool_o = (int_ant_array_40f4 == "o")
    int_ant_array_40f4_bool_x = (int_ant_array_40f4 == "x")
    int_ant_array_40f4_bool_o_num = int_ant_array_40f4_bool_o.sum(axis='columns')
    int_ant_array_40f4_bool_x_num = int_ant_array_40f4_bool_x.sum(axis='columns')
    int_ant_array_40f4_bool = int_ant_array_40f4_bool_o_num > int_ant_array_40f4_bool_x_num
    int_ant_array_40f4_score = int_ant_array_40f4_bool.mask(int_ant_array_40f4_bool==True, 1)
    int_ant_array_40f4_score = int_ant_array_40f4_score.mask(int_ant_array_40f4_bool==False, 0)

    
    int_ant_array_50f1_bool_o = (int_ant_array_50f1 == "o")
    int_ant_array_50f1_bool_x = (int_ant_array_50f1 == "x")
    int_ant_array_50f1_bool_o_num = int_ant_array_50f1_bool_o.sum(axis='columns')
    int_ant_array_50f1_bool_x_num = int_ant_array_50f1_bool_x.sum(axis='columns')
    int_ant_array_50f1_bool = int_ant_array_50f1_bool_o_num > int_ant_array_50f1_bool_x_num
    int_ant_array_50f1_score = int_ant_array_50f1_bool.mask(int_ant_array_50f1_bool==True, 1)
    int_ant_array_50f1_score = int_ant_array_50f1_score.mask(int_ant_array_50f1_bool==False, 0)

    int_ant_array_50f2_bool_o = (int_ant_array_50f2 == "o")
    int_ant_array_50f2_bool_x = (int_ant_array_50f2 == "x")
    int_ant_array_50f2_bool_o_num = int_ant_array_50f2_bool_o.sum(axis='columns')
    int_ant_array_50f2_bool_x_num = int_ant_array_50f2_bool_x.sum(axis='columns')
    int_ant_array_50f2_bool = int_ant_array_50f2_bool_o_num > int_ant_array_50f2_bool_x_num 
    int_ant_array_50f2_score = int_ant_array_50f2_bool.mask(int_ant_array_50f2_bool==True, 1)
    int_ant_array_50f2_score = int_ant_array_50f2_score.mask(int_ant_array_50f2_bool==False, 0)

    int_ant_array_50f3_bool_o = (int_ant_array_50f3 == "o")
    int_ant_array_50f3_bool_x = (int_ant_array_50f3 == "x")
    int_ant_array_50f3_bool_o_num = int_ant_array_50f3_bool_o.sum(axis='columns')
    int_ant_array_50f3_bool_x_num = int_ant_array_50f3_bool_x.sum(axis='columns')
    int_ant_array_50f3_bool = int_ant_array_50f3_bool_o_num > int_ant_array_50f3_bool_x_num
    int_ant_array_50f3_score = int_ant_array_50f3_bool.mask(int_ant_array_50f3_bool==True, 1)
    int_ant_array_50f3_score = int_ant_array_50f3_score.mask(int_ant_array_50f3_bool==False, 0)


    int_ant_array_20m1_bool_o = (int_ant_array_20m1 == "o")
    int_ant_array_20m1_bool_x = (int_ant_array_20m1 == "x")
    int_ant_array_20m1_bool_o_num = int_ant_array_20m1_bool_o.sum(axis='columns')
    int_ant_array_20m1_bool_x_num = int_ant_array_20m1_bool_x.sum(axis='columns')
    int_ant_array_20m1_bool = int_ant_array_20m1_bool_o_num > int_ant_array_20m1_bool_x_num
    int_ant_array_20m1_score = int_ant_array_20m1_bool.mask(int_ant_array_20m1_bool==True, 1)
    int_ant_array_20m1_score = int_ant_array_20m1_score.mask(int_ant_array_20m1_bool==False, 0)

    int_ant_array_20m2_bool_o = (int_ant_array_20m2 == "o")
    int_ant_array_20m2_bool_x = (int_ant_array_20m2 == "x")
    int_ant_array_20m2_bool_o_num = int_ant_array_20m2_bool_o.sum(axis='columns')
    int_ant_array_20m2_bool_x_num = int_ant_array_20m2_bool_x.sum(axis='columns')
    int_ant_array_20m2_bool = int_ant_array_20m2_bool_o_num > int_ant_array_20m2_bool_x_num 
    int_ant_array_20m2_score = int_ant_array_20m2_bool.mask(int_ant_array_20m2_bool==True, 1)
    int_ant_array_20m2_score = int_ant_array_20m2_score.mask(int_ant_array_20m2_bool==False, 0)

    int_ant_array_20m3_bool_o = (int_ant_array_20m3 == "o")
    int_ant_array_20m3_bool_x = (int_ant_array_20m3 == "x")
    int_ant_array_20m3_bool_o_num = int_ant_array_20m3_bool_o.sum(axis='columns')
    int_ant_array_20m3_bool_x_num = int_ant_array_20m3_bool_x.sum(axis='columns')
    int_ant_array_20m3_bool = int_ant_array_20m3_bool_o_num > int_ant_array_20m3_bool_x_num
    int_ant_array_20m3_score = int_ant_array_20m3_bool.mask(int_ant_array_20m3_bool==True, 1)
    int_ant_array_20m3_score = int_ant_array_20m3_score.mask(int_ant_array_20m3_bool==False, 0)

    int_ant_array_20m4_bool_o = (int_ant_array_20m4 == "o")
    int_ant_array_20m4_bool_x = (int_ant_array_20m4 == "x")
    int_ant_array_20m4_bool_o_num = int_ant_array_20m4_bool_o.sum(axis='columns')
    int_ant_array_20m4_bool_x_num = int_ant_array_20m4_bool_x.sum(axis='columns')
    int_ant_array_20m4_bool = int_ant_array_20m4_bool_o_num > int_ant_array_20m4_bool_x_num
    int_ant_array_20m4_score = int_ant_array_20m4_bool.mask(int_ant_array_20m4_bool==True, 1)
    int_ant_array_20m4_score = int_ant_array_20m4_score.mask(int_ant_array_20m4_bool==False, 0)

    int_ant_array_20m5_bool_o = (int_ant_array_20m5 == "o")
    int_ant_array_20m5_bool_x = (int_ant_array_20m5 == "x")
    int_ant_array_20m5_bool_o_num = int_ant_array_20m5_bool_o.sum(axis='columns')
    int_ant_array_20m5_bool_x_num = int_ant_array_20m5_bool_x.sum(axis='columns')
    int_ant_array_20m5_bool = int_ant_array_20m5_bool_o_num > int_ant_array_20m5_bool_x_num
    int_ant_array_20m5_score = int_ant_array_20m5_bool.mask(int_ant_array_20m5_bool==True, 1)
    int_ant_array_20m5_score = int_ant_array_20m5_score.mask(int_ant_array_20m5_bool==False, 0)

    
    int_ant_array_30m1_bool_o = (int_ant_array_30m1 == "o")
    int_ant_array_30m1_bool_x = (int_ant_array_30m1 == "x")
    int_ant_array_30m1_bool_o_num = int_ant_array_30m1_bool_o.sum(axis='columns')
    int_ant_array_30m1_bool_x_num = int_ant_array_30m1_bool_x.sum(axis='columns')
    int_ant_array_30m1_bool = int_ant_array_30m1_bool_o_num > int_ant_array_30m1_bool_x_num
    int_ant_array_30m1_score = int_ant_array_30m1_bool.mask(int_ant_array_30m1_bool==True, 1)
    int_ant_array_30m1_score = int_ant_array_30m1_score.mask(int_ant_array_30m1_bool==False, 0)

    int_ant_array_30m2_bool_o = (int_ant_array_30m2 == "o")
    int_ant_array_30m2_bool_x = (int_ant_array_30m2 == "x")
    int_ant_array_30m2_bool_o_num = int_ant_array_30m2_bool_o.sum(axis='columns')
    int_ant_array_30m2_bool_x_num = int_ant_array_30m2_bool_x.sum(axis='columns')
    int_ant_array_30m2_bool = int_ant_array_30m2_bool_o_num > int_ant_array_30m2_bool_x_num 
    int_ant_array_30m2_score = int_ant_array_30m2_bool.mask(int_ant_array_30m2_bool==True, 1)
    int_ant_array_30m2_score = int_ant_array_30m2_score.mask(int_ant_array_30m2_bool==False, 0)

    int_ant_array_30m3_bool_o = (int_ant_array_30m3 == "o")
    int_ant_array_30m3_bool_x = (int_ant_array_30m3 == "x")
    int_ant_array_30m3_bool_o_num = int_ant_array_30m3_bool_o.sum(axis='columns')
    int_ant_array_30m3_bool_x_num = int_ant_array_30m3_bool_x.sum(axis='columns')
    int_ant_array_30m3_bool = int_ant_array_30m3_bool_o_num > int_ant_array_30m3_bool_x_num
    int_ant_array_30m3_score = int_ant_array_30m3_bool.mask(int_ant_array_30m3_bool==True, 1)
    int_ant_array_30m3_score = int_ant_array_30m3_score.mask(int_ant_array_30m3_bool==False, 0)


    int_ant_array_40m1_bool_o = (int_ant_array_40m1 == "o")
    int_ant_array_40m1_bool_x = (int_ant_array_40m1 == "x")
    int_ant_array_40m1_bool_o_num = int_ant_array_40m1_bool_o.sum(axis='columns')
    int_ant_array_40m1_bool_x_num = int_ant_array_40m1_bool_x.sum(axis='columns')
    int_ant_array_40m1_bool = int_ant_array_40m1_bool_o_num > int_ant_array_40m1_bool_x_num
    int_ant_array_40m1_score = int_ant_array_40m1_bool.mask(int_ant_array_40m1_bool==True, 1)
    int_ant_array_40m1_score = int_ant_array_40m1_score.mask(int_ant_array_40m1_bool==False, 0)

    int_ant_array_40m2_bool_o = (int_ant_array_40m2 == "o")
    int_ant_array_40m2_bool_x = (int_ant_array_40m2 == "x")
    int_ant_array_40m2_bool_o_num = int_ant_array_40m2_bool_o.sum(axis='columns')
    int_ant_array_40m2_bool_x_num = int_ant_array_40m2_bool_x.sum(axis='columns')
    int_ant_array_40m2_bool = int_ant_array_40m2_bool_o_num > int_ant_array_40m2_bool_x_num 
    int_ant_array_40m2_score = int_ant_array_40m2_bool.mask(int_ant_array_40m2_bool==True, 1)
    int_ant_array_40m2_score = int_ant_array_40m2_score.mask(int_ant_array_40m2_bool==False, 0)

    int_ant_array_40m3_bool_o = (int_ant_array_40m3 == "o")
    int_ant_array_40m3_bool_x = (int_ant_array_40m3 == "x")
    int_ant_array_40m3_bool_o_num = int_ant_array_40m3_bool_o.sum(axis='columns')
    int_ant_array_40m3_bool_x_num = int_ant_array_40m3_bool_x.sum(axis='columns')
    int_ant_array_40m3_bool = int_ant_array_40m3_bool_o_num > int_ant_array_40m3_bool_x_num
    int_ant_array_40m3_score = int_ant_array_40m3_bool.mask(int_ant_array_40m3_bool==True, 1)
    int_ant_array_40m3_score = int_ant_array_40m3_score.mask(int_ant_array_40m3_bool==False, 0)

    int_ant_array_40m4_bool_o = (int_ant_array_40m4 == "o")
    int_ant_array_40m4_bool_x = (int_ant_array_40m4 == "x")
    int_ant_array_40m4_bool_o_num = int_ant_array_40m4_bool_o.sum(axis='columns')
    int_ant_array_40m4_bool_x_num = int_ant_array_40m4_bool_x.sum(axis='columns')
    int_ant_array_40m4_bool = int_ant_array_40m4_bool_o_num > int_ant_array_40m4_bool_x_num
    int_ant_array_40m4_score = int_ant_array_40m4_bool.mask(int_ant_array_40m4_bool==True, 1)
    int_ant_array_40m4_score = int_ant_array_40m4_score.mask(int_ant_array_40m4_bool==False, 0)

    int_ant_array_40m5_bool_o = (int_ant_array_40m5 == "o")
    int_ant_array_40m5_bool_x = (int_ant_array_40m5 == "x")
    int_ant_array_40m5_bool_o_num = int_ant_array_40m5_bool_o.sum(axis='columns')
    int_ant_array_40m5_bool_x_num = int_ant_array_40m5_bool_x.sum(axis='columns')
    int_ant_array_40m5_bool = int_ant_array_40m5_bool_o_num > int_ant_array_40m5_bool_x_num
    int_ant_array_40m5_score = int_ant_array_40m5_bool.mask(int_ant_array_40m5_bool==True, 1)
    int_ant_array_40m5_score = int_ant_array_40m5_score.mask(int_ant_array_40m5_bool==False, 0)

    au_int_array_20f1 = pd.concat([au_array_20f1, int_ant_array_20f1_score], axis=1)
    au_int_array_20f2 = pd.concat([au_array_20f2, int_ant_array_20f2_score], axis=1)
    au_int_array_20f3 = pd.concat([au_array_20f3, int_ant_array_20f3_score], axis=1)
    au_int_array_20f4 = pd.concat([au_array_20f4, int_ant_array_20f4_score], axis=1)

    au_int_array_30f1 = pd.concat([au_array_30f1, int_ant_array_30f1_score], axis=1)
    au_int_array_30f2 = pd.concat([au_array_30f2, int_ant_array_30f2_score], axis=1)
    au_int_array_30f3 = pd.concat([au_array_30f3, int_ant_array_30f3_score], axis=1)

    au_int_array_40f1 = pd.concat([au_array_40f1, int_ant_array_40f1_score], axis=1)
    au_int_array_40f2 = pd.concat([au_array_40f2, int_ant_array_40f2_score], axis=1)
    au_int_array_40f3 = pd.concat([au_array_40f3, int_ant_array_40f3_score], axis=1)
    au_int_array_40f4 = pd.concat([au_array_40f4, int_ant_array_40f4_score], axis=1)

    au_int_array_50f1 = pd.concat([au_array_50f1, int_ant_array_50f1_score], axis=1)
    au_int_array_50f2 = pd.concat([au_array_50f2, int_ant_array_50f2_score], axis=1)
    au_int_array_50f3 = pd.concat([au_array_50f3, int_ant_array_50f3_score], axis=1)

    au_int_array_20m1 = pd.concat([au_array_20m1, int_ant_array_20m1_score], axis=1)
    au_int_array_20m2 = pd.concat([au_array_20m2, int_ant_array_20m2_score], axis=1)
    au_int_array_20m3 = pd.concat([au_array_20m3, int_ant_array_20m3_score], axis=1)
    au_int_array_20m4 = pd.concat([au_array_20m4, int_ant_array_20m4_score], axis=1)
    au_int_array_20m5 = pd.concat([au_array_20m5, int_ant_array_20m5_score], axis=1)

    au_int_array_30m1 = pd.concat([au_array_30m1, int_ant_array_30m1_score], axis=1)
    au_int_array_30m2 = pd.concat([au_array_30m2, int_ant_array_30m2_score], axis=1)
    au_int_array_30m3 = pd.concat([au_array_30m3, int_ant_array_30m3_score], axis=1)

    au_int_array_40m1 = pd.concat([au_array_40m1, int_ant_array_40m1_score], axis=1)
    au_int_array_40m2 = pd.concat([au_array_40m2, int_ant_array_40m2_score], axis=1)
    au_int_array_40m3 = pd.concat([au_array_40m3, int_ant_array_40m3_score], axis=1)
    au_int_array_40m4 = pd.concat([au_array_40m4, int_ant_array_40m4_score], axis=1)
    au_int_array_40m5 = pd.concat([au_array_40m5, int_ant_array_40m5_score], axis=1)

    print(au_int_array_20f1)

    '''
    print(au_array_20f1)
    print(au_array_20f2)
    print(au_array_20f3)
    print(au_array_20f4)

    print(au_array_30f1)
    print(au_array_30f2)
    print(au_array_30f3)

    print(au_array_40f1)
    print(au_array_40f2)
    print(au_array_40f3)
    print(au_array_40f4)

    print(au_array_50f1)
    print(au_array_50f2)
    print(au_array_50f3)

    print(au_array_20m1)
    print(au_array_20m2)
    print(au_array_20m3)
    print(au_array_20m4)
    print(au_array_20m5)

    print(au_array_30m1)
    print(au_array_30m2)
    print(au_array_30m3)

    print(au_array_40m1)
    print(au_array_40m2)
    print(au_array_40m3)
    print(au_array_40m4)
    print(au_array_40m5)
    '''

    print(int_ant_array_20f1)
    print(int_ant_array_20f2)
    print(int_ant_array_20f3)
    print(int_ant_array_20f4)

    print(int_ant_array_20f1_score)
    print(int_ant_array_20f2_score)
    print(int_ant_array_20f3_score)
    print(int_ant_array_20f4_score)

    print(int_ant_array_30f1)
    print(int_ant_array_30f2)
    print(int_ant_array_30f3)

    print(int_ant_array_30f1_score)
    print(int_ant_array_30f2_score)
    print(int_ant_array_30f3_score)

    print(int_ant_array_40f1)
    print(int_ant_array_40f2)
    print(int_ant_array_40f3)
    print(int_ant_array_40f4)

    print(int_ant_array_40f1_score)
    print(int_ant_array_40f2_score)
    print(int_ant_array_40f3_score)
    print(int_ant_array_40f4_score)

    print(int_ant_array_50f1)
    print(int_ant_array_50f2)
    print(int_ant_array_50f3)

    print(int_ant_array_50f1_score)
    print(int_ant_array_50f2_score)
    print(int_ant_array_50f3_score)

    print(int_ant_array_20m1)
    print(int_ant_array_20m2)
    print(int_ant_array_20m3)
    print(int_ant_array_20m4)
    print(int_ant_array_20m5)

    print(int_ant_array_20m1_score)
    print(int_ant_array_20m2_score)
    print(int_ant_array_20m3_score)
    print(int_ant_array_20m4_score)
    print(int_ant_array_20m5_score)

    print(int_ant_array_30m1)
    print(int_ant_array_30m2)
    print(int_ant_array_30m3)

    print(int_ant_array_30m1_score)
    print(int_ant_array_30m2_score)
    print(int_ant_array_30m3_score)

    print(int_ant_array_40m1)
    print(int_ant_array_40m2)
    print(int_ant_array_40m3)
    print(int_ant_array_40m4)
    print(int_ant_array_40m5)

    print(int_ant_array_40m1_score)
    print(int_ant_array_40m2_score)
    print(int_ant_array_40m3_score)
    print(int_ant_array_40m4_score)
    print(int_ant_array_40m5_score)


'''
### F4
    start_time_f4 = d_20f4_dump['end(system)[ms]'].valuesd_20f1_dump['AU01_c_mean'].values
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