# J Eisenmann 2013 
# jeisenma@accad.osu.edu

## 1 
# def draw():
	# line(pmouseX, pmouseY, mouseX, mouseY)

## 2
# def draw():
	# pass
# def mouseDragged():
	# line(pmouseX, pmouseY, mouseX, mouseY)
	
## 3
# def setup():
	# size(400,400)
	# background(200)
# def draw():
	# pass
# def mouseDragged():
	# line(pmouseX, pmouseY, mouseX, mouseY)

## 4
# def setup():
	# size(400,400)
	# background(200)
# def draw():
	# pass
# def mouseDragged():
	# line(pmouseX, pmouseY, mouseX, mouseY)
# def keyPressed():
	# background(200)

## 5
# maxSW = 12
# def setup():
	# size(400,400)
	# background(200)
# def draw():
	# pass
# def mouseDragged():
	# strokeWeight(maxSW)
	# line(pmouseX, pmouseY, mouseX, mouseY)
# def keyPressed():
	# background(200)
	
## 6 
# maxSW = 12
# def setup():
	# size(400,400)
	# background(200)
# def draw():
	# pass
# def mouseDragged():
	# d = max(1, dist(pmouseX, pmouseY, mouseX, mouseY))
	# strokeWeight(d)
	# line(pmouseX, pmouseY, mouseX, mouseY)
# def keyPressed():
	# background(200)

## 7
# maxSW = 12
# def setup():
	# size(400,400)
	# background(200)
# def draw():
	# pass
# def mouseDragged():
	# d = max(1, dist(pmouseX, pmouseY, mouseX, mouseY))
	# strokeWeight(maxSW/d)
	# line(pmouseX, pmouseY, mouseX, mouseY)
# def keyPressed():
	# background(200)

## 8
maxSW = 12
sw = 0
def setup():
	size(400,400)
	background(200)
def draw():
	pass
def mouseDragged():
	global sw
	d = max(1, dist(pmouseX, pmouseY, mouseX, mouseY))
	sw += maxSW/d
	sw /=2
	strokeWeight(sw)
	line(pmouseX, pmouseY, mouseX, mouseY)
def keyPressed():
	background(200)
