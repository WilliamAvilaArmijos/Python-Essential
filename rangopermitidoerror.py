# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:49:32 2022

@author: Willirin
"""

def readint(prompt, min, max):
    while(True):
        try:
            n=int(input(prompt))
            assert n>=min and n<=max
            return n
           
        except ValueError:
            print("Ingresar solo numeros")
        except :
            print("Esta fuera del rango")
            
     
        
v = readint("Ingrese un número entre -10 y 10: ", -10, 10)
print("El número es: ",v)