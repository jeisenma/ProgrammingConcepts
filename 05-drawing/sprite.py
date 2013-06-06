cat = loadImage("sprite.png")

def setup():
	size(400,400)
	
def draw():
	global cat
	background(255)
	imageMode(CENTER)
	image(cat, mouseX, mouseY)
	
