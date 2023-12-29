# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 07:07:35 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(-30,120)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor('red') 
  
t.begin_fill()

t.forward(120)

t.left(90)

t.forward(40)

t.left(90)

t.forward(160)

t.left(90)

t.forward(230)

t.left(90)

t.forward(40)

t.left(90)

t.forward(90)

t.right(90)

t.forward(80)

t.left(90)

t.forward(40)

t.left(90)

t.forward(80)

t.right(90)

t.forward(60)

t.end_fill() 
