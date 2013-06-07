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

# draw hexagon
hexagon(0, 0, 100)

# when to stop window: on mouse click
exitonclick()
