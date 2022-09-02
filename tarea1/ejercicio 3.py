# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:54:59 2022

@author: luana
"""

#%% EJERCICIO 3 

import numpy as np
import random 

#número de observaciones= 10000

#fijamos una semilla
np.random.seed(175)

#creamos 5 variables, las cuales tienen una distribución uniforme de entre [0,1]    

x1 = np.random.rand(10000) 
x2 = np.random.rand(10000) 
x3 = np.random.rand(10000) 
x4 = np.random.rand(10000)
x5 = np.random.rand(10000) 
e = np.random.normal(0,1,10000) # normal distribution mean = 0 and sd = 1

# El modelo sin contar a la explicativa x5 sería: 
# Y = b1*x1 + b2*x2 + b3*x3 + b4*x4 + e

Y = 0.7*x1 + 1.6*x2 + 0.3*x3 + 1.8*x4 + e

#Con un n=10

X = np.column_stack((np.ones(10000),x1,x2,x3,x4,x5))
print(X)

beta = np.linalg.inv(X.T @ X) @ ((X.T) @ Y )
print(beta)

n = list(10,50,80,120,200,500,800)
w1= random.sample( range(10000) , 10 )
print(w1)
