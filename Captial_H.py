# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:59:12 2023

@author: mgosh
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

t.forward(90)

t.right(90)

t.forward(100)

t.left(90)

t.forward(40)

t.right(-90)

t.forward(240)

t.left(90)

t.forward(40)

t.left(90)

t.forward(100)

t.right(90)

t.forward(90)

t.right(90)

t.forward(100)

t.right(-90)

t.forward(40)

t.left(90)

t.forward(240)

t.left(90)

t.forward(40)

t.left(90)

t.forward(100)

t.end_fill() 

turtle.done()