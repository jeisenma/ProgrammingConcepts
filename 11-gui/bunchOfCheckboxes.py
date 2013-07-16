from checkbox import *

def setup():
	global checks
	size(130,310)
	checks = []
	for i in range(10):
		checks.append( CheckBox( Rect(20,10+30*i,20,20,2), label="Checkbox %d"%i, toggle=i%2 ) )

def draw():
	background(200)
	for check in checks:
		check.draw()

def mouseReleased():
	for check in checks:
		check.release()

