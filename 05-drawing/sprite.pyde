# J Eisenmann 2013 
# jeisenma@accad.osu.edu

def setup():
    global cat
    cat = loadImage("sprite.png")
    size(400,400)
	
def draw():
    background(255)
    imageMode(CENTER)
    image(cat, mouseX, mouseY)
	
