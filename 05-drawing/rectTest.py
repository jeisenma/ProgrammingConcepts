# the rectangle dimensions
x=100
y=100
w=120
h=170

def setup():
	size(400,400)

def draw():
	global x,y,w,h
	background(100)
	
	# change the color of the rectangle if mouse is over it
	if( x < mouseX and mouseX <= x+w and
		y < mouseY and mouseY <= y+h ):
		fill(80,10,100)
	else:
		fill(255)
	
	# draw the rectangle
	rect(x,y,w,h)
	
	# visual debugging:
	noFill()
	if( x < mouseX and mouseX <= x+w ):
		rect( x, 0, w, height )
	if( y < mouseY and mouseY <= y+h ):
		rect( 0, y, width, h )
