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


for i in range(0,239):
    sum=[]
    i+=1
    filename = '/Users/selin/Documents/work/file_script/file{}.txt'.format(i)
    x=filesumscript(filename)
    sum = sum.append(x)
    
                 
