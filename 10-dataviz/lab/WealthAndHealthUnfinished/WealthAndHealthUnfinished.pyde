def loadDataFromCSV( csvFile ):
    # load the table once without header option to get contury names
    table = loadTable(csvFile, 'csv')
    countries = []
    years = []
    
    for i in range(1,table.getColumnCount()):	# gather the countries names into a list
        colHeading = table.getRow(0).getString(i).strip() 
        if len(colHeading) > 0:
            countries.append( colHeading )
    
    for rowHeading in table.getStringColumn(0):	# gather the countries names into a list
        rowHeading = rowHeading.strip()
        if len(rowHeading) > 0 and not rowHeading == "Year":
            years.append( int(rowHeading) )
    
    # load the table again with country names so we can use them as indices for the column data
    table = loadTable(csvFile, 'header')
    data = {}
    
    for country in countries:
        data[country] = {}									# create an empty list for each country
        for i,row in enumerate(table.rows()): 				# iterate over the rows
            datum = row.getString(country).replace(',','')	# remove commas from numbers, i.e. 1,000 becomes 1000
            if len(datum) > 0:
                data[country][years[i]] = float(datum) 		# convert the datum to floating point, add to the list

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
        map between them (linear search) """
    # make sure the years are sorted! 
    # the first year we have data for
    # the data in that first year

    # we haven't found it yet...
    # remember the last value visited (for mapping later)

    # if we passed it, map between the last value and this one

    # an exact match, just return it
    return 0

def findBounds( dataDict ):
    """ find the min and max values for each dataset, for 
        all countries and return them as a list of length 2 """
    # start with ridiculously high min and low max
    # for each country
    # for each data point
    # if lower than min
    # new min
    # if higher than max
    # new max
    return bounds
    
def mouseDragged():		# only change the year when dragging
    global year
    # find the year based on horizontal mouse position
    # constrain the years to the allowable range

def draw():
    background(255)

    noFill()
    rect(margin,margin,width-2*margin,height-2*margin)		# draw a border around the chart

    # arbitrarily choosing the circle size range
    
    # draw the current year in the bg

    for country in countries:
        # use a logarithmic scale for GDP (it grows exponentially)
        # calculate diameter based on the area of the circle
        # shade and area show the same data: population
        pass
    
