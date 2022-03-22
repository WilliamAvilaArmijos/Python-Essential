# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:37:18 2022

@author: Willirin
"""
lista=[] 
file=open("devices.txt")
for item in file:
    item=item.strip()
    lista.append(item)
     
file.close()
print (lista)