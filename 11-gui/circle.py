class Circle:
	""" A simple circle class """
	def __init__(self, x, y, r):
		""" x,y indicate the center of the circle
			r is the radius """
		self.x = x
		self.y = y
		self.r = r
	
	def contains(self, x, y, tol=0):
		""" circle collision test for point x,y with tolerance tol """
		return dist(self.x, self.y, x, y) < self.r+tol
		
	def draw(self):
		""" draw the circle """
		ellipse(self.x, self.y, 2*self.r, 2*self.r)
