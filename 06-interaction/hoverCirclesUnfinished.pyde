places = []
numCircles = 10

def setup():
    size(400,400)
    textAlign(CENTER,CENTER)

    for i in range(numCircles):
        x = random(width)
        y = random(height)
        # add random locations (PVector) to the places list
        places.append( PVector(x,y) )

def draw():
    background(100)
    # iterate over each position in the list
    for i,p in enumerate(places):
        ellipse( p.x, p.y, 30, 30 )
        fill(255)
        text(i,p.x,p.y)
        line(p.x,p.y, mouseX, mouseY)
    
