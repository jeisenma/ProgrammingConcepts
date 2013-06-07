# J Eisenmann 2013 
# jeisenma@accad.osu.edu

worm = []		 # create a list called 'worm' that will store positions

def setup():
	size(400,400)
	for i in range(100):
		# initialize each value of the array to be at screen center
		 worm.append( vectorNoise() )

def update():
	""" moves the worm """
	# remove the last item and insert a new noise value at the beginning
	worm.pop(-1)
	worm.insert(0, vectorNoise() )

def draw():
	""" draws the worm """
	background(150)
	update()						# call the update function (otherwise, nothing will move)
	for i,w in enumerate(worm): 	# draw the worm
		ellipse( w.x, w.y, len(worm)-i, len(worm)-i )
	
def vectorNoise():
	""" construct a PVector using noise,
		mapped to the window width and height """
	x = map( noise(0.01*frameCount), 0, 1, 0, width)
	y = map( noise(0.01*frameCount+456), 0, 1, 0, height)
	return PVector(x,y)
