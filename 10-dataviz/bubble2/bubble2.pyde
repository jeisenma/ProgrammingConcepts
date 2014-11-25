# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# A bubble chart example that loads data from a CSV file using Processing's loadTable() function

def setup():
	global data, headings
	size(480,400)
	data = {}	# new empty dictionary
	table = loadTable('housingData.csv', 'csv')
	headings = []
	for i in range(table.getColumnCount()):	# get the column headings from the first line
		heading = table.getRow(0).getString(i)
		if len(heading) > 0:
			headings.append( heading )	# add this header to the list of headings
			data[ heading ] = []		# make an empty list for each heading
	
	table = loadTable('housingData.csv', 'header')
	for row in table.rows():
		for heading in headings:
			data[ heading ].append( row.getFloat(heading) )	# get the data in this row indexed by the heading

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
	for i in range(len(data[headings[0]])):
		# if area is stored in d.z and for a circle, area = PI*R^2, then diameter = sqrt(area/PI)*2
		fill(map(data[headings[2]][i],min(data[headings[2]]),max(data[headings[2]]),100,255))
		diameter = sqrt(data[headings[2]][i]/PI)*2
		ellipse(	data[headings[0]][i]*width,
					data[headings[1]][i]*height,
					diameter,diameter) 

