# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:31:49 2022

@author: Willirin
"""

def direct(ciudad,barrio,calle):
    print("La direccion de la entrega es: ")
    print("Ciudad: " , ciudad)
    print("La referencia es: ", barrio)
    print("La entrega sera en la calle: ", calle,"\n"*2)
    
ca=input("Ingrese la calle: ")
ci=input("Ingrese la ciudad: ")
ba=input("Ingrese el barrio o sector: ")
print("\n"*2)
direct(ci, ba, ca)
    