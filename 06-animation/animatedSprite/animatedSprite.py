# Adapted from James Paterson's example: http://processing.org/examples/sequential.html

import glob

def setup():
	size(200,200)
	global images
	images = []
	imageFiles = glob.glob('C:/Users/jeisenma/Dropbox/Teach/ProgrammingConceptsForArtistsAndDesigners/examples/p5py/animatedSprite/data/PT_anim*.gif')
	for imageFile in imageFiles:
		images.append( loadImage(imageFile) )

def draw():
	global images
	whichOne = frameCount % len(images)
	image( images[whichOne], 0, 0 )