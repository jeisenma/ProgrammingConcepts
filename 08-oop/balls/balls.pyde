# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# J Eisenmann 2013 
# jeisenma@accad.osu.edu

class Ball:
    """ Ball objects are 2D circles that bounce off walls and each other """
    def __init__(self, rad, pos, vel):	# the constructor -- responsible for creating balls
        """ rad: the ball radius
            pos: initial position of the ball 
            vel: initial velocity of the ball """
        self.rad = rad				
        self.pos = pos.get()		# make a copy of the parameter "pos"
        self.vel = vel.get()		# make a copy of the parameter "vel"
        self.g = PVector( 0, 0.9 )	# make all the balls' gravities the same -- remember positive Y is down
        self.d = 0.97				# the same damping for all the balls
        self.springyness = 0.25		# elasticity for ball-ball collisions
        self.shade = color(random(255), random(255), random(255))	# ball color is random

    def collide(self, allBalls):
        """ bounce off the other balls 
            (don't worry about the math here...) """
        for other in allBalls:
            distance = dist(self.pos.x, self.pos.y, other.pos.x, other.pos.y)
            mindist = self.rad + other.rad
            if distance < mindist:
                angle = atan2(other.pos.y - self.pos.y, other.pos.x - self.pos.x)
                target = PVector( self.pos.x + cos(angle)*mindist, self.pos.y + sin(angle)*mindist)
                acc = PVector(target.x,target.y)
                acc.sub(other.pos)
                acc.mult(self.springyness)
                selfMass = sq(self.rad)
                otherMass = sq(other.rad)
                selfForce = PVector(acc.x,acc.y)
                selfForce.mult(otherMass/(selfMass+otherMass))
                otherForce = PVector(acc.x,acc.y)
                otherForce.mult(selfMass/(selfMass+otherMass))
                self.vel.sub(selfForce)
                other.vel.add(otherForce)
    
    def update(self, allBalls):		
        """ updates the "physics" of the ball """
        # springy collisions with other balls
        self.collide(allBalls)
        # update the velocity with the force
        self.vel.add(self.g)
        # update the position with the velocity
        self.pos.add(self.vel)
        # deal with wall collisions
        if(self.pos.y > height-self.rad):	# floor collision
            self.pos.y = height-self.rad
            self.vel.y = -self.vel.y
            self.vel.mult(self.d)
        if(self.pos.x < self.rad):			# left wall collision
            self.pos.x = self.rad
            self.vel.x = -self.vel.x
            self.vel.mult(self.d)
        if(self.pos.x > width-self.rad):	# right wall collision
            self.pos.x = width-self.rad
            self.vel.x = -self.vel.x
            self.vel.mult(self.d)
    
    def display(self):
        """ draws the ball """
        fill(self.shade)
        ellipse( self.pos.x, self.pos.y, self.rad*2, self.rad*2)	# draw the ball
    
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



