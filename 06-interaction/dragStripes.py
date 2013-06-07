# J Eisenmann 2013 
# jeisenma@accad.osu.edu

stripes = []
numStripes = 100

def setup():
	global stripes
	size(400,400)
	for i in range(numStripes):
		stripes.append(0)
	
def draw():
	w = width/numStripes
	for i in range(numStripes):
		fill(stripes[i])
		rect(i*w,0,w,height)

def mouseDragged():
	which = (mouseX%width)/(width/numStripes)
	stripes[which] += 5
