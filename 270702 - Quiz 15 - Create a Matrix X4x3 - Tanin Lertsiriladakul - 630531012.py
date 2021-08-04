# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:34:22 2021

@author: Tanin Lertsiriladakul 630531012
"""
#Quiz 15 : Creat a Matrix X4*3
import numpy as np
m = np.array([[1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]]).reshape(4,3)
print(m)
m[2,:] #array([7, 8, 9])
m[2:] #array([[ 7,  8,  9],
       #      [10, 11, 12]])

#Other methods
import numpy as np
m = np.arange(1,13).reshape((4, 3))
print(m)
m[2,:] 
m[2:] 