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
    


