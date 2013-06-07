# J Eisenmann 2013 
# jeisenma@accad.osu.edu

class Shape:
	def __init__(self, p=PVector(), n=8, r=40, oscilAmp=0.0, oscilFrq=4, nzFrq=0, part=0):
		self.p = p
		self.n = n
		self.r = r
		self.oa = oscilAmp
		self.of = oscilFrq
		self.nz = nzFrq
		self.part = part
		self.update()

	def update(self):
		self.pts = []
		for i in range(self.n):
			center = PVector(self.p.x, self.p.y);
			angle = map( i, 0, self.n, 0, TWO_PI-self.part)
			pt = PVector( self.r*sin(angle), self.r*cos(angle) )
			pt.mult(  	map( sin( float(i)/self.n*self.of ), -1, 1, 0, self.oa) * 
						noise( float(i)/self.n*self.nz ) );
			pt.add(center)
			self.pts.append( pt )
			
	def draw(self):
		strokeWeight(8)						# thick outlines!
		fill(200,200,250)
		beginShape()
		vertex( self.pts[0].x, self.pts[0].y )
		for pt in self.pts:
			# ellipse(pt.x, pt.y, 5,5)	# to see what the vertices are doing
			curveVertex(pt.x, pt.y)
		curveVertex( self.pts[-1].x, self.pts[-1].y )
		endShape(CLOSE)
