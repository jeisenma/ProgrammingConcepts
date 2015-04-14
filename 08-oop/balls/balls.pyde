# J Eisenmann 2013 
# jeisenma@accad.osu.edu

from Ball import *

balls = []					# list to hold all the balls
mouseDown = False			# keeps track of whether or not the mouse is down
mouseDownPos = PVector()	# keeps track of where the mouse was initially pressed	

# set up the world
def setup():
    size(400,400)

# update each ball's state and draw it every frame
def draw():
    # draw the scene
    background(150)		   # refresh the background
    strokeWeight(2)
    
    # if dragging, show slingshot line
    if mouseDown:
        line(mouseDownPos.x, mouseDownPos.y, mouseX, mouseY) 
    
    # update and draw all the balls
    for b in balls:
        b.update(balls)
        b.display()

def mousePressed():
    global mouseDown, mouseDownPos
    mouseDown = True
    # memorize where the mouse was clicked
    mouseDownPos = PVector(mouseX, mouseY)

def mouseReleased():
    global mouseDown
    mouseDown = False
    # random radius for each ball
    radius = round(map(random(1),0,1,10,30))
    # the location of the ball
    position = PVector(mouseX,mouseY)
    # use the mouse pressed position that we memorized earlier to generate an initial velocity
    velocity = PVector(mouseDownPos.x-mouseX, mouseDownPos.y-mouseY)
    # scale the velocity down so it isn't too fast
    velocity.mult(0.2)
    # make a ball
    balls.append( Ball( radius, position, velocity ) )



