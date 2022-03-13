# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:26:16 2022

@author: craig
"""

number = int(input("Which number do you want to check? "))

number = number % 2
if number == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")