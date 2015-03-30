# J Eisenmann 2013 
# jeisenma@accad.osu.edu

floor = 60
goingUp = True
timer = 0

def setup():
    size(400,400)
    textAlign(CENTER,CENTER)	# whenever we draw text to the screen, make sure 
                                # it's centered horizontally and vertically
    
def draw():
    # clear the screen every frame
    background(200)

    # draw the floor
    fill(0)
    rect(0, height-floor, width, height)
    
    # title
    textSize(20)	# title text is bigger than the other text
    fill(0)			# ... and black
    text("The Many Adventures of Sine", width/2, 20)
    textSize(14)	# set the text size back to something reasonable
    fill(255)		# ... and white
    
    # squashing
    freq = 0.04										# the speed of the action
    w = map( sin(frameCount*freq), -1, 1, 30, 100 )	# remap sine from [-1,1] to [30, 100]
    h = 130-w 										# pretty much the opposite of w
    ellipse( 70, height-floor-h/2, w, h )			# draw ellipse with w and h for size (center Y depends on h)
    text("squashing", 70, height-floor/2)			# label this adventure
    
    # bouncing
    freq = 0.08												# the speed of the action
    y = map( abs( sin(frameCount*freq) ), 0, 1, 0, 180 )	# absolute value of sine, remapped to [0,180]
    rad = 30												# the radius of the ball
    ellipse( 160, height-floor-rad-y, 2*rad, 2*rad )		# draw the ball, center Y depends on y
    text("bouncing", 160, height-floor/2)					# label this adventure
    
    # waving
    freq = 0.07											# the speed of the action
    numJoints = 2										# how many joints in the arm?
    rot = map( sin(frameCount*freq) , -1, 1, -10, -60 )	# control joint rotation with sine, vary between [-10,-60]
    pushMatrix()										# remember the current translation/rotation
    translate( 230, height-floor-40 )		# start at 40 pixels above the floor (moving the paper!)
    for i in range(numJoints):				# draw each arm segment
        ellipse( 0, 0, 20, 20 )				# start with a circle for the joint (note the position!)
        rotate( radians(rot) )				# rotation based on sine
        line( 10, 0, 30, 0 )				# draw a line for the bone
        translate( 40, 0 )					# move the paper to the location of the next joint
    ellipse( 0, 0, 30, 20 )								# draw the hand at the end of the arm
    popMatrix()											# restore the previous translation/rotation
    text("waving", 250, height-floor/2)					# label this adventure
    
    # easing
    global timer
    freq = 0.02											# the speed of the action
    thick = 10											# the platform thickness
    low = height-floor-thick							# the lower position of the platform
    high = height-300									# the upper position of the platform
    y = easing( timer*freq, low, high, goingUp )		# call the easing function
    rect( 300, y, 80, thick )							# draw the platform
    text("easing\n(click!)", 340, height-floor/2)		# label this adventure
    timer += 1											# increase the timer by one
    
def easing( now, here, there, up ):
    """ A function that smoothly changes a value from 
        *here* to *there* as *now* varies from 0 to 1.  
        Sine is used for ease-in/ease-out, and *up* is 
        a boolean that toggles up/down. """
    now = constrain( now, 0, 1 )	# make sure *now* is betweeen [0,1]
    now = map( now, 0, 1, -PI/2, PI/2 )
    if up:	# if going up
        return map( sin(now), -1, 1, here, there )
    else:	# if going down
        return map( sin(now), -1, 1, there, here )

def mousePressed():
    global goingUp, timer
    goingUp = not goingUp		# tell the platform to go up
    timer = 0					# restart the timer
