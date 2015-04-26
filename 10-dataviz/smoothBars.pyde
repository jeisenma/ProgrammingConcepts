def setup():
    global bg
    size(400,400)
    # create some labels
    someLabels = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ] 
    # create some random numbers between 0 and 1000
    someNumbers = []
    for i in range(10):
        someNumbers.append( random(0,1000) ) 
    # create a bar graph object with those labels and numbers
    bg = BarGraph(someLabels, someNumbers)
    
def draw():
    background(150)
    bg.update()
    bg.display()
    
def mousePressed():
    # generate random data between [0,1000] for the graph -- this could 
    # be replaced with code that switches between different datasets
    someNumbers = []
    for i in range(10):
        someNumbers.append( random(0,1000) ) 
    bg.changeData(someNumbers)
    
class BarGraph:
    def __init__( self, L, D ):
        self.labels = []	# labels for the bars
        self.data = []		# data displayed at the current frame
        self.oldData = []	# where we came from - used for interpolation
        self.newData = []	# where we're going - used for interpolation
        self.margin = 30	# margin around the edges of the sketch
        self.spacing = 5	# space between bars
        self.timer = 0.0	# time used for interpolation
        self.duration = 1.0	# how long the interpolation should take
        self.labels = []	# make space for our arrays
        # copy the parameter values to our arrays
        for i in range(len(L)):
            self.labels.append( L[i] )
            self.data.append( D[i] )
            self.oldData.append( D[i] )
            
    def changeData( self, newNumbers ):
        """ change the data set this bar graph displays """
        # copy the current data over to the oldData so we know where we're coming from
        for i,d in enumerate(self.data):
            self.oldData[i] = d 
        # put the data into the newData array for interpolating to
        self.newData = []
        for i in range(len(self.data)):
            self.newData.append( newNumbers[i] ) 
        # start the interpolation timer (counting down)
        self.timer = self.duration
        
    def update( self ):
        if(self.timer > 0.0):	   # if timer is still going
            for i in range(len(self.data)):	# interpolate between old and data
                # linear interpolation -- gradual, but not smooth
                #data[i] = lerp(oldData[i], newData[i], map(timer, duration, 0, 0, 1))	
                # cubic interpolation -- smooth and sexy
                self.data[i] = cubicEase( self.duration-self.timer, self.oldData[i], self.newData[i], self.duration)	
            self.timer = self.timer - 1.0/frameRate	 # timer counting down
	
    def display( self ):
        w = (width-2*self.margin)/len(self.data)	# figure out how wide each bar should be
        w -= self.spacing						# add space between each bar
        for i,d in enumerate(self.data):
            x = self.margin + (w + self.spacing)*i
            y = height-self.margin
            # negative height draws rectangles up from the bottom left corner (instead of down from top right corner)
            h = -map( d, 0, 1000, 0, height-2*self.margin )
            rect( x, y, w, h )
            text( self.labels[i], x+w/2, y+20 )

# utility function	
def cubicEase( time, startingPoint, stoppingPoint, dur ):
    """ smooth interpolation between (startingPoint) and (stoppingPoint)
        parameters are: time, startingPoint, stoppingPoint, duration """
    distance = stoppingPoint - startingPoint
    time = time / dur-1
    return distance * ( time**3 + 1) + startingPoint
	


