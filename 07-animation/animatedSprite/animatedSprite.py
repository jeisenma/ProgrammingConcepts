# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# Adapted from James Paterson's example: http://processing.org/examples/sequential.html

import glob	# useful for collecting files using a wildcard (i.e. PT_anim*.gif)
path = "C:/Users/jeisenma/Documents/GitHub/ProgrammingConcepts/07-animation/animatedSprite/"
images = []

def setup():
	size(200,200)
	imageFiles = glob.glob('%sdata/PT_anim*.gif'%path)
	for imageFile in imageFiles:
		images.append( loadImage(imageFile) )

def draw():
	whichOne = frameCount % len(images)
	image( images[whichOne], 0, 0 )