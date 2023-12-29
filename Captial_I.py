# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:38:26 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(-150,170)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor('red') 

t.begin_fill()

t.forward(290)

t.right(90)

t.forward(50)

t.left(-90)

t.forward(115)

t.left(90)

t.forward(270)

t.left(90)

t.forward(115)

t.right(90)

t.forward(50)

t.left(-90)

t.forward(290)

t.right(90)

t.forward(50)

t.right(90)

t.forward(115)

t.left(90)

t.forward(270)

t.left(90)

t.forward(115)

t.left(-90)

t.forward(50)

t.end_fill() 

turtle.done()
