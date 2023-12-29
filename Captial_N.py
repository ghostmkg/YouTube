# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 09:16:14 2023

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

t.forward(70)

t.right(55)

t.forward(250)

t.left(145)

t.forward(210)

t.right(90)

t.forward(70)

t.right(90)

t.forward(320)

t.right(90)

t.forward(70)

t.right(55)

t.forward(250)

t.left(145)

t.forward(210)

t.left(-90)

t.forward(70)

t.right(90)

t.forward(320)

t.end_fill() 

turtle.done()
