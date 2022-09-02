# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:36:42 2022

@author: luana
"""
import numpy as np

a = vector = list(np.arange(100))

b = vector = np.arange(100)

print(a)

print(b)

y = np.random.randint(-10, 10, 10)

print(y)

vector = list(np.arange(10))

vector = np.arange(10)
 
  
import pandas as pd 
  
# list of name, degree, score
var1 = np.random.rand(10000)
var2 = np.arange(0,10000)
var3 =  np.random.rand(10000)
var4 = np.arange(10,10000)

print(var4)

  
# dictionary of lists 
dict = {'v1': var1, 'v2': var2, 'v3': var3} 
    
df = pd.DataFrame(dict)

df.apply(np.sum, axis = 0)  # columna por columna 
df.apply(np.sum, axis = 1)  # fila por fila

df['nueva_var'] = df['v2'].apply(lambda x : x**99)
