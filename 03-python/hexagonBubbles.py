# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# import the turtle module (from the TK library) -- discuss alternatives
from turtle import *

def hexagon(x,y,r):
    """function to draw a hexagon at point x,y with side length r"""
    up()
    goto(x,y)
    down()
    for i in range(6):
        forward(r)
        right(60)

# set up the drawing window
setup()

# so we don't have to wait forever"""
speed("fastest")

# draw hexagon bubbles
for i in range(1,10):
    hexagon(40*i, 4*i*i, 4*i)

# when to stop window: on mouse click
exitonclick()
