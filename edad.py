# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:37:56 2022

@author: Willirin
"""

nom=input("ingrese tu nombre:")
ape=input("ingrese tu apellido:")
loca=input("ingrese tu domicilio:")
edad=int(input("ingrese tu edad:"))
if edad>=1 and edad<=4:
    print("Es un bebé")
elif edad>=5 and edad<=12:    
    print("Es un niño")
elif edad>=13 and edad<=18:    
    print("Es un adolescente")
elif edad>=19 and edad<=29:    
    print("Es un joven")
elif edad>=30 and edad<=70:    
    print("Es un adulto")
else:
    print("Es de la tercera edad")
space=" "
print("Su nombre es: "+nom+" su apellido es: "+ape+" domicilio: "+loca+" edad: ",edad
     )