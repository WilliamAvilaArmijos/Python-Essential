# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:28:05 2022

@author: Willirin
"""

def isPrime(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

for i in range (1,20):
    if isPrime(i+1):
        print(i+1, end=" ")
        
print(" ")