# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:25:47 2022

@author: Willirin
"""

acl=int(input("Ingrese el # del ACL: "))
if acl>=1 and acl<=99:
    print("La ACL es Standar")
elif acl>=100 and acl<=199:    
    print("La ACL es Extendida")
else:
    print("El # ingresado no es de ACL normal")