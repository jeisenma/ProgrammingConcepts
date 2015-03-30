# J Eisenmann 2013 
# jeisenma@accad.osu.edu

radius = 150
pos = PVector(200,200)

def setup():
    size(400,400)

def draw():
    background(100)
    # find the distance from the mouse to the circle center
    d = dist( mouseX, mouseY, pos.x, pos.y )
    # change the color of the circle if mouse is over it
    if( d < radius ):
        fill(80,10,100)
    else:
        fill(255)
    # draw the circle (without a stroke)
    noStroke()
    ellipse(pos.x, pos.y, 2*radius, 2*radius)
    
    # visual debugging:
    if( d < radius ):	# change the line color if mouse is over circle
        stroke(255)
    else:
        stroke(0)
    line( mouseX, mouseY, pos.x, pos.y )
    
    # draw the distance value to the screen
    fill(255)
    text( d, mouseX, mouseY )
    
