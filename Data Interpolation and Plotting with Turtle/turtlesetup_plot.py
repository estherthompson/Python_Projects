# This code sets up the turtle for use in 231
# By Richard Zhao
# This file should not be edited in any way
# Your code should be created in a new, separate file, and
# import this file by using: from turtlesetup_plot import *

import sys
if "turtle" in sys.modules:
    print("Do not import turtle yourself.")
    sys.exit()

import turtle
# Setting up the turtle environment
WIDTH = 1024
HEIGHT = 768
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.screensize(WIDTH, HEIGHT)
screen.setworldcoordinates(1900, 0, 2050, 5)
screen.delay(delay=0)
screen.title("Birth Rate Plot")
t.shape("turtle")
t.up()
t.speed(0)
t.setposition(1910, 0.1)
t.write("1910")
t.setposition(1910, 0.2)
t.down()
t.forward(130)
t.up()
t.setposition(2040, 0.1)
t.write("2040")
t.setposition(1906, 0.2)
t.write("0.2")
t.setposition(1910, 0.2)
t.down()
t.left(90)
t.forward(4.5)
t.up()
t.setposition(1906, 4.5)
t.write("4.5")
t.setposition(1910, 0.2)
t.right(90)
