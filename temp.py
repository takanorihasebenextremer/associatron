#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:39:34 2016

@author: takanori.hasebe
"""

import numpy as np
import seaborn as sns

arr1 = np.loadtxt("re1.txt", dtype=int)

print(arr1[3])
"""
for i in range(0, len(arr1)):
    
    sns.heatmap(arr1[i].reshape(5, 5), annot = True, cmap = "Blues")
    sns.plt.show()
"""