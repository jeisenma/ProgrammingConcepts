greens = []		# a list to hold the green color values of each circle
numCircles = 12	# how many circles are there?

def setup():
	global greens, numCircles
	size(400,400)
	# create a bunch of random numbers that will represent to green values 
	for i in range(numCircles):
		greens.append( random(255) )

def draw():
	global greens, numCircles
	background(200)
	# calculate the circle diameter based on screen width and number of circles
	diam = float(width)/numCircles
	# for every circle...
	for i in range(numCircles):
		# make it a shade of green (based on the values in the "greens" list)
		fill( 100, greens[i], 100 )
		# draw a circle at the correct place
		ellipse( i*diam+diam/2, height/2, diam, diam )
