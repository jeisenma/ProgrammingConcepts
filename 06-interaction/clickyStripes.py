stripes = []
numStripes = 100

def setup():
	global stripes, numStripes
	size(400,400)
	for i in range(numStripes):
		stripes.append(0)
	
def draw():
	global stripes, numStripes
	w = width/numStripes
	for i in range(numStripes):
		fill(stripes[i])
		rect(i*w,0,w,height)

def mouseDragged():
	global stripes, numStripes
	which = (mouseX%width)/(width/numStripes)
	stripes[which] += 5
