# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:55:37 2020

@author: vishal
"""

import math
a=int(input("Enter  value of A in quadratic equation"))
b=int(input("Enter  value of B in quadratic equation"))
c=int(input("Enter  value of C in quadratic equation"))
dis=(b*b)-(4*a*c)
if(dis > 0):
    root1 = (-b + math.sqrt(dis)) / (2 * a)
    root2 = (-b - math.sqrt(dis)) / (2 * a)
    print(f"Two Distinct Real Roots Exists: root1 = {root1} and root2 = {root2}")
elif(dis == 0):
    root1 = root2 = -b / (2 * a)
    print(f"Two Equal and Real Roots Exists: root1 = {root1} and root2 = {root2}")
else:    
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-dis) / (2 * a)
    print(f"Two Distinct Complex  Roots Exists: root1 = {root1} and root2 = {root2}")