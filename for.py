# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:20:59 2022

@author: Willirin
"""
switch=[]
lista=["R1","R2","R3","R4","R5","S1","S2"]
for item in lista:
    if "S" in item:
        switch.append(item)
print(switch)