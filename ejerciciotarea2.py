# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:53:50 2022

@author: Willirin
"""

def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def obtener_dias_del_mes(mes: int, anio: int) -> int:
    if mes in [4, 6, 9, 11]:
        return 30
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    else:        
        return 31

mes=int(input("Ingrese el mes: "))
if mes>12 or mes<1:
        raise Exception("El mes ingresado no existe")
anio = int( input("Ingrese el año: "))
dias = obtener_dias_del_mes(mes, anio)
print("El mes ", mes," en el año ",anio," tiene ",dias," días")