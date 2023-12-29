# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 08:56:11 2023

@author: mgosh
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(-190,170)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor("yellow") 

t.begin_fill()

t.forward(150)

t.right(45)

t.forward(110)

t.left(90)

t.forward(110)

t.right(45)

t.forward(150)

t.right(90)

t.forward(280)

t.left(-90)

t.forward(150)

t.right(90)

t.forward(130)

t.left(135)

t.forward(110)

t.right(90)

t.forward(110)

t.left(135)

t.forward(130)

t.left(-90)

t.forward(150)

t.right(90)

t.forward(280)

t.end_fill()

t.penup()

t.pensize(25)

t.color("red")

t.setpos(65,20)

t.pendown()

t.right(55)

t.forward(160)

t.back(75)

t.right(120)

t.forward(120)

t.penup()

t.setpos(165,20)

t.pendown()

t.left(45)

t.forward(80)

t.left(115)

t.forward(170)

turtle.done()
