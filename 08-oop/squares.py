# J Eisenmann 2013 
# jeisenma@accad.osu.edu

squares = []

def setup():
    size(400,400)

def draw():
    background(255)
    for square in squares:
		square.spin()
		square.display()
		
def mousePressed():
    squares.append( Square(mouseX, mouseY) )
    
class Square:
	def __init__( self, mx, my ):
		self.position = PVector(mx,my)
		self.speed = random(0.01, 0.2)
		self.c = color(random(255), random(255), random(255))
		self.sz = random(10,100)
		self.angle = 0
	
	def spin( self ):
		self.angle += self.speed
	
	def display( self ):
		pushMatrix()
		fill(self.c)
		translate( self.position.x, self.position.y)
		rotate(self.angle)
		rect( 0, 0, self.sz, self.sz )
		popMatrix()

