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
    # for i in range( len(places) ):
    print(frameCount)
    for i,p in enumerate(places):
        if dist(mouseX, mouseY, p.x, p.y) < 15:
            fill(255,0,0)
        else:
            fill(150,150,240)
        ellipse( p.x, p.y, 30, 30 )
        fill(255)
        text(i,p.x,p.y)
        line(p.x,p.y, mouseX, mouseY)
    which = -1
    for i,p in enumerate(places):
        if dist(mouseX, mouseY, p.x, p.y) < 15:
            which = i
            break
    # if over a circle, show index in upper left corner
    if which >= 0:
        fill(0)
        rect(10,10,20,20)
        fill(255)
        text( which, 20, 20)

