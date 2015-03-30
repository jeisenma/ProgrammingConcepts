########
# BALL #
########

from Rectangle import *

class Ball:
	def __init__ ( self, X, Y, limits) :
		self.width = 5							# dimensions
		self.height = 5
		self.hasStroke = False					# color properties
		self.strokeColor = color(255,255,255)
		self.hasFill = True
		self.fillColor = color(255,255,255)
		self.velX = 3							# initial velocity
		self.velY = 3
		
		self.x = X
		self.y = Y
		self.limits = limits
		self.ox = X
		self.oy = Y
		self.xcenter = X
		self.ycenter = Y
		self.rectangle = Rectangle(self.width, self.height, self.hasStroke, self.strokeColor, self.hasFill, self.fillColor)
		self.rectangle.setPosition(self.x, self.y)
	
	def display( self, paddle, bricks ):
		self.updatePosition( paddle, bricks )
		self.rectangle.display()
	
	def updatePosition( self, paddle, bricks ) :
		# add velocity to position
		self.x += self.velX
		self.y += self.velY
		# collision with limits
		if(self.x <= self.limits[0] or self.x >= self.limits[2]-self.width):
			self.velX = -self.velX
			self.x = constrain(self.x, self.limits[0], self.limits[2]-self.width)
		
		if(self.y <= self.limits[1] or self.y >= self.limits[3]-self.height):
			self.velY = -self.velY
			self.y = constrain(self.y, self.limits[1], self.limits[3]-self.height)
		
		self.xcenter = self.x+self.width/2
		self.ycenter = self.y+self.height/2
		# collision with paddle
		result = self.checkCollisionWithRectangle(paddle.rectangle)
		# if collides on top, control direction of ball
# 		if (result == 1):
# 			if(self.xcenter < paddle.rectangle.x1+paddle.rectangle.width/2):
# 				if(self.velX>0):
# 					self.velX = -self.velX
# 			else:
# 				if(self.velX<0):
# 					self.velX = -self.velX

		# collision with bricks
		if (result == 0) :
			for i in range( len(bricks) ):
				if(bricks[i].imAlive):
					res = self.checkCollisionWithRectangle(bricks[i].rectangle)
					if not(res == 0):
						bricks[i].die()
						break
		self.ox = self.x
		self.oy = self.y
		self.rectangle.setPosition(self.x, self.y)
	
	def checkCollisionWithRectangle( self, R ):
		""" Collision Detection Function
			result: 0 = no collision, 1 = top, 2 = right, 3 = bottom, 4 = left, 5 = couldn't detect which side """
		result = 0
		if (R.doesPointTouchMe(self.xcenter, self.ycenter)):
			# which side did it collide
			trajectory = LineSeg(self.xcenter,self.ycenter,self.ox+self.width/2,self.oy+self.height/2)
			result = R.whatSideDoesLineTouch(trajectory, self.velX, self.velY)
			# top
			if(result==1):
				self.velY = -self.velY
				self.y = R.y1-self.height
			# right
			elif(result==2):
				self.velX = -self.velX
				self.x = R.x2
			# bottom
			elif(result==3):
				self.velY = -self.velY
				self.y = R.y2
			# left
			elif(result==4):
				self.velX = -self.velX
				self.x = R.x1-self.width
			else:
				result = 5
		return result
	
	

