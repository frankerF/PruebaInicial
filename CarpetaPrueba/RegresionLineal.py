# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:58:27 2022

@author: Francis
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston

boston = load_boston()
X = np.array(boston.data[:,5])
Y = np.array(boston.target)

plt.scatter(X,Y,alpha=0.3)
#Se agrega  una dimensión más para el termino independiente.
X2 = np.array([np.ones(X.size),X]).T

#Calcula minimos cuadrados.  Devuelve B[0] termino independiente , B[1] pendiente  
#Para la ecuación de la recta Y=B[1]+ B[0] 
B = np.linalg.inv(X2.T @ X2) @ X2.T @ Y

#[4,9] punto iniciales en x, A los puntos Y se les calcula la ecuación
#
plt.plot([4,9],[B[0]+B[1]*4,B[0]+B[1]*9],c="red")

plt.show()
