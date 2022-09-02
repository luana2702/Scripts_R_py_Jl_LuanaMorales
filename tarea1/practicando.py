# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:54:17 2022

@author: luana
"""

#%% EJERCICIO 3 (LOOPS OLS)

import random
import numpy as np
import math

from scipy.stats import t # t - student 
import pandas as pd 


np.random.seed(175)

x1 = np.random.rand(10000) # uniform distribution  [0,1]
x2 = np.random.rand(10000) # uniform distribution [0,1]
x3 = np.random.rand(10000) # uniform distribution [0,1]
x4 = np.random.rand(10000) # uniform distribution [0,1]
x5 = np.random.rand(10000) # uniform distribution [0,1]
e = np.random.normal(0,1,10000) # normal distribution mean = 0 and sd = 1
z = np.random.rand(10000)

# Poblacional regression (Data Generating Process GDP)


Y = 1 + 0.8*x1 + 1.2*x2 + 0.5*x3 + 1.5*x4 + 0.6*x5 + e

X = np.column_stack((np.ones(10000),x1,x2,x3,x4,x5))

def ols(M,Y, standar = True, Pvalue = True , instrumento = None, index = None):

    if standar and Pvalue and (instrumento is None)  and (index is None) :
        
         beta = np.linalg.inv(X.T @ X) @ ((X.T) @ Y ) 
        
         y_est =  X @ beta 
         n = X.shape[0]
         k = X.shape[1] - 1 
         nk = n - k    
         sigma =  sum(list( map( lambda x: x**2 , Y - y_est)   )) / nk 
         Var = sigma*np.linalg.inv(X.T @ X)
         sd = np.sqrt( np.diag(Var) )
         t_est = np.absolute(beta/sd)
         pvalue = (1 - t.cdf(t_est, df=nk) ) * 2
         df = pd.DataFrame( {"OLS": beta , "standar_error" : sd ,
                             "Pvalue" : pvalue} )    
         
    
    elif (not instrumento is None) and (not index is None) :
        
        beta = np.linalg.inv(X.T @ X) @ ((X.T) @ Y )
        
        index = index  - 1 
        Z = X
        Z[:,index] = z
        beta_x = np.linalg.inv(Z.T @ Z) @ ((Z.T) @ X[:,index] ) 
        x_est  = Z @ beta_x
        X[:,index] = x_est
        beta_iv = np.linalg.inv(X.T @ X) @ ((X.T) @ Y )
        df = pd.DataFrame( {"OLS": beta , "OLS_IV" : beta_iv})  

    return df



ols(X,Y)

ols(X,Y,instrumento = z, index = 2)