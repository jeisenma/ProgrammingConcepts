#########
# BRICK #
#########

from Rectangle import Rectangle
 
class Brick:
	def __init__( self, X, Y, W, H, HASSTROKE, STROKE, HASFILL, FILL):
		# BRICK PROPERTIES
		self.rectangle =  Rectangle(W, H, HASSTROKE, STROKE, HASFILL, FILL)
		self.rectangle.setPosition(X, Y)
		self.imAlive = True
		self.respawns = False
		self.timeToRespawn = 60 # time is in frames
		self.frame = 0
	
	def display( self ):
		if (self.imAlive):
			self.rectangle.display()
		else:
			if (self.respawns):
				self.frame += 1
				if(self.frame > self.timeToRespawn):
					# rise up from your grave, brick
					self.imAlive = True

	def die( self ) :
		self.imAlive = False
		self.frame = 0
	
	
	
