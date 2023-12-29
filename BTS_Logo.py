# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 08:44:30 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()

window = turtle.Screen()

window.bgcolor('black')

t.penup()

t.setpos(-190,230)

t.pendown()

t.pensize(10)

t.color("white")

t.fillcolor("white") 

t.begin_fill()

t.right(40)

t.forward(110)

t.right(50)

t.forward(250)

t.right(70)

t.forward(90)

t.right(110)

t.forward(350)

t.end_fill()

t.penup()

t.setpos(40,230)

t.pendown()

t.begin_fill()

t.left(-180)

t.forward(350)

t.left(-105)

t.forward(110)

t.right(75)

t.forward(250)

t.right(55)

t.forward(125)

t.end_fill()

t.penup()

t.setpos(-155,-200)

t.pendown()

t.left(-35)

t.circle(25, 180)

t.forward(30)

t.left(90)

t.forward(100)

t.left(90)

t.forward(30)

t.circle(25,180)

t.forward(30)

t.penup()

t.setpos(-35,-155)

t.pendown()

t.forward(80)

t.back(40)

t.left(90)

t.forward(95)

t.penup()

t.setpos(35,-155)

t.pendown()

t.right(90)

t.forward(25)

t.circle(25, 180)

t.left(175)

t.circle(25, -180)

t.right(-5)

t.back(25)

turtle.done()
