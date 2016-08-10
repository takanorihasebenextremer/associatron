# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:13:36 2016

@author: takanori.hasebe
"""
"""
このプログラムは
2×2のアソシアトロンである
3×3のアソシアトロンになる確率もあり
"""

import numpy as np
import associatronfunction as af

arr1 = np.array([1, 0, -1])
arr2 = np.array([0, -1, -1])
arr3 = np.array([1, -1, 1])

arr1_T = np.vstack(arr1)
arr2_T = np.vstack(arr2)
arr3_T = np.vstack(arr3)

M = np.array([])

M = arr1_T * arr1 + arr2_T * arr2 + arr3_T * arr3 

#print(M)

y = np.array([1, 0, -1])

print(af.phi_r(np.dot(y, af.phi_M(M))))


