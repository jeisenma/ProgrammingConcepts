# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# animation properties
rad = 30
recording = False
f = 0
motion = []

def setup():
    size(400,400)
    strokeWeight(2)
    motion.append( PVector(width/2, height-rad))

def draw():
    global f, recording
    background(200)
    
    # when recording...
    if(recording):
        fill(255,0,0)
        text("recording...", 10, 20)
        # get the positions of the mouse and save them as keyframes
        x = constrain(mouseX, rad, width-rad)
        y = constrain(mouseY, rad, height-rad)
        motion.append( PVector(x,y) )
        f = len(motion)-1

    # draw the ball
    fill(20,160,240)
    ellipse(motion[f].x, motion[f].y, 2*rad, 2*rad)
    
    if not recording:
        # advance the frame number
        f = (f+1)%len(motion)

def keyPressed():
    global f, recording, motion
    if(key == ' '):
        if not recording:
            motion = []
        # stop and start recording
        recording = not(recording)
        f = 0
    

