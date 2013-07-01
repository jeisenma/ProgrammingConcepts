# J Eisenmann 2013 
# jeisenma@accad.osu.edu
from random import random
from Shape import Shape

faves = {}		# the favorites
buttons = []	# the buttons
howMany = 0		# how many favorites
bw = 80.0			# button width
pos = PVector(200, 160)	# shape display position
sketchPath = ""

def setup():
	global shape
	size(400,480)
	n = map(random(), 0, 1, 4, 80)		# number of points
	r = map(random(), 0, 1, 24, 30)		# radius
	amp = map(random(), 0, 1, 4, 20)	# amplitude of oscillation
	frq = map(random(), 0, 1, 1, 30)	# frequency of oscillation
	nz = map(random(), 0, 1, 0, 40)		# frequency of Perlin noise
	part = map(random(), 0, 1, 0, PI)	# ignore a slice of the shape?
	shape = Shape( pos, n=n, r=r, oscilAmp=amp, oscilFrq=frq, nzFrq=nz, part=part)
	
def draw():
	background(200)
	# interactively change some of the parameters with mouse movement
	# shape.part = map(mouseX, 0, width, 0, PI);
	# shape.of = map(mouseY, 0, width, 4, 200);
	# shape.update()
	shape.draw()	
	for b in buttons:
		b.draw()

def keyPressed():
	setup()	# generate a new shape

def mousePressed():
	global howMany, shape
	if( mouseY > height-bw ):	# if button area clicked
		for but in buttons:
			if but.isOver():	# if this button was clicked
				fav = faves[ but.name ]	# look up that favorite by  name and restore it
				shape = Shape( pos,  n=fav.n, r=fav.r, oscilAmp=fav.oa, oscilFrq=fav.of, nzFrq=fav.nz, part=fav.part)
				
	elif( howMany < width/bw ):	# if image area clicked
		imgName = "data/shape-%d.png"%howMany
		saveFrame(imgName)		# save the image to disk
		faves[imgName] = shape	# store the shape in the faves dictionary with imgName as the key
		b = Button(imgName, PVector(howMany*bw, height-bw), bw)	# create a button for that favorite
		if howMany >= len(buttons):	# if we don't have  full set of buttons, create a new one
			buttons.append( b )
		else:
			buttons[howMany] = b	# otherwise, replace a previous button
		howMany+=1
		howMany = howMany % int(width/bw)	# modulo howMany so it doesn't add more buttons than will fit on screen
		
class Button:
	def __init__(self, name="", pos=PVector(), size=bw):
		""" name: the image name
			pos: the top left corner of this button
			size: the width of this button """
		self.name = name
		self.pos = pos.get()
		self.size = size
		self.img = loadImage("%s%s"%(sketchPath,name))
		
	def draw(self):
		""" draw this button """
		strokeWeight(2)
		rect( self.pos.x-1, self.pos.y-1, self.size, self.size ) # draw an outline around each button
		image( self.img, self.pos.x, self.pos.y, self.size, self.size/width*height ) # draw the image so that part of it hangs off the bottom of the screen
		
	def isOver(self):	
		""" returns true if the mouse is over this button """
		return ( mouseX > self.pos.x and mouseX < self.pos.x+self.size and 
				 mouseY > self.pos.y and mouseY < self.pos.y+self.size )

