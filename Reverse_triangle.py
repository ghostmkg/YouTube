# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:56:52 2024

@author: Grow With Code
"""

row = int(input())

for i in range(1, row+1):
    
    for j in range(i-1):
        
        print(' ', end='')
    
    for j in range(2*(row-i)+1):
        
        print('*', end='')
        
    print()
