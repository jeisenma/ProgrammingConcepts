# J Eisenmann 2013 
# jeisenma@accad.osu.edu

def setup():
    size(400,400)
	
def draw():
    background(100)
    translate(width/2, height/2)
    for i in range(frameCount/2):
        rotate(radians(10))
        ellipse(i*2,0,20,20)
