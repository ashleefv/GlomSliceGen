# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:51:17 2017

Midpoint Circle Algorithm

@author: Steve
"""

import numpy as np


def CircleDraw(diameter, fill):
    radius = (diameter+1)/2.0
    
    
    
    output = np.zeros((int(radius*2-1), int(radius*2-1)))
    
    x = np.ceil(radius - 1)
    y = 0
    dx = 1
    dy = 1
    err = dx - int(radius * 2)
    x0 = radius - 1
    y0 = radius - 1
    
    while(x >= y):
        output[int(np.floor(x0 + x)), int(np.floor(y0 + y))] = 1
        output[int(np.floor(x0 + y)), int(np.floor(y0 + x))] = 1
        output[int(np.ceil(x0 - y)), int(np.floor(y0 + x))] = 1
        output[int(np.ceil(x0 - x)), int(np.floor(y0 + y))] = 1
        output[int(np.ceil(x0 - x)), int(np.ceil(y0 - y))] = 1
        output[int(np.ceil(x0 - y)), int(np.ceil(y0 - x))] = 1
        output[int(np.floor(x0 + y)), int(np.ceil(y0 - x))] = 1
        output[int(np.floor(x0 + x)), int(np.ceil(y0 - y))] = 1
        
        if(err <= 0):
            y += 1
            err += dy
            dy += 2
            
        if(err > 0):
            x -= 1
            dx += 2
            err += (-radius * 2) + dx
            
    if fill:
        for i in range(len(output)):
            points = np.where(output[i,:])[0]
            if len(points) > 2:
                continue
            for j in range(points[0],points[1]):
                output[i,j] = 1
                
    return output
    
if __name__ == '__main__':
    diameter = 6
    fill = 1
    output = CircleDraw(diameter, fill)
        