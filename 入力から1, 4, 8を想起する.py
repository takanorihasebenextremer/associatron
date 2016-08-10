#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:19:40 2016

@author: takanori.hasebe
"""

"""
このプログラムは
記憶行列(Matrix)に
1, 4, 8を記憶している。

入力から異なった
パターンを想起する
"""

import numpy as np
import associatronfunction as af
from matplotlib import pyplot as plt
import seaborn as sns
import random as rd
arr = np.array([])

arr1 = np.array([-1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1,-1, -1, 1, -1, -1,-1, -1, 1, -1, -1])

arr4 = np.array([-1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1])

arr8 = np.array([-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1])

#arr_rd = np.random.randint(-1, 2, 25)

arr_open = np.loadtxt("re8.txt", dtype = int)
arr_rd = arr_open[5]

arr1_T = np.vstack(arr1)
arr4_T = np.vstack(arr4)
arr8_T = np.vstack(arr8)

arr_re_1 = np.array([])
arr_re_4 = np.array([])
arr_re_8 = np.array([])

"""
このMatrixは数字1, 4, 8を自己相関をたすことによって記憶している。
"""
Matrix = arr1_T * arr1 + arr4_T * arr4 + arr8_T * arr8

"""
#記憶行列を可視化
sns.heatmap(Matrix, annot = True, cmap = 'Blues')
sns.plt.show()
"""


#入力行列を可視化
sns.heatmap(arr_rd.reshape(5,5), annot = True, cmap = "Blues")
sns.plt.show()

recall = af.phi_r(np.dot(arr_rd, af.phi_M(Matrix)))


#以下はランダムな入力から１, 4, 8のどれかを想起した時に
#ランダムな配列をtxt形式で保存するものである。
"""
for i in range(200):

    arr_rd = np.random.randint(-1, 2, 25)
    recall = af.phi_r(np.dot(arr_rd, af.phi_M(Matrix)))
    
    
    if np.array_equal(recall, arr1):
        
        if np.array_equal(arr_re_1, arr):
            
            arr_re_1 = arr_rd
        else:
            
            arr_re_1 = np.vstack((arr_re_1, arr_rd))
        
    elif np.array_equal(recall, arr4):
        
        if np.array_equal(arr_re_4, arr):
            
            arr_re_4 = arr_rd
        else:
            
            arr_re_4 = np.vstack((arr_re_4, arr_rd))
        
    elif np.array_equal(recall, arr8):
        
        if np.array_equal(arr_re_8, arr):
            
            arr_re_8 = arr_rd
        else:
            
            arr_re_8 = np.vstack((arr_re_8, arr_rd))

np.savetxt('re1.txt', arr_re_1, fmt = "%d")
np.savetxt('re4.txt', arr_re_4, fmt = "%d")
np.savetxt('re8.txt', arr_re_8, fmt = "%d")
"""

#想起行列を可視化
sns.heatmap(recall.reshape(5,5), annot = True, cmap = "Blues")
sns.plt.show()


"""
#記憶パターンを可視化
sns.heatmap(arr1.reshape(5,5), annot=True, fmt='g', cmap='Blues')
sns.plt.show()
sns.heatmap(arr4.reshape(5,5), annot=True, fmt='g', cmap='Blues')
sns.plt.show()
sns.heatmap(arr8.reshape(5,5), annot=True, fmt='g', cmap='Blues')
sns.plt.show()
"""



