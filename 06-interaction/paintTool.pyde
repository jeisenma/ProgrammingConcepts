maxSW = 12
sw = 0
mode = False
clickX = 0
clickY = 0
clickCount = 0

def setup():
    size(400,400)
    background(200)
    
def draw():
    pass

def mouseDragged():
    global sw
    if not mode:
        d = max( 1, dist(pmouseX, pmouseY, mouseX, mouseY))
        sw = (sw + maxSW/d)/2
        strokeWeight(sw)
        line(pmouseX, pmouseY, mouseX, mouseY)

def mousePressed():
    global clickX, clickY, clickCount
    if mode and clickCount > 0:
        strokeWeight(4)
        line( clickX, clickY, mouseX, mouseY )
    
    clickX = mouseX
    clickY = mouseY
    if mode:
        clickCount += 1
        
def keyPressed():
    global mode
    if keyCode == 127 or keyCode == 8:
        setup()
    if key == ' ':
        mode = not(mode)
    elif key == 'r':
        stroke(color(255,0,0))		
    elif key == 'g':
        stroke(color(0,255,0))		
    elif key == 'b':
        stroke(color(0,0,255))		
    elif key == 's':
        save("myPainting.png")
