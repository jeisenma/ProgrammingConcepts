def loadDataFromCSV( csvFile ):
    # load the table once with the first row so we can get the country names
    table = loadTable(csvFile, 'csv')
    countries = []
    years = []
    
    for i in range(1,table.getColumnCount()):	# gather the countries names into a list
        colHeading = table.getRow(0).getString(i).strip() 
        if len(colHeading) > 0:
            countries.append( colHeading )
    
    for rowHeading in table.getStringColumn(0):	# gather the years into a list
        rowHeading = rowHeading.strip()
        if len(rowHeading) > 0 and not rowHeading == "Year":
            years.append( int(float(rowHeading)) )
    
    # load the table again with the 'header' option so we can use the country names as an index for the columns 
    table = loadTable(csvFile, 'header')
    data = {}
    
    for country in countries:
        data[country] = {} # create an empty dictionary for each country
        for i,row in enumerate(table.rows()): 			# iterate over the rows
            datum = row.getString(country).replace(',','')	# remove commas from numbers, i.e. 1,000 becomes 1000
            if len(datum) > 0:
                data[country][years[i]] = float(datum) 		# convert the datum to floating point, add to the dictionary, indexed by year

    # if there are less than 2 data points for a country, throw that country away
    for country in data.keys():
        if len(data[country]) < 2:
            data.pop(country,None)		# remove this country from the dictionary

    return data, years

def findCommon(list1, list2, list3):
    from sets import Set
    return sorted(list( Set(list1).intersection(list2).intersection(list3) ) )
    
def getData():
    # collect dictionaries with the data from each file
    gdpData, gdpYears = loadDataFromCSV('gdp.csv')
    lifeData, lifeYears = loadDataFromCSV('lifeExpectancy.csv')
    popData, popYears = loadDataFromCSV('population.csv')
    
    # find the countries and years that are listed in ALL the tables (intersection)
    countries = findCommon( gdpData.keys(), lifeData.keys(), popData.keys() )
    years = findCommon( gdpYears, lifeYears, popYears )
    
    return countries, years, gdpData, lifeData, popData

def setup():
    global margin, countries, year, years, gdpData, lifeData, popData, gdpBounds, lifeBounds, popBounds
    countries, years, gdpData, lifeData, popData = getData()
    gdpBounds = findBounds(gdpData)
    lifeBounds = findBounds(lifeData)
    popBounds = findBounds(popData)
    
    size(800,600)
    margin = 20
    year = years[0]
    

def interpData( dataDict, searchVal ):		
    """ Find the data point corresponding with the 
        year, or the surrounding two data points and 
        map between them (linear search is used) """
    allYears = sorted(dataDict.keys()) 			        # make sure the years are sorted! 
    prevYear = allYears[0]					# the first year we have data for
    prevVal = dataDict[prevYear]				# the data in that first year
    for yr in allYears:
        if searchVal > yr:					# we haven't found it yet...
            prevYear = yr					# remember the last value visited (for mapping later)
            prevVal = dataDict[yr]	
        elif searchVal < yr: 					# if we passed it, map between the last value and this one
            return map( searchVal, prevYear, yr, prevVal, dataDict[yr] )
        else:							# an exact match, just return it
            return dataDict[yr]
    return 0

def findBounds( dataDict ):
    """ find the min and max values for each dataset, for 
        all countries and return them as a list of length 2 """
    bounds = [9999999,-999999]					# start with ridiculously high min and low max
    for country in dataDict.keys():				# for each country
        for val in dataDict[country].values():	# for each data point
            if val < bounds[0]:					# if lower than min
                bounds[0] = val	# new min
            if val > bounds[1]:					# if higher than max
                bounds[1] = val	# new max
    return bounds
    
def mouseDragged():		# only change the year when dragging
    global year
    year = map(mouseX, margin, width-2*margin, years[0], years[-1])	# find the year based on horizontal mouse position
    year = constrain(year, years[0], years[-1])						# constrain the years to the allowable range

def draw():
    background(255)
    
    noFill()
    rect(margin,margin,width-2*margin,height-2*margin)		# draw a border around the chart
    
    circleArea = [10,10000]	# arbitrarily choosing the circle size range
    
    textSize(12)
    text( "GDP", width/2, height-margin*0.5 )
    pushMatrix()
    translate( margin*0.5, height/2 )
    rotate(-PI/2)
    text( "Life Expectancy", 0, 0 )
    popMatrix()
    textAlign(RIGHT,CENTER)
    text( "Population size is represented by circle area", width-margin, height-margin*0.5 ) 
    
    
    fill(210)
    textSize(300)
    textAlign(CENTER,CENTER)
    text( "%d"%round(year), width/2, height/2 )		# draw the current year in the bg
    
    for country in countries:
        gdp = log( interpData( gdpData[country], year ) )		# use a logarithmic scale for GDP (it grows exponentially)
        life = interpData( lifeData[country], year )
        pop = interpData( popData[country], year )
        x = map( gdp, log( gdpBounds[0] ), log( gdpBounds[1] ), margin, width-margin )	# use a logarithmic scale for GDP (it grows exponentially)
        y = map( life, lifeBounds[0], lifeBounds[1], height-margin, margin )
        a = map( pop, popBounds[0], popBounds[1], circleArea[0], circleArea[1] )
        diameter = sqrt(a/PI)*2		# calculate diameter based on the area of the circle
        fill( map( a, circleArea[0], circleArea[1], 100, 255) )				# shade and area show the same data: population
        ellipse( x, y, diameter, diameter )
    
