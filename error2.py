# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:09:41 2022

@author: Willirin
"""

try:
    y=1/0
    
except ZeroDivisionError:
    print("ERROR zero division")
except ArithmeticError:
    print("ERROR aritmetico")

print("END")