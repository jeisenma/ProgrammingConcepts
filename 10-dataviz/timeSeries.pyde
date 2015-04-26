# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# X,Y data of temperature vs time
data = [ PVector(0.1175,0.2725),
         PVector(0.245,0.5075),
         PVector(0.3725,0.32),
         PVector(0.5125,0.71),
         PVector(0.61,0.52), 
         PVector(0.725,0.9175),
         PVector(0.81,0.555),
         PVector(0.8775,0.325) ]

def setup():
    size(400,400)
    textAlign(CENTER,TOP)
    stroke(0)
    

def draw():
    background(255)
    # draw the axes
    bd = 15		# border space
    fill(0)
    # x-axis
    line( bd, height-bd, width-bd, height-bd )	  
    text( "time", width/2, height-bd )	 # ALWAYS label your axes!
    
    # y-axis
    line( bd, bd, bd, height-bd )	 
    pushMatrix()            # rotate before drawing y-axis label
    rotate( radians(-90) )
    text( "temperature (F)", -width/2, 0 )
    popMatrix()
    
    # draw the data points as a series of vertices
    strokeWeight(2)
    noFill()
    beginShape()
    for d in data:
        vertex(d.x * width, d.y * height)
    endShape()

	



