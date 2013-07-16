from button import *

def setup():
	global b
	size(300,200)
	b = Button( Rect(50,50,200,100,20), "Click", fill=255, over=color(250,250,220), down=180 )

def draw():
	background(100)
	b.draw()

def mousePressed():
	b.press()

def mouseReleased():
	b.release()

