# CircleDrop
# J Eisenmann

# 3 parallel lists for holding info about the circles we're going to drop
# (these lists should always be the same size so they stay parallel)
diameters = []
positions = []
colors = []

def setup():
    # the usual size
    size(400,400)
    # set the stroke thickness for the whole sketch
    strokeWeight(2)
    
def draw ():
    # clear the screen with solid gray every frame
    background(150)
    # iterate over the positions list and get an index 'i' (using 'enuemrate') for finding the corresponding color and diameter
    for i, p in enumerate(positions):
        # find the distance between the mouse and this position
        d = dist( mouseX, mouseY, p.x, p.y )
        # if the distance is less than half the diameter of this circle (corresponding diameter found with index 'i')
        if( d < diameters[i]*0.5 ):
            # red fill and white stroke
            fill(255, 0, 0)
            stroke(255)
        # otherwise, if the mouse is not on this circle...
        else:
            # use the circle's own random fill color found in the parallel list 'colors'
            fill(colors[i])
            stroke(0)
        # now that the colors are set and we can use this position 'p' and the corresponding diameter at index 'i' to draw the circle
        ellipse (p.x, p.y, diameters[i], diameters[i])

def mousePressed ():
    # the mouse has been pressed!  So add a PVector that wraps up the X and Y location into one thing to the list of positions
    positions.append(PVector(mouseX,mouseY))
    # also add a random diameter
    diameters.append(int(random(10,200)))
    # and a random color
    r = random(255)
    g = random(255)
    b = random(255)
    colors.append(color(r,g,b))
    # since we are appending one thing to each list, the lists will stay in sync 

def keyPressed ():
    # iterate through the positions again (just copied this loop from the draw() function above)
    for i, p in enumerate(positions):
        # find the distance to the mouse
        d = dist( mouseX, mouseY, p.x, p.y )
        # if mouse over the circle
        if d < diameters[i]*0.5:
            # and if the up arrow key was pressed
            if keyCode == UP:
                # increase the diameter at index 'i'
                diameters[i] += 5
            # or if the down arrow key was pressed
            elif keyCode == DOWN:
                # decrease the diameter at index 'i'
                diameters[i] -= 5
            # make sure the diameter is limited to stay between 5 and 250
            diameters[i] = constrain(diameters[i], 5, 250)

