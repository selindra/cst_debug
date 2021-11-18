#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:24:48 2021

@author: selin
"""

with open('mylog.txt') as f:
    filenum=0
    for line in f:    
        if ".:" in line:
            filenum+=1
            filename = 'file{}.txt'.format(filenum)
            with open(filename, 'a') as file:
                file.write(line)
        else:
            filename = 'file{}.txt'.format(filenum)
            with open(filename, 'a') as file:
                file.write(line)


