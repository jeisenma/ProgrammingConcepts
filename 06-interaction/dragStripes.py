# J Eisenmann 2013 
# jeisenma@accad.osu.edu

stripes = []
numStripes = 10

def setup():
	size(400,400)
	print stripes
	for i in range(numStripes):
		stripes.append(0)
	print stripes
	
def draw():
	w = width/numStripes
	for i in range(numStripes):
		fill(stripes[i])
		rect(i*w,0,w,height)
	# draw visual debugging info
	which = (mouseX%width)/(width/numStripes)
	fill(255)
	rect(0, 0, 100, 30)
	fill(0)
	text( "%d = %d / %d"%(which, mouseX, width/numStripes), 20, 20 )
	
def mouseDragged():
	which = (mouseX%width)/(width/numStripes)
	stripes[which] += 5
