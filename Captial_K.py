# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:40:14 2023

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

t.right(90)

t.forward(240)

t.right(-90)

t.forward(50)

t.left(90)

t.forward(110)

t.right(135)

t.forward(135)

t.right(-45)

t.forward(60)

t.left(135)

t.forward(165)

t.right(80)

t.forward(135)

t.left(125)

t.forward(60)

t.left(55)

t.forward(100)

t.right(147)

t.forward(80)

t.left(90)

t.forward(50)

t.end_fill() 

turtle.done()
