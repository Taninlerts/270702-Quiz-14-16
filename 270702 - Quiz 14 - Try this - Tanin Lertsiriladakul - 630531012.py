# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:14:19 2021

@Auther : Tanin Lertsiriladakul 630531012
"""

#Quiz 14 : Try this
import numpy as np
from scipy.linalg import solve
A = np.array([[1.,2.],[3.,4.]])
b = np.array([1.,4.])
x = solve(A,b)
print(x)