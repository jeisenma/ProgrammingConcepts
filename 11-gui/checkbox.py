from rect import *

class CheckBox:
	""" A checkbox class """
	def __init__(self, place, label, toggle=False ):
		self.place = place
		self.label = label
		self.toggle = toggle
			
	def draw(self):
		strokeWeight(2)
		fill(255)
		self.place.draw()
		if self.toggle:
			line(self.place.x+2, self.place.y+2, self.place.x+self.place.w-2, self.place.y+self.place.h-2)
			line(self.place.x+2, self.place.y+self.place.h-2, self.place.x+self.place.w-2, self.place.y+2)
		fill(0)
		textAlign( LEFT, CENTER )
		textSize( self.place.h/2 )
		text( self.label, self.place.x+3*self.place.w/2, self.place.y+self.place.h*0.45 )
	
	def release(self):
		if self.place.contains(mouseX, mouseY,):
			self.toggle = not self.toggle
