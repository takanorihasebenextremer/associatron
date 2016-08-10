#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:26:36 2016

@author: takanori.hasebe
"""

"""
このプログラムは
Cでつくる脳の情報システムP.79を参照に
数字１のみを記憶行列(Matrix)に記憶し
入力から記憶パターンを想起している
"""

import numpy as np
import associatronfunction as af

arr1 = np.array([-1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1,-1, -1, 1, -1, -1,-1, -1, 1, -1, -1])

arr1_T = np.vstack(arr1)

"""
このMatrixは数字１のみを記憶している。 arr1に近いものを入力するとarr1が想起される。
"""
Matrix = arr1_T * arr1

recall = af.phi_r(np.dot(arr1, af.phi_M(Matrix)))

if np.array_equiv(recall, arr1):
    
    print("1")