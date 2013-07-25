# adapted from the following examples:
# - the video capture example http://processing.org/reference/libraries/video/Capture.html
# - the blob detection example http://www.v3ga.net/processing/BlobDetection/index-page-download.html
# - the video background subtraction example https://github.com/processing/processing/tree/master/java/libraries/video/examples/Capture/BackgroundSubtraction

from processing.video import Capture
from blobDetection import BlobDetection

def setup():
	global cam, theBlobDetection, numPixels, backgroundPixels, newFrame, mode, bg, img
	mode = 0
	size(640/2, 480/2)
	cameras = Capture.list()
	
	if len(cameras) == 0:
		print("There are no cameras available for capture.")
		exit()
	else:
		print("Available cameras:")
		for i,camera in enumerate(cameras):
			print(i,camera)
	
	# The camera can be initialized directly using an 
	# element from the array returned by list():
	cam = Capture(this, cameras[7])
	cam.start()
	newFrame = False	# is the frame ready yet?
	
	# BlobDetection
	img = PImage(width,height)
	bg = PImage(width,height)  
	theBlobDetection = BlobDetection(img.width, img.height)
	theBlobDetection.setPosDiscrimination(True)
	theBlobDetection.setThreshold(0.2) # will detect bright areas whose luminosity > 0.2f;
  
  	# Background subtraction
	numPixels = width * height;
	backgroundPixels = [0]*numPixels  # Create a list to store the background image
	loadPixels();

def draw():
	global newFrame
	if cam.available():
		cam.read()
		newFrame = True
	
	if newFrame:
		newFrame = False;
	if mode == 0:
		image(bg,0,0,width,height)  
		text("bg image", 20, 20) 
	elif mode == 1:
		image(cam,0,0,width,height)  
		text("camera image", 20, 20) 
	elif mode == 2:
		bgSub()
		img.loadPixels()
		for i,pix in enumerate(pixels):
			img.pixels[i] = pixels[i]
		img.updatePixels()
		fastblur(img, 2)
		theBlobDetection.computeBlobs(img.pixels)
		drawBlobsAndEdges(True,True)
#		image(cam, 0, 0)
		text("with bg subtracted", 20, 20)

def bgSub():
	# Difference between the current frame and the stored background
    presenceSum = 0
    for i in range(numPixels): # For each pixel in the video frame...
		# Fetch the current color in that location, and also the color of the background in that spot
		currColor = cam.pixels[i]
		bkgdColor = backgroundPixels[i]
		# Extract the red, green, and blue components of the current pixel?s color
		currR = (currColor >> 16) & 0xFF
		currG = (currColor >> 8) & 0xFF
		currB = currColor & 0xFF
		# Extract the red, green, and blue components of the background pixel?s color
		bkgdR = (bkgdColor >> 16) & 0xFF
		bkgdG = (bkgdColor >> 8) & 0xFF
		bkgdB = bkgdColor & 0xFF
		# Compute the difference of the red, green, and blue values
		diffR = abs(currR - bkgdR)
		diffG = abs(currG - bkgdG)
		diffB = abs(currB - bkgdB)
		# Add these differences to the running tally
		presenceSum += diffR + diffG + diffB;
		# Render the difference image to the screen
		pixels[i] = color(diffR, diffG, diffB);
		# The following line does the same thing much faster, but is more technical
		#pixels[i] = 0xFF000000 | (diffR << 16) | (diffG << 8) | diffB;
    updatePixels() # Notify that the pixels[] array has changed
    #print(presenceSum) # Print out the total amount of movement

def keyPressed():
	global mode, backgroundPixels
	if(key == ' '):
		cam.loadPixels()
		for i,pix in enumerate(cam.pixels):
			backgroundPixels[i] = cam.pixels[i]
		bg.copy(cam, 0, 0, cam.width, cam.height, 
					 0, 0, bg.width, bg.height)
	else:
		mode = (mode+1)%3

def drawBlobsAndEdges(drawBlobs, drawEdges):
	noFill()
	for n in range(theBlobDetection.getBlobNb()):
		b=theBlobDetection.getBlob(n)
		if b != None:
			if drawEdges:
				strokeWeight(3)
				stroke(0,255,0)
				for m in range(b.getEdgeNb()):
					eA = b.getEdgeVertexA(m)
					eB = b.getEdgeVertexB(m)
					if (eA != None and eB != None):
						line(
							  eA.x*width, eA.y*height, 
							  eB.x*width, eB.y*height
						  	)

				# Blobs
				if drawBlobs:
					strokeWeight(1)
					stroke(255,0,0)
					rect(
						  b.xMin*width,b.yMin*height,
						  b.w*width,b.h*height
					  	)

"""
// ==================================================
// Super Fast Blur v1.1
// by Mario Klingemann 
// <http://incubator.quasimondo.com>
// ==================================================\
"""
def fastblur( img, radius):
	if (radius<1):
		return
	w=img.width
	h=img.height
	wm=w-1
	hm=h-1
	wh=w*h
	div=radius+radius+1
	r = [0]*wh
	g = [0]*wh
	b = [0]*wh
	vmin = [0]*max(w,h)
	vmax = [0]*max(w,h)
	pix = [0]*len(img.pixels)
	dv = [0]*256*div
	for i in range(256*div):
		dv[i] = i/div
	yw = 0
	yi = 0
	
	for y in range(h):
		rsum=0
		gsum=0
		bsum=0
		for i in range(-radius,radius+1):
			p=pix[yi+min(wm,max(i,0))]
			rsum +=(p & 0xff0000)>>16
			gsum +=(p & 0x00ff00)>>8
			bsum += p & 0x0000ff
		for x in range(w):
			r[yi]=dv[rsum]
			g[yi]=dv[gsum]
			b[yi]=dv[bsum]

			if(y==0):
				vmin[x]=min(x+radius+1,wm)
				vmax[x]=max(x-radius,0)
			p1=pix[yw+vmin[x]]
			p2=pix[yw+vmax[x]]

			rsum+=((p1 & 0xff0000)-(p2 & 0xff0000))>>16
			gsum+=((p1 & 0x00ff00)-(p2 & 0x00ff00))>>8
			bsum+= (p1 & 0x0000ff)-(p2 & 0x0000ff)
			yi+=1
		yw+=w

	for x in range(w):
		rsum=0
		gsum=0
		bsum=0
		yp=-radius*w
		for i in range(-radius,radius+1):
			yi = max(0,yp)+x
			rsum+=r[yi]
			gsum+=g[yi]
			bsum+=b[yi]
			yp+=w
		yi=x
		for y in range(h):
			pix[yi]=0xff000000 | (dv[rsum]<<16) | (dv[gsum]<<8) | dv[bsum]
			if(x==0):
				vmin[y]=min(y+radius+1,hm)*w
				vmax[y]=max(y-radius,0)*w
			p1=x+vmin[y]
			p2=x+vmax[y]

			rsum+=r[p1]-r[p2]
			gsum+=g[p1]-g[p2]
			bsum+=b[p1]-b[p2]

			yi+=w
