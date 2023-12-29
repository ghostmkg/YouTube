# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:15:30 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(-50,-150)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor('red') 

t.begin_fill()

t.back(40)

t.circle(120, -180)

t.back(40)

t.circle(120, -180)

t.end_fill() 

t.penup()

t.setpos(-50,-100)

t.fillcolor('black') 

t.begin_fill()

t.pendown()

t.back(30)

t.circle(75, -180)

t.back(30)

t.circle(75, -180)

t.end_fill() 

turtle.done()
