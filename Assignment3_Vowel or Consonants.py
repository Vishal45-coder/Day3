# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:27:01 2020

@author: vishal
"""

ch=str(input("enter a character"))
if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I'
       or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    print(f"{ch} is vowel")
else:
    print("consonant")