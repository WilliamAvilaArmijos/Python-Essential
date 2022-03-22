# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:49:43 2022

@author: Willirin
"""

try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
    
except ZeroDivisionError:
    print("ERROR")
except ValueError:
    print("ERRORa")
except:
    print("ERROR")
print("END")