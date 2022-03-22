# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:14:49 2022

@author: Willirin
"""

def fibo(n):
    a,b=0,1
    while a<=n:
        print(a, end=' ')
        a,b=b, a+b
    
    print("\n"*2)
       

