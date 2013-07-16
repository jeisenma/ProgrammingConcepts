class Rect:
	""" A simple rectangle class """
	def __init__(self, x, y, w, h, r=0):
		""" x,y indicate the top left corner
			w,y indicate the dimensions 
			r is an optional paramater for the radius of rounded corners (default is 0)"""
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.r = r
	
	def contains(self, x, y, tol=0):
		""" rectangle collision test for point x,y with tolernace tol
			(rounded corners are ignored for this test """
		return (x > self.x-tol and 
				x < self.x+self.w+tol and 
				y > self.y-tol and 
				y < self.y+self.h+tol)
	
	def draw(self):
		""" draw the rectangle """
		rect(self.x, self.y, self.w, self.h, self.r)


