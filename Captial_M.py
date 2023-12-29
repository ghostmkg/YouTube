# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 08:19:06 2023

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

t.fillcolor("red") 

t.begin_fill()

t.forward(70)

t.right(45)

t.forward(110)

t.left(90)

t.forward(110)

t.right(45)

t.forward(70)

t.right(90)

t.forward(280)

t.left(-90)

t.forward(70)

t.right(90)

t.forward(210)

t.left(135)

t.forward(110)

t.right(90)

t.forward(110)

t.left(135)

t.forward(210)

t.left(-90)

t.forward(70)

t.right(90)

t.forward(280)

t.end_fill()

turtle.done()
