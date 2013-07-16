from slider import *

def setup():
	global slidy
	size(400,200)
	slidy = Slider( Rect(50,80,300,40), minVal=100, maxVal=255 )

def draw():
	background(slidy.value)
	slidy.draw()

def mousePressed():
	slidy.press()

def mouseDragged():
	slidy.drag()

def mouseReleased():
	slidy.release()

