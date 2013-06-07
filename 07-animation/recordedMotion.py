# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# animation properties
rad = 30
recording = False
f = 0
numFrames = 800
motion = []

def setup():
	size(400,400)
	strokeWeight(2)
	
	global pos
	pos = PVector(width/2,height-rad)
	
	# fill keyframes with starting position
	for i in range(numFrames):
		motion.append( PVector(pos.x,pos.y) )


def draw():
	global f, recording
	background(200)
	
	# when recording...
	if(recording):
		fill(255,0,0)
		text("recording...", 10, 20)
		# get the positions of the mouse and save them as keyframes
		motion[f].x = constrain(mouseX, rad, width-rad)
		motion[f].y = constrain(mouseY, rad, height-rad)
	
	
	# draw the ball
	fill(20,160,240)
	ellipse(motion[f].x, motion[f].y, 2*rad, 2*rad)
	
	# advance the frame number
	f = (f+1)%numFrames
	# if we've reached the end of recording frames, stop recording
	if(f == 0 and recording):
		recording = False


def keyPressed():
	global f, recording
	if(key == ' '):
		# stop and start recording
		recording = not(recording)
		f = 0
	

