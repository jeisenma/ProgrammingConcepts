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

def draw():
    background(255)
    # draw the axes
    bd = 15		# border space
    stroke(0)
    fill(0)
    line( bd, height-bd, width-bd, height-bd )	  # x-axis
    textAlign(CENTER,TOP)
    text( "time", width/2, height-bd )					  # ALWAYS label your axes!
    line( bd, bd, bd, height-bd )	 # y-axis
    pushMatrix()
    rotate( radians(-90) )
    text( "temperature (F)", -width/2, 0 )
    popMatrix()
    
    # draw the data points
    strokeWeight(2)
    stroke( 0 )
    pd = data[0]		# previous data point
    for d in data:	  	# display the data set indicated by 'mode'
        # draw a line from previous point (pd) to current point (d)
        line(pd.x*width,pd.y*height, d.x*width,d.y*height) 
	pd = d.get()	# make a copy of this point so we can reference it next time as the previous point
	



