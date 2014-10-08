# J Eisenmann 2013 
# jeisenma@accad.osu.edu

def setup():
	size(400,400)
	global center
	center = PVector(width/2, height/2)
	
def draw():
	# if mouse is in bottom right hand corner
	if mouseX > center.x and mouseY > center.y:		
		stroke(255)			# white
	# if mouse is either in the right half or in the bottom half
	elif mouseX > center.x or mouseY > center.y:
		stroke(200,100,50)	# red
	else:
		stroke(0)			# black
	strokeWeight(6)
	point(mouseX,mouseY)
