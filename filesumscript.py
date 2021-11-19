#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:43:15 2021

@author: selin
"""
import matplotlib.pyplot as plt
import sys 

def filesumscript(filename):
    with open(filename) as f:
        s=0
        for line in f:
            line=line.split()
            if len(line)>7:
                s+=int(line[4])
    return s

def main():
    sum = []
    for file in sys.argv[1:]:   
        x=filesumscript(file)/10e+8
        sum.append(x)
        
    plt.plot(sum, 'red')           
    plt.xlabel('File number')
    plt.ylabel('Gb memory')
    plt.show()
    

#----------------------------------

if __name__ == '__main__':
    main()