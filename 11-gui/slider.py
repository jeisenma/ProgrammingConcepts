from rect import *
from circle import *

class Slider:
	""" A slider class.  Works for vertical or horizontal sliders """
	def __init__(self, place, minVal=0.0, maxVal=1.0):
		self.place = place
		self.minMax = [minVal, maxVal]
		self.isVertical = place.w < place.h	# is the slider vertical?
		self.value = minVal
		self.isDragging = False
		if self.isVertical:
			self.handle = Circle( 	place.x+place.w/2, 
									place.y+place.h, 
									8 )
		else:
			self.handle = Circle( 	place.x,
									place.y+place.h/2, 
									8 )
	
	def update(self):
		if self.isVertical:
			self.value = map(mouseY, self.place.y+self.place.h, self.place.y, self.minMax[0], self.minMax[1])
		else:
			self.value = map(mouseX, self.place.x, self.place.x+self.place.w, self.minMax[0], self.minMax[1])
		self.value = constrain(self.value, self.minMax[0], self.minMax[1])
			
	def draw(self):
		if self.isVertical:
			self.handle.y = map(self.value, 
								self.minMax[0], self.minMax[1], 
								self.place.y+self.place.h, self.place.y)
		else:
			self.handle.x = map(self.value, 
								self.minMax[0], self.minMax[1], 
								self.place.x, self.place.x+self.place.w)
		strokeWeight(4)
		if self.isVertical:
			line( 	self.place.x+self.place.w/2, self.place.y, 
					self.place.x+self.place.w/2, self.place.y+self.place.h )
		else:
			line( 	self.place.x, self.place.y+self.place.h/2, 
					self.place.x+self.place.w, self.place.y+self.place.h/2 )
		strokeWeight(2)
		self.handle.draw()
	
	def press(self):
		if (self.handle.contains(mouseX, mouseY, tol=14) or
			self.place.contains(mouseX, mouseY,) ):
			self.isDragging = True
			self.update()
	
	def drag(self):
		if self.isDragging:
			self.update()
	
	def release(self):
		self.isDragging = False
