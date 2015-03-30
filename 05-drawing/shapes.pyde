# J Eisenmann 2013 
# jeisenma@accad.osu.edu

def setup():
    size(400,400)

def draw():
    # every 30 frames, draw another random shape
    if frameCount % 30 == 0:	
    # pick a number between 0 and 6, use that to decide which shape to draw
    whichShape = int(random(0,6))
    # make the shape a random size between 10 and 50
    size = random(10, 50)
    # fill our shape with a random RGB color
    shade = color( random(255), random(255), random(255) )
    fill(shade)
    # pick a random line thickness
    strokeWeight( int(random(1,4)) )
    
    # draw at the current location of the mouse 
    translate(mouseX, mouseY)
    # rotate by a random amount -- note we're picking a random 
    # number between 0 and 360, then converting to radians
    rotate( radians(random(360)) )
    
    # decide which shape to draw based on our random number "whichShape"
    if whichShape == 0:
        line(-size/2, 0, size/2, 0)
    elif whichShape == 1:
        ellipse( 0, 0, size, size )
    elif whichShape == 2:
        rect( 0, 0, size, size )
    elif whichShape == 3:
        triangle( 0, 0, size/2, size, size, 0 )
    elif whichShape == 4:
        arc(0, 0, size, size, radians(0), radians(270), PIE)
    elif whichShape == 5:
        quad( 0, 0, size/2, size, size, 0, size/2, -size )
    else:
        point( 0, 0 )
