# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# the data
angles = [ 30, 10, 45, 35, 80, 38, 75, 47 ] 

def setup(): 
    global diameter
    size(640, 360)
    noStroke()
    diameter = min(width, height) * 0.75
    noLoop()    # Run once and stop -- no need for animation here
    
def draw(): 
    background(200,200,240)
    lastAngle = 0
    for angle in angles:
        # set the color of this slice based on the angle value (brighter is bigger)
        fill( map(angle, min(angles), max(angles), 0, 255) ) 				
        # draw an angle starting from the last slice
        arc(width/2, height/2, diameter, diameter, lastAngle, lastAngle+radians(angle))
        # keep track of where we left off, so we can start there next time
        lastAngle += radians(angle)    


