# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:19:55 2021

@author: Francis
"""

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw


xdots=800   
ydots=600

colores=256

xmin=-2.5
xmax=1.5
ymin=-1.5
ymax=1.5

iteraciones = 20
threshold=50.


p0 = np.linspace(xmin,xmax,xdots)        
q0 = np.linspace(ymin,ymax,ydots)    

a,b = np.meshgrid(p0,q0)    

c = a + b*1j
z = np.zeros_like(c)

#esto es lo que hay que iterar unas cuantas veces para que se forme el fractal.
z = z**2 + c

#mandelbrot_set = (1-(abs(z)<threshold)*1)*255
diverge = abs(z)> 20


mandelbrot_set = diverge

plt.figsize=(xdots,ydots)
plt.imshow(mandelbrot_set, extent=[-2, 1, -1.5, 1.5])
#plt.gray()
#plt.show()

"""
im = Image.new('RGB',(xdots,ydots),(0,0,0))

draw = ImageDraw.Draw(im) #Permite pintar en la imagen anterior.

for y in range (0,ydots):
    for x in range(0,xdots):
        draw.point([x,y],(mandelbrot_set[x][y],mandelbrot_set[x][y],mandelbrot_set[x][y]))

#im = Image.fromarray(mandelbrot_set.T,)
im.save('mandel.png','png')

"""
