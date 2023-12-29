# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:08:57 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(-30,0)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor('red') 
  
t.begin_fill()

t.forward(50)

t.right(90)

t.forward(80)

t.right(90)

t.forward(70)

t.right(180)

t.circle(90,-180)

t.back(110)

t.right(90)

t.forward(40)

t.left(90)

t.forward(110)

t.circle(130,180)

t.forward(110)

t.left(90)

t.forward(160)

t.left(90)

t.forward(90)

t.left(90)

t.forward(40)

t.end_fill() 

turtle.done()
