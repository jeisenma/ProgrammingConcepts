from rect import *
from circle import *

def setup():
	global w
	size(200,200)
	w = Widget( Rect(10,10,100,20) )

def draw():
	w.draw()
	
def mousePressed():
	w.press()

def mouseDragged():
	w.drag()

def mouseReleased():
	w.release()
	
class Widget:
	""" A template class """
	def __init__(self, place, value="nothing"):
		""" initialize the widget's properties """
		self.place = place
		self.value = value
		
	def update(self):
		""" update the value of this widget """
		self.value = "something"
			
	def draw(self):
		self.place.draw()
	
	def press(self):
		if self.place.contains(mouseX, mouseY,):
			self.update()
	
	def drag(self):
		pass
	
	def release(self):
		pass
