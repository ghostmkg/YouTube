# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:06:01 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(30,170)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor('red') 

t.begin_fill()

t.forward(60)

t.right(90)

t.forward(220)

t.left(180)

t.circle(120,-180)

t.left(90)

t.forward(60)

t.right(90)

t.circle(60,180)

t.forward(220)

t.end_fill() 

turtle.done()
