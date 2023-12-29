# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:42:29 2023

@author: Grow With Code
"""

import turtle
 
t = turtle.Turtle()
def ring(col, rad):
    t.fillcolor(col)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    
t.up()
t.setpos(-65, 95)
t.down
ring('black', 55)
t.up()
t.setpos(65, 95)
t.down()
ring('black', 55)
t.up()
t.setpos(0, 50)
t.down()
ring('white', 85)
t.up()
t.setpos(-42, 103)
t.down
ring('black', 28)
t.up()
t.setpos(42, 103)
t.down()
ring('black', 28)
t.up()
t.setpos(-42, 105)
t.down()
ring('white', 14)
t.up()
t.setpos(42, 105)
t.down()
ring('white', 14)
t.up()
t.setpos(0, 93)
t.down
ring('black', 5)
t.up()
t.setpos(0, 93)
t.down()
t.right(90)
t.circle(5, 180)
t.up()
t.setpos(0, 93)
t.down()
t.left(360)
t.circle(5, -180)
t.hideturtle()