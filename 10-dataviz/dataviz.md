--------------------------------

# Data Visualization: telling stories with data
--------------------------------

## Discussion
- Parsing your data: getting it into a usable format
	- Common data file types (csv, tab delimited, xls, xml)
	- File I/O
		- [loadStrings](http://www.processing.org/reference/loadStrings_.html)
		- [loadTable](http://www.processing.org/reference/loadTable_.html)
		- [loadXML](http://www.processing.org/reference/loadXML_.html)
	- Strings
		- [toUpperCase](http://www.processing.org/reference/String_toUpperCase_.html)/[toLowerCase](http://www.processing.org/reference/String_toLowerCase_.html)
		- [replaceAll](http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/String.html#replaceAll%28java.lang.String,%20java.lang.String%29)
		- [substring](http://www.processing.org/reference/String_substring_.html)
		- [startsWith](http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/String.html#startsWith%28java.lang.String%29)/[endsWith](http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/String.html#endsWith%28java.lang.String%29)
		- [split](http://www.processing.org/reference/split_.html)/[join](http://www.processing.org/reference/join_.html)
		- [trim](http://www.processing.org/reference/trim_.html)

## Examples
<table border="1">
<tr><td> Type </td><td> How </td><td> Interaction </td><td> Challenges </td><td> Example(s) </td></tr>

<tr><td> map </td><td> plot latitude/ longitude points </td><td> zooming, panning </td><td> multi-resolution </td><td> <a href="http://www.sf.biomapping.net/map.htm">biomapping</a> </td></tr>

<tr><td> time series </td><td> interpolation </td><td> scrubbing, selecting </td><td> easing </td><td> <a href="http://weatherspark.com">weatherspark</a> </td></tr>

<tr><td> associative relationships </td><td> connector splines </td><td> selecting </td><td> layout (spaghetti) </td><td> <a href="http://www.propublica.org/special/a-tangled-web">campaign money</a> </td></tr>

<tr><td> quantitative relationships </td><td> graphs (bar, pie, bubble, line, scatter) </td><td> selecting </td><td> clarity, accurate metaphor </td><td> <a href="http://www.climateinstitute.org.au/global-climate-leadership-review-2012.html/section/479">climate data</a> </td></tr>
</table>

[Load from CSV]: http://docs.python.org/2/library/csv.html
[Scrape from HTML]: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
[Connect to Twitter]: http://blog.blprnt.com/blog/blprnt/updated-quick-tutorial-processing-twitter

- Data scraping and parsing
	- [Load from CSV]() - load data from a CSV file 
	- [Scrape from HTML]() - scrapes data from HTML source
	- [Connect to Twitter]() - describes how to connect to twitter to run real time queries

- Making pictures with data
	- [Pie Chart](http://processing.org/learning/basics/piechart.html)
	- [Radial Bar Graph](id/examples.py?page=RadialBarGraph)
	- [Time Series](id/examples.py?page=TimeSeries)
	- [Scatter Plot](id/examples.py?page=ScatterPlot)
	- [Bubble Chart](id/examples.py?page=BubbleChart)
	- [Bar Graph](id/examples.py?page=SmoothBars)
	- [Connection Graph (cluster)](http://www.openprocessing.org/sketch/22525)
	- [Connection Graph (polar)](http://www.openprocessing.org/sketch/34748)

## Reading
 - [Tell a great story](http://flowingdata.com/2008/10/10/great-data-visualization-tells-a-great-story/)
 - [Inspiration](http://flowingdata.com/) (note: a lot of these are not interactive -- we're interested in the interactive ones)
 - Optional further reading/coding:
 	- [Visualizing Data by Ben Fry](http://books.google.com/books?id=6jsVAiULQBgC&lpg=PP1&pg=PP1#v=onepage&q&f=false)
 	- [Visualize This by Nathan Yau](http://books.google.com/books?id=CB9XRIv9oigC&lpg=PP1&dq=978-0470944882&pg=PP1#v=onepage&q&f=false)
 	- [Beautiful Visualization](http://books.google.com/books?id=TKh6fdlKwfMC&lpg=PP1&dq=978-1449379865&pg=PP1#v=onepage&q&f=false)
 	- [Data Driven Documents (d3)](http://d3js.org/) 
 	
## Some Data Sources
 - [data.gov](http://data.gov)
 - [the united nations](http://unstats.un.org/unsd/)
 - [us census bureau](http://www.census.gov/main/www/access.html)
 - [ocean portal](http://www.data.gov/communities/node/237/data_tools/feature)
 - [aviation weather data](http://aviationweather.gov/adds/)
 - [weatherspark climate trends](http://weatherspark.com/climatetrends/data)
 - [wikipedia](http://en.wikipedia.org/wiki/Wikipedia:Database_download)
 - [imdb](http://www.imdb.com/interfaces)

## Assignment DataViz Project
- You will build an interactive data viz sketch.  The sketch should allow users to explore data and learn about a story that matters to you.  You wil need to submit a proposal on Carmen before our next class that includes:
    - Project Description: who your audience is, what story you want to tell and why, and your chosen interaction style
    - References: data sources (must read data from a file or a server), images, videos, audio, articles, etc
    - Wireframe drawing that shows what a screenshot of your data viz might look like
    - Data flow and control flow diagrams
    - Tasklist: what you have to get done and a timeline for doing it
- The materials for your project (i.e. code, images, etc) will be due before class on the 16th, and we will be doing gallery style presentations in class that day

