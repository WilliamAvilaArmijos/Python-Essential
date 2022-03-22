# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:37:56 2022

@author: Willirin
"""

def anio(n):
    if (n%4==0 and n%100!=0 or n%400==0):
        return True
    else:
        return False

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr,"-> ",end="")
    result = anio(yr)
    if result == True:
        print("OK")
    else:
        print("Failed")

