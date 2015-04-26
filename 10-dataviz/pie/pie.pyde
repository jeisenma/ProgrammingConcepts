# J Eisenmann 2013
# jeisenma@accad.osu.edu

# the data file
dataFile = "pieData.csv"
# empty lists to hold the data (we'll use parallel lists for this example)
categories = []
amounts = []

def setup():
    global diameter
    size(540, 360)
    diameter = min(width, height) * 0.75
    strokeWeight(2)
    noLoop()    # Run once and stop -- no need for animation here
    # set the color mode to hue/saturation/brightness so we can set hue values based on the data
    colorMode(HSB, 255)
    # load in the data from file
    loadData()

def loadData():
    # with the data file open for reading ('r') and with nickname f...
    with open(dataFile, 'r') as f:
        # keep track of what line we're on
        lineNum = 0
        # for every line in the dataFile (lines come in as strings)
        for line in f:
            # if we are not on the first line (where the headings are)
            if lineNum > 0:
                # split the string at the comma and assign the first part to category, 
                # and the second part to amount
                category, amount = line.split(',')
                # convert amount to a number and add it to the list
                amounts.append(float(amount))
                # keep the category as a string and add it to the list
                categories.append(category)
            # count up
            lineNum += 1

def draw():
    background(200)
    # move to the center of the window
    translate(width / 2, height / 2)
    # keep track of angle
    lastAngle = 0
    # iterate over the amounts from the data file
    for amount in amounts:
        # calculate the angle by mapping from the total amount range to 360 degrees
        angle = map(amount, 0, sum(amounts), 0, 360)
        # set the hue of this color of this slice based on the amount value (saturation and brightness are both maxed out at 255)
        fill(map(amount, min(amounts), max(amounts), 20, 255),255,255)
        # draw an angle starting from the last slice (use the PIE mode to add strokes on all the edges)
        arc(0, 0, diameter, diameter, lastAngle, lastAngle + radians(angle), PIE)
        # keep track of where we left off, so we can start there next time
        lastAngle += radians(angle)
        
    # now we'll draw the key, move over to the right edge
    translate(width/2-60,0)
    # iterate over both the amounts and the categories using zip
    for amount, category in zip(amounts, categories):
        # choose the fill color the same way as we did last time
        fill(map(amount, min(amounts), max(amounts), 20, 255),255,255)
        # draw a rectangle
        rect(0, 0, 15, 15)
        # black text
        fill(0)
        # draw the category name inside the rectangle
        text(category, 3, 12)
        # move down a bit for the next one
        translate(0, 15)

