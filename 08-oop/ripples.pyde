# a list to hold all the Ripple objects
ripples = []

def setup():
    size(400,400)
    
def draw():
    background(70)
    # for every Ripple object in the ripples list
    for r in ripples:
        # call the animate function of the Ripple object to update the diameter
        r.animate()
        # call the display function of the Ripple object to draw the ellipse
        r.display()

def mouseMoved():
    # create a PVector to hold the mouse position
    ripplePosition = PVector(mouseX, mouseY)
    # only do this every four frames (reduces the ripple creation frequency)
    if frameCount % 4 == 0:
        # find the distance from the last mouse position to the current position
        mouseSpeed = dist(pmouseX, pmouseY, mouseX, mouseY)
        # constrain this distance between a low and high number
        mouseSpeed = constrain(mouseSpeed, 0.5, 5)
        # create a new Ripple object and add it to the ripples list:
        #   pass in the position PVector we created from the mouse X and Y values
        #   also pass in the distance as a speed parameter for a new ripple
        ripples.append( Ripple( ripplePosition, mouseSpeed ) )

class Ripple:
    # this function creates new Ripple objects, the second parameter is 
    # optional and has a default speed of 2
    def __init__(self, pos, speed=2):
        self.position = pos
        self.speed = speed
        # start with a zero diameter (a point)
        self.diameter = 0
        
    def animate(self):
        # always make the diameter bigger using the speed
        self.diameter += self.speed
        
    def display(self):
        # no fill for these ellipses, only stroke
        noFill()
        # create an transparency value that gets smaller as the diameter gets bigger
        alpha = map(self.diameter, 0, width/2, 255, 0)
        # set the stroke color with this transparency value
        stroke(255,alpha)
        # draw the circle
        ellipse(self.position.x, self.position.y, self.diameter, self.diameter)