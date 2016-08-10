# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 14:22:17 2016

@author: takanori.hasebe
"""

"""
このプログラムは
アソシアトロンに用いられる
関数全般を記述している。
"""


"""
量子化関数φ
"""
def phi_M(Matrix):
    
    for i in range(0, len(Matrix)):
        for j in range(0, len(Matrix[i])):
            
            if Matrix[i][j] < 0:
                
                Matrix[i][j] = -1
            elif Matrix[i][j] == 0:
                
                Matrix[i][j] = 0
            else:
                
                Matrix[i][j] = 1
                
    return Matrix
    
def phi_r(row):
    
    for i in range(0, len(row)):
        
        if row[i] < 0:
            
            row[i] = -1
        elif row[i] == 0:
            
            row[i] = 0
        else:
            
            row[i] = 1
            
    return row

