# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:58:15 2023

@author: Grow With Code
"""

import turtle

t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor('black')
#window.setup(width=1000, height=1000)

def outer_circle():
	t.setposition(0, -380)
	t.pendown()
	t.begin_fill()
	t.color('red')
	t.pencolor('white')
	t.circle(380)
	t.end_fill()
	t.penup()

def inner_circle():
	t.pensize(2)
	t.setposition(0, -320)
	t.pendown()
	t.begin_fill()
	t.color('black')
	t.circle(300)
	t.end_fill()
	t.penup()

def draw_A():
	t.setposition(0, -50)
	t.pendown()
	t.begin_fill()
	t.color('red')
	t.pensize(10)
	t.pencolor('white')
	t.forward(43)
	t.backward(123)
	t.left(60)
	t.backward(370)
	t.right(60)
	t.backward(120)
	t.right(117)
	t.backward(950)
	t.right(63)
	t.backward(110)
	t.right(90)
	t.backward(607)
	t.right(90)
	t.backward(110)
	t.right(90)
	t.backward(82)
	t.end_fill()
	t.penup()

def draw_triangle():
	t.pensize(10)
	t.setposition(50, 30)
	t.pendown()
	t.begin_fill()
	t.color('black')
	t.pencolor('white')
	t.right(90)
	t.forward(110)
	t.right(115)
	t.forward(270)
	t.right(154.8)
	t.forward(245)
	t.end_fill()

def draw_arrow():
    
    t.backward(80)
    t.left(42)
    t.forward(150)
    t.right(83)
    t.forward(170)

def avenger():
	t.speed(10)
	t.pensize(10)
	t.penup()
	outer_circle()
	inner_circle()
	draw_A()
	draw_triangle()
	draw_arrow()
	
    
avenger()
t.penup()
t.setposition(170, -30)
t.pensize(20)
t.pencolor("white")
t.write("venger",font=('Kalam',40,'bold'))
t.hideturtle()
t.done()

