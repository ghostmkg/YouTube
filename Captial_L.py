# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 08:53:00 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(-70,170)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor('red') 

t.begin_fill()

t.forward(50)

t.right(90)

t.forward(230)

t.left(90)

t.forward(130)

t.right(90)

t.forward(50)

t.left(-90)

t.forward(180)

t.right(90)

t.forward(280)

t.end_fill() 

turtle.done()
