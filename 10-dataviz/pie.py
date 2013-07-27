# J Eisenmann 2013 
# jeisenma@accad.osu.edu

angles = [ 30, 10, 45, 35, 60, 38, 75, 67 ] 

def setup(): 
	global diameter
	size(640, 360)
	noStroke()
	diameter = min(width, height) * 0.75
	noLoop()    # Run once and stop -- no need for animation here

def draw(): 
	background(200,200,240)
	lastAngle = 0
	for angle in angles:
		fill(angle * 3.0)				# set the color of this slice
		arc(width/2, height/2, 			# draw an angle starting from the last slice
			diameter, diameter, 
			lastAngle, lastAngle+radians(angle))
		lastAngle += radians(angle)		# keep track of where we left off, so we can start there next time
    


