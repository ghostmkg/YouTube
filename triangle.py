# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:21:42 2024

@author: Grow With Code
"""

row = int(input())

temp = row - 1


for i in range(0, row):

	for j in range(0, temp):
		print(end=" ")

	temp = temp - 1

	for j in range(0, i+1):

		print("* ", end="")

	print("\r")
