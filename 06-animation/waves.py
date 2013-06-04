# Adapted from Dan Shiffman's example: http://processing.org/examples/sinewave.html

def setup():
	size(640, 360)
	global xspacing, w, theta, amplitude, period, dx, yvalues 
	xspacing = 16		# How far apart should each horizontal location be spaced
	theta = 0.0			# Start angle at 0
	amplitude = 75.0	# Height of wave
	period = 500.0		# How many pixels before the wave repeats
	w = width+16
	num = w/xspacing	# How many circles to draw
	yvalues = [0]*num	# Using an array to store height values for the wave (Notice the shortcut for making an array filled with zeros) 
	dx = (TWO_PI / period) * xspacing	  # Value for incrementing X, a function of period and xspacing

def draw():
	background(0)
	calcWave()
	renderWave()

def calcWave():
	global theta, yvalues, amplitude, dx
	# Increment theta (try different values for 'angular velocity' here
	theta += 0.02
	
	# For every x value, calculate a y value with sine function
	x = theta
	for i,y in enumerate(yvalues):	# Notice the enumerate which gives us each value in the list along with an index
		yvalues[i] = sin(x)*amplitude
		x+=dx

def renderWave():
	global yvalues, xspacing
	noStroke()
	fill(255)
	# A simple way to draw the wave with an ellipse at each location
	for i,y in enumerate(yvalues):
		ellipse(i*xspacing, height/2+y, 16, 16)

