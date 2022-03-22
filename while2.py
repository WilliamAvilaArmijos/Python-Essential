# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:21:04 2022

@author: Willirin
"""

num=input("Ingrese el número al que contaré: ")
num=int(num)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>num:
        break