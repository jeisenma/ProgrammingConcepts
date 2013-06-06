def setup(): 
	size(640, 360)
	background(255, 204, 0)
	frameRate(24)
	
	global xpos, ypos, drag, mouseDown, animation1, animation2 
	xpos = 0
	ypos = height * 0.25
	drag = 30.0
	mouseDown = False
	animation1 = Animation("PT_Shifty_", 38)
	animation2 = Animation("PT_Teddy_", 60)

def draw():	 
	global xpos
	
	# have the animation follow the mouse (horizontal only)
	dx = mouseX - xpos
	xpos = xpos + dx/drag

	# Display the sprite at the position xpos, ypos
	if mouseDown:
		# if mouse is down, show one animation
		background(153, 153, 0)
		animation1.draw(xpos-animation1.getWidth()/2, ypos)
	else:
		# if mouse is up, show the other animation
		background(255, 204, 0)
		animation2.draw(xpos-animation1.getWidth()/2, ypos)

class Animation:
	""" Class for animating a sequence of GIFs """
	def __init__(self, imagePrefix, count):
		""" count: how many images there are the sequence
			imagePrefix: the image name prefix (note: assumes the image filenames use 4 digit padding) """
		self.imageCount = count
		self.images = [] #PImage[imageCount]
		self.frame = 0
		
		for i in range(self.imageCount): 
			# Use nf() to number format 'i' into four digits
			filename = imagePrefix + nf(i, 4) + ".gif"
			self.images.append( loadImage(filename) )

	def draw(self, x, y): 
		""" update the current frame and draw the image corresponding to that frame """
		self.frame = (self.frame+1) % self.imageCount
		image(self.images[self.frame], x, y)
	
	def getWidth(self): 
		""" get the image width """
		return self.images[0].width

# keep track of whether the mouse is down or up
def mousePressed():
	global mouseDown
	mouseDown = True

def mouseReleased():
	global mouseDown
	mouseDown = False
