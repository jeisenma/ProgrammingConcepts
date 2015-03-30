# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# ball properties
rad = 25		  # radius of the ball
pos = PVector( 150, 50 )		# initial position of the ball
vel = PVector( random(-3,3), random(-3,3) )	 # velocity of the balll
grav = PVector( 0, 0.9 )		# force on the ball (gravity)
d = 0.97		  # how much bounce?

def setup():
    size(300,300)

def draw():
    """ update the ball's state and draw it every frame """
    # update the velocity with the force
    vel.add(grav)
    
    # update the position with the velocity
    pos.add(vel)
    
    # deal with wall collisions
    if(pos.y > height-rad):	  # floor collision
        pos.y = height-rad
        vel.y = -vel.y
        vel.mult(d)
    
    if(pos.x < rad):		  # left wall collision
        pos.x = rad
        vel.x = -vel.x
        vel.mult(d)
    
    if(pos.x > width-rad):	  # right wall collision
        pos.x = width-rad
        vel.x = -vel.x
        vel.mult(d)
    
    
    # draw the scene
    background(150)	   # refresh the background
    strokeWeight(2)
    
    fill(20,160,240)
    ellipse( pos.x, pos.y, rad*2, rad*2)  # draw the ball


def mousePressed():
    """ If the ball is clicked, add a random velocity. """
    if( dist(mouseX,mouseY,pos.x,pos.y) < rad ):
        vel.add( PVector(random(-3,3), random(10,20)) )


