# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:10:10 2022

@author: Willirin
"""


file=open("devices.txt","a")
while True:
    newItem=input("Enter device name: ")
    if newItem=="exit":
        print("All done! ")
        break
    file.write(newItem+ "\n")
file.close()