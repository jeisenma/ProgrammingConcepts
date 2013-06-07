# J Eisenmann 2013 
# jeisenma@accad.osu.edu

maxSW = 12	# the thickest possible stroke weight
sz = 0		# variable to keep track of the current stroke weight

# set up the drawing area
def setup():
	size(400,400)
	background(200)

# define the draw function (always!)
def draw():
	pass	# do nothing
	
# when the mouse is dragged...
def mouseDragged():
	""" Draws lines on the screen.  
		Slower strokes are fatter and faster ones are thinner. """
	global sz	# we will be changing the value of sz in this function, so make it global

	# how far did the mouse move? (minimum of one pixel)
	d = max(1, dist(pmouseX, pmouseY, mouseX, mouseY))
	
	# the stroke weight is a running average of current and previous stroke weight	
	sz += maxSW/d
	sz /= 2
	strokeWeight( sz )
	
	# draw a line between the previous and current mouse positions
	line(pmouseX, pmouseY, mouseX, mouseY)

# when a key is pressed...
def keyPressed():
	""" when the delete key is pressed, clear the screen """
	print(keyCode)
	if( keyCode == 127):
		background(200)
