# J Eisenmann 2013 
# jeisenma@accad.osu.edu

greens = []		# a list to hold the green color values of each circle
numCircles = 12	# how many circles are there?

def setup():
    global greens
    size(400,400)
    # create a bunch of random numbers that will represent to green values 
    for i in range(numCircles):
        greens.append( random(255) )

def draw():
    background(200)
    # calculate the circle diameter based on screen width and number of circles
    diam = float(width)/numCircles
    # for every column...
    for i,g in enumerate(greens):
        # make the circles in this column a shade of green (based on the values in the "greens" list)
        fill( 100, g, 100 )
        # for every row
        for j in range( numCircles ):
            # draw a circle at the correct place
            ellipse( i*diam+diam/2, j*diam+diam/2, diam, diam )
