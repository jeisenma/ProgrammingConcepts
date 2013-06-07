# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# the rectangle dimensions
x = 50
y = 100
w = 300
h = 200

# circle attributes
cx = x+w/2
cy = y+h/2
r = 20
easing = 0.05

def setup():
	size(400,400)

def draw():
	global cx,cy	
	background(100)
	
	# draw the rectangle
	fill(255)
	rect(x,y,w,h)
	
	# update the circle position
	if( abs(mouseX-cx) > 0 ):
		cx += (mouseX-cx)*easing;
	if( abs(mouseY-cy) > 0 ):
		cy += (mouseY-cy)*easing;
	
	# constrain the circle to stay inside the rectangle
	cx = constrain( cx, x+r, x+w-r );
	cy = constrain( cy, y+r, y+h-r );
	
	# draw the circle
	fill(80,10,100)
	ellipse(cx,cy,2*r,2*r)

