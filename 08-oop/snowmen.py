# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# import randint for randomly choosing the number of body segments
from random import randint
			
# create a list for storing snowmen
snowmen = []

def setup():
	size(800,400)

def draw():
	background(240,240,250)
	# draw all the snowmen in the list
	for snowman in snowmen:
		snowman.draw()
		
def mousePressed():
	# fake depth with size (small in the back, large in the front)
	size = map(mouseY, 0, height, 1, 100)
	# make a new snowman and add it to the list
	snowmen.append( Snowman( 	base=size,
								segments=randint(2,3),
								pos=PVector(mouseX, mouseY) 
							) )


class Snowman:
	""" Snowman class: draws a snowman """
	def __init__(	self, 
					base=80, 
					segments=3, 
					shade=color(255), 
					pos=PVector(width/2,height) 
				 ):
		""" segments: number of body parts (typically 3)
			shade: fill color of snowman (typically white)
			base: diameter of the base segment 
			pos: position of the bottom of the snowman """
		self.segments = segments
		self.shade = shade
		self.base = base
		self.pos = pos
	
	def draw(self):
		""" draws the snowman """
		fill(self.shade)
		pushMatrix()
		translate(self.pos.x,self.pos.y)
		for i in range(self.segments):
			diam = self.base*(1-float(i)/self.segments)
			print diam
			translate(0,-diam/2)
			ellipse(0,0,diam,diam)
			translate(0,-diam*0.4)
		popMatrix();

