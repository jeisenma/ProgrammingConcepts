from sets import Set

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
		for i,row in enumerate(table.rows()): 							# iterate over the rows
			datum = row.getString(country).replace(',','')	# remove commas from numbers, i.e. 1,000 becomes 1000
			if len(datum) > 0:
				data[country][year] = float(datum) 		# convert the datum to floating point, add to the list
	
	# if there are less than 2 data points for a country, throw that country's list away
	for country in data.keys():
		if len(data[country]) < 2:
			data.pop(country,None)
			
	return data, years

def findCommon(list1, list2, list3):
	return sorted(list( Set(list1).intersection(list2).intersection(list3) ) )
	
def getData():
	# collect dictionaries with the data from each file
	gdpData, gdpYears = loadDataFromCSV('gdp.csv')
	lifeData, lifeYears = loadDataFromCSV('lifeExpectancy.csv')
	popData, popYears = loadDataFromCSV('population.csv')
	
	# find the countries and years that are listed in ALL the tables
	countries = findCommon( gdpData.keys(), lifeData.keys(), popData.keys() )
	years = findCommon( gdpYears, lifeYears, popYears )
	
	return countries, years, gdpData, lifeData, popData

def setup():
	global countries, years, gdpData, lifeData, popData, gdpBounds, lifeBounds, popBounds
	countries, years, gdpData, lifeData, popData = getData()
	gdpBounds = findBounds(gdpData)
	lifeBounds = findBounds(lifeData)
	popBounds = findBounds(popData)
	
	#print countries
	#print years
	size(800,600)

def interpData( dataDict, matchList, searchVal ):		# need to re work this for dictionary
	for i,item in enumerate(matchList):
		print "\tsearch for %f against %d with data %f"%(searchVal, item, dataList[i])
		if searchVal < item:
			print "FOUND! ", map( searchVal, matchList[i-1], matchList[i], dataList[i-1], dataList[i] ) 
			return map( searchVal, matchList[i-1], matchList[i], dataList[i-1], dataList[i] )
	return 0

def findBounds( dataDict ):
	bounds = [9999999,-999999]
	for key in dataDict.keys():
		for val in dataDict[key]:
			if val < bounds[0]:
				bounds[0] = val	# new min
			if val > bounds[1]:
				bounds[1] = val	# new max
	return bounds
	
def draw():
	background(200)
	
	circleArea = [10,2000]	# arbitrarily choosing the biggest possible circle size
	
	year = map(mouseX, 0, width, years[0], years[-1])	# find the year based on horizontal mouse position
	
	fill(160)
	textSize(300)
	textAlign(CENTER,CENTER)
	text( "%d"%round(year), width/2, height/2 )
	
	fill(255)
	for country in countries:
		print country
		gdp = log(interpData( gdpData[country], years, year ))
		life = interpData( lifeData[country], years, year )
		pop = interpData( popData[country], years, year )
		x = map( gdp, log(gdpBounds[0]), log(gdpBounds[1]), 0, width )
		y = map( life, lifeBounds[0], lifeBounds[1], height, 0 )
		a = map( pop, popBounds[0], popBounds[1], circleArea[0], circleArea[1] )
		diameter = sqrt(a/PI)*2	
		ellipse( x, y, diameter, diameter )
	
