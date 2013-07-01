# the scale of the graph
innerRadius = 130
outerRadius = 300

data = [ 0.1325, 0.36, 0.468, 0.987, 0.852, 0.932, 0.873, 0.065, 1.0, 0.254 ]

def setup():
	size(400,400)

def draw():
	background(255)
	noStroke()
	# move things to the center of the screen
	translate(width*0.5, height*0.5) 
	
	# how far to rotate each time
	angle = TWO_PI/len(data)
	
	for i,d in enumerate(data):
		# length of the arc for this data point
		arcSz = map(d,0,1,innerRadius,outerRadius)
		# pick a hue
		shade = map(i,0,len(data),0,255)
		rotate(angle)
		# switch to the HSB color mode
		colorMode(HSB)
		fill(shade,255,255)
		arc( 0, 0, arcSz, arcSz, 0, angle ) 
	
	# cut out the middle by drawing a white circle
	fill(255)
	ellipse(0,0,innerRadius, innerRadius)

