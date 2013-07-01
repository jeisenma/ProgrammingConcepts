data = [PVector(0.135,0.115,2112.0493),
		PVector(0.4025,0.185,715.86224),
		PVector(0.1525,0.32,1548.8124),
		PVector(0.38,0.3725,1493.197),
		PVector(0.1625,0.755,2387.9358),
		PVector(0.3725,0.7875,2186.2312),
		PVector(0.84,0.1075,1029.9718),
		PVector(0.74,0.5775,1854.2734),
		PVector(0.7175,0.8575,1507.7217) ]

def setup():
	size(480,400)

def draw():
	background(255)
	
	# draw the axes
	bd = 15		# border space
	stroke(0)
	fill(0)
	textSize(12)
	textAlign(CENTER,TOP)
	line( bd, height-bd, height-bd, height-bd )	  				# x-axis
	text( "Distance to the coast (miles)", height/2, height-bd )# ALWAYS label your axes!
	line( bd, bd, bd, height-bd )	 							# y-axis
	pushMatrix()
	rotate( radians(-90) )
	text( "Altitude (feet)", -width/2, 0 )
	popMatrix()
	
	textSize(20)
	text( "Housing Prices" , width/2, bd )		# title
	
	# draw a bubble size key
	for i,cost in enumerate(range(500, 2501, 1000)):
		diameter = sqrt(cost/PI)*2				# see note on diameter math below
		shade = map(cost,500,2500,100,255) 		# pick a circle fill color
		fill( shade )
		ellipse( 440, 260+i*diameter, diameter, diameter )
		fill( (shade+150)%255 )					# offset the circle fill to get a text fill
		textSize(8)
		text( "$%d"%cost, 440, 255+i*diameter )	# label this circle
		
	# draw the data points
	stroke( 0 )
	for d in data:	  # display the data set indicated by 'mode'
		# if area is stored in d.z and for a circle, area = PI*R^2, then diameter = sqrt(area/PI)*2
		fill(map(d.z,500,2500,100,255))
		diameter = sqrt(d.z/PI)*2
		ellipse(d.x*width,d.y*height,diameter,diameter) 
	



