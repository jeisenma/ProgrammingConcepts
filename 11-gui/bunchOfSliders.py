from slider import *

def setup():
	global sliders
	size(400,200)
	sliders = []
	for i in range(10):
		sliders.append( Slider( Rect(40*i,10,40,180), minVal=100, maxVal=255 ) )

def draw():
	background(200)
	for slidy in sliders:
		slidy.draw()

def mousePressed():
	for slidy in sliders:
		slidy.press()

def mouseDragged():
	for slidy in sliders:
		slidy.drag()

def mouseReleased():
	for slidy in sliders:
		slidy.release()

