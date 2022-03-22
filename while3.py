# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:28:26 2022

@author: Willirin
"""

while True:
    x=input("Ingrese el número al que contaré: ")
    if x == 'q' or x=='quit':
        break  
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break