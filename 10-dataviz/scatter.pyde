# two X,Y datasets
data1 = [ PVector(0.1825,0.6675),
          PVector(0.1825,0.6675),
          PVector(0.4075,0.7575),
          PVector(0.3,0.62),
          PVector(0.5,0.5),
          PVector(0.445,0.4825),
          PVector(0.8225,0.1825) ]

data2 = [ PVector(0.2225,0.1825),
          PVector(0.2225,0.1825),
          PVector(0.17,0.34),
          PVector(0.375,0.2175),
          PVector(0.3125,0.6075),
          PVector(0.535,0.415),
          PVector(0.655,0.3775),
          PVector(0.4325,0.31),
          PVector(0.665,0.23),
          PVector(0.7325,0.395),
          PVector(0.6175,0.5975),
          PVector(0.625,0.6025),
          PVector(0.8825,0.7325),
          PVector(0.725,0.7775),
          PVector(0.7975,0.8825),
          PVector(0.885,0.8675) ]

data = []
dataColors = []
dataLabels = []

blendTimer = 0		# smoothly blends between the data sets
startTimer = 30		# how long the blend should last (in frames)
mode = 0          # which data set to display
pmode = 0          # previous mode

def setup():
    size(400,400)
    data.append( data1 )
    dataColors.append( color(255,150,5) )
    dataLabels.append( "USA" )
    data.append( data2 )		# data is 2 dimensional
    dataColors.append( color(5,150,150) )
    dataLabels.append( "UK" )

def draw():
    global blendTimer
    background(255)
    # draw the axes
    bd = 15		# border space
    stroke(0)
    fill(0)
    line( bd, height-bd, width-bd, height-bd )	  # x-axis
    textAlign(CENTER,TOP)
    text( "cats", width/2, height-bd )          		  # ALWAYS label your axes!
    line( bd, bd, bd, height-bd )	 # y-axis
    pushMatrix()
    rotate( radians(-90) )
    text( "rain (inches per day)", -width/2, 0 )
    popMatrix()
    
    # draw the data points, using transparency to fade in current data set
    transparency = map(blendTimer, 0, startTimer, 255, 0)
    stroke( 0, transparency )
    fill( dataColors[ mode ], transparency )
    # display the data set indicated by 'mode'
    for d in data[ mode ]:	  
        ellipse( d.x*width, d.y*height, 5, 5 ) 
	
    # if fading, draw the old data points, using transparency to fade out other data set
    if blendTimer > 0 :
        transparency = map(blendTimer, 0, startTimer, 0, 255)
        stroke( 0, transparency )
        fill( dataColors[ mode ], transparency )
        for d in data[ pmode ]:	   # display the data set indicated by 'mode'
            ellipse( d.x*width, d.y*height, 5, 5 ) 
	blendTimer = max( 0, blendTimer-1 )
	
    # draw data selector buttons
    stroke(0)
    for i in range(len(data)):
        fill( dataColors[i] )
        ellipse( width - (i+0.5)*40, 20, 30, 30 )
        fill( 255 )
        textAlign(CENTER,CENTER)
        text( dataLabels[i], width - (i+0.5)*40, 20 )

def mousePressed():
    global pmode, mode, blendTimer
    # figure out if mouse is over any of the data selector buttons
    for i in range(len(data)):
        if dist(mouseX, mouseY, width - (i+0.5)*40, 20) <= 30 :
            pmode = mode # remember the previous mode
            mode = i	# change the mode accordingly
            blendTimer = startTimer
            
