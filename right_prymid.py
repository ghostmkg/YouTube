# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:24:56 2024

@author: Grow With Code
"""

  
rows = int(input())  
 
for i in range(0, rows):    
  
    for j in range(0, i + 1):    
        print("*", end=' ')    
  
    print(" ")    
   
for i in range(rows , 0, -1):    
    for j in range(0, i - 1):     
        print("*", end=' ')    
    print(" ")  
