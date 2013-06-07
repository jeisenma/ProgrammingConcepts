#############
# RECTANGLE #
#############

class Rectangle :
	""" In this game every visible object is a Rectangle
		(ball, paddle, bricks, even the game frame)
		are represented by a Rectangle object """
	def __init__ (self, w, h, hasStroke, stroke, hasFill, fill):
		self.width = w
		self.height = h
		self.x1 = 0
		self.y1 = 0
		self.x2 = self.x1+self.width
		self.y2 = self.y1+self.height
		self.hasStroke = hasStroke
		self.strokeColor = stroke
		self.hasFill = hasFill
		self.fillColor = fill
		self.opacity = 255

	def setPosition( self, X, Y) :
		self.x1 = X
		self.y1 = Y
		self.x2 = self.x1+self.width
		self.y2 = self.y1+self.height

	def display( self ):
		""" Display:
			Draws the rectangle to the screen """
		# stroke
		if (self.hasStroke) :
			stroke(self.strokeColor)
		else:
			noStroke()
		# fill
		if (self.hasFill) :
			fill(self.fillColor, self.opacity)
		else:
			noFill()
		rect(self.x1, self.y1, self.width, self.height)

	def doesPointTouchMe ( self, px,  py):
		""" Collision detection: 
			Is the point given by (px, py) inside this rectangle? """
		result = False
		if (px >= self.x1 and px <= self.x2) :
			if (py >= self.y1 and py <= self.y2) :
				result = True
		return result

	def whatSideDoesLineTouch ( self, LINE, VELX, VELY):
		""" Collision detection:
			Given a line segment and a velocity, decide which side was touched """
		# top (1) / bottom (3)
		if (VELY>0):
			side = LineSeg(self.x1,self.y1,self.x2,self.y1)
			if(LINE.intersectsLine(side)):
				return 1
			
		elif (VELY<0):
			side = LineSeg(self.x1,self.y2,self.x2,self.y2)
			if(LINE.intersectsLine(side)):
				return 3
		
		# left (4) / right (2)
		if (VELX>0):
			side = LineSeg(self.x1,self.y1,self.x1,self.y2)
			if(LINE.intersectsLine(side)):
				return 4
		elif (VELX<0):
			side = LineSeg(self.x2,self.y1,self.x2,self.y2)
			if(LINE.intersectsLine(side)):
				return 2
		return 0
		
class LineSeg:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.len = sqrt( (x2-x1)**2 + (y2-y1)**2 )
	
	def intersectsLine(self, other):
		""" Detects if one line segment intersects another
			adapted from: http://alienryderflex.com/intersect/ """
		# Fail if either line segment is zero-length.
		if( self.len == 0 or other.len == 0 ):
			return False
		# Fail if the segments share an end-point.
		elif( ( self.x1 == other.x1 and self.y1 == other.y1 ) or
			  ( self.x2 == other.x2 and self.y2 == other.y2 ) or
			  ( self.x1 == other.x2 and self.y1 == other.y2 ) or
			  ( self.x2 == other.x1 and self.y2 == other.y1 ) ):
			return False
		# Shorten the notation
		ax = self.x1
		ay = self.y1
		bx = self.x2
		by = self.y2
		cx = other.x1
		cy = other.y1
		dx = other.x2
		dy = other.y2
		# Translate the system so that point A is on the origin.
		bx -= ax
		by -= ay
		cx -= ax
		cy -= ay
		dx -= ax
		dy -= ay
		# Rotate the system so that point B is on the positive X axis.
		theCos = bx/self.len
		theSin = by/self.len
		newX = cx*theCos + cy*theSin
		cy =   cy*theCos - cx*theSin
		cx = newX
		newX = dx*theCos + dy*theSin
		dy =   dy*theCos - dx*theSin
		dx = newX
		
		# Fail if segment C-D doesn't cross line A-B.
		if (cy < 0 and dy < 0) or (cy >= 0 and dy >= 0):
			return False
		
		# Discover the position of the intersection point along line A-B (using similar triangles)
		abPos = dx+(cx-dx)*dy/(dy-cy)
		
		# Fail if segment C-D crosses line A-B outside of segment A-B.
		if abPos < 0 or abPos > self.len:
			return False
		else:
			return True