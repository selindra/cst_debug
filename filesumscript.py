#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:43:15 2021

@author: selin
"""
import matplotlib.pyplot as plt


def filesumscript(filename):
    with open(filename) as f:
        s=0
        for line in f:
            line=line.split()
            if len(line)>7:
                s+=int(line[4])
    return s

sum = []
for i in range(0,238):   
    i+=1
    filename = '/Users/selin/Documents/git/cst_debug/file{}.txt'.format(i)
    x=filesumscript(filename)/10e+8
    sum.append(x)
    
plt.plot(sum, 'palevioletred')           
plt.xlabel('File number')
plt.ylabel('Gb memory')