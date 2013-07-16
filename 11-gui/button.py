from rect import *

class Button:
	""" A button class """
	def __init__(self, place, label, fill=255, over=200, down=100 ):
		self.place = place
		self.label = label
		self.fill = fill
		self.over = over
		self.down = down
		self.mode = 0
	
	def update(self):
		if (self.place.contains(mouseX, mouseY) and self.mode == 0):
			self.mode = 1
		elif (not self.place.contains(mouseX, mouseY) and self.mode == 1):
			self.mode = 0
			
	def draw(self):
		self.update()
		strokeWeight(2)
		if self.mode == 0:
			fill(self.fill)
		elif self.mode == 1:
			fill(self.over)
		elif self.mode == 2:
			fill(self.down)
		self.place.draw()
		fill(0)
		textAlign( CENTER, CENTER )
		textSize( self.place.h/2 )
		text( self.label, self.place.x+self.place.w/2, self.place.y+self.place.h*0.45 )
	
	def press(self):
		if self.place.contains(mouseX, mouseY,):
			self.mode = 2
	
	def release(self):
		self.mode = 0
