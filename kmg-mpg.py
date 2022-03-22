# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:46:41 2022

@author: Willirin
"""

def mpgtol100km(a):
    print(235.215/a)
    return a

c=float(input("Ingrese la milla/galon: "))
print("La transformación de milla/galon a litro/100km es igual a: ")
mpgtol100km(c)


def l100kmtompg(b):
    print(235.215/b)
    return b

d=float(input("Ingrese la litro/100km: "))
print("La transformación de litro*100km a milla/galon es igual a: ")
mpgtol100km(d)
