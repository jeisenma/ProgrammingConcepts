# J Eisenmann 2013 
# jeisenma@accad.osu.edu

mass = 20
gravity = 0.8
restLen = 10.0	# rest length
ks = 0.6		# Spring constant
kd = 0.95		# Damping constant

vel = PVector()		# Velocity
accel = PVector()	# Acceleration
force = PVector()	# Force
currPos = PVector()
restPos = PVector()

def setup():
    size(400,400)
    strokeWeight(2)

    # Mouse button state
    global mouseDown
    mouseDown = False

def update():
    restPos.x = mouseX
    restPos.y = mouseY
    springF = PVector.sub(currPos, restPos)	 # f=-ky
    currLen = springF.mag()
    springF.normalize()
    springF.mult(-ks*(currLen-restLen))
    force.add(PVector(0,gravity*mass,0))
    force.add(springF)
    accel = PVector.mult(force, 1.0/mass)  # Set the acceleration, f=ma == a=f/m
    vel.add(accel)						   # Update the velocity
    vel.mult(kd)
    currPos.add(vel)					   # Updated position

def draw():
    if not mouseDown:
        update()
    
    background(200)
    stroke(175,0,0)
    line(restPos.x,restPos.y,currPos.x,currPos.y)
    fill(255)
    stroke(0)
    ellipse(currPos.x,currPos.y,mass,mass)
    
    force.x = 0
    force.y = 0				   # zero out forces


def mousePressed():
    global mouseDown
    mouseDown = True
    currPos.x = mouseX
    currPos.y = mouseY
    vel.x = 0
    vel.y = 0	 # get rid of leftover velocity

def mouseReleased():
    global mouseDown
    mouseDown = False

def mouseDragged():
    restPos.x = mouseX
    restPos.y = mouseY



