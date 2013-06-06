
def setup():
	size(400,400)
	
def draw():
	center = PVector(width/2, height/2)
	# if mouse is in bottom right hand corner
	if mouseX > center.x and mouseY > center.y:		
		stroke(255)			# white
	# if mouse is either in the right half or in the bottom half
	elif mouseX > center.y or mouseY > center.y:
		stroke(200,100,50)	# red
	else:
		stroke(0)			# black
	strokeWeight(3)
	point(mouseX,mouseY)
