def setup():
	global data, headings
	size(480,400)
	data = {}	# new empty dictionary
	f = open('housingData.csv', 'r')
	lines = f.readlines()
	headings = lines[0].split(',')	# get the column headings from the first line
	for heading in headings:
		data[ heading ] = []
	for line in lines[1:]:	# slice the list to skip the first line (header)
		for i, item in enumerate(line.split(',')):
			data[ headings[i] ].append( float(item) )

def draw():
	background(255)
	bd = 15		# border space
	stroke(0)
	fill(0)
	textSize(12)
	textAlign(CENTER,TOP)
	# draw the axes
	line( bd, height-bd, height-bd, height-bd )	  				# x-axis
	text( data.keys()[0], height/2, height-bd ) # ALWAYS label your axes!	data column 1
	line( bd, bd, bd, height-bd )	 							# y-axis
	pushMatrix()
	rotate( radians(-90) )
	text( data.keys()[1], -width/2, 0 )			# data column 2
	popMatrix()
	
	textSize(20)
	text( data.keys()[2] , width/2, bd )		# data column 3
	
	# draw a bubble size key
	for i,cost in enumerate(range(500, 2501, 1000)):
		diameter = sqrt(cost/PI)*2				# see note on diameter math below
		shade = map(cost,500,2500,100,255) 		# pick a circle fill color
		fill( shade )
		ellipse( 440, 250+i*diameter, diameter, diameter )
		fill( (shade+150)%255 )					# offset the circle fill to get a text fill
		textSize(8)
		text( "$%d"%cost, 440, 245+i*diameter )	# label this circle
		
	# draw the data points
	stroke( 0 )
	print headings[2]
	print data[headings[2]]
	for i in range(len(data[headings[0]])):
		# if area is stored in d.z and for a circle, area = PI*R^2, then diameter = sqrt(area/PI)*2
		fill(map(data[headings[2]][i],min(data[headings[2]]),max(data[headings[2]]),100,255))
		diameter = sqrt(data[headings[2]][i]/PI)*2
		ellipse(	data[headings[0]][i]*width,
					data[headings[1]][i]*height,
					diameter,diameter) 

