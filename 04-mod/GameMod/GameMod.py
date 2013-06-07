# Breakout 
# 
# adapted by J Eisenmann (05/2013)
# from the java version by Steph Thirion (02/2007)
# Game Mod workshop: < http:#trsp.net/teaching/gamemod >

bricks = []
balls = []
frameNum = 0

# SCREEN PROPERTIES 
screenWidth = 400
screenHeight = 400
backgroundColor = color(48,48,48)
backgroundRefreshes = False

# GAME FRAME PROPERTIES
gameFrameWidth = 300
gameFrameHeight = 300
gameFrameStroke = color(255,255,255)
gameFrameHasStroke = False
gameFrameFill = color(0,0,0)
opacityOfRefresh = 255
gameFrameRefreshes = True

recX = (screenWidth-gameFrameWidth)/2
recY = (screenHeight-gameFrameHeight)/2

from Rectangle import Rectangle
from Ball import Ball
from Brick import Brick
from Paddle import Paddle

gameFrame = Rectangle(gameFrameWidth, gameFrameHeight, gameFrameHasStroke, gameFrameStroke, True, gameFrameFill)
paddle =  Paddle(gameFrameWidth)

# SETUP FUNCTION --
def setup():
	size(screenWidth,screenHeight)
	background(backgroundColor)
	
	# create objects
	gameFrame.opacity = opacityOfRefresh
	createBricks()
	createBalls()

# DRAW FUNCTION --
def draw():
	# BACKGROUND
	if(backgroundRefreshes):
		background(backgroundColor)
	
	translate(recX, recY)

	# GAME FRAME
	if(gameFrameRefreshes):
		gameFrame.display()
	
	# PADDLE
	paddle.display(recX)
	
	# BRICKS
	for i in range( len(bricks) ):
		bricks[i].display()
	
	# BALLS
	for i in range( len(balls) ):
		balls[i].display( paddle, bricks )

	saveScreenshots()

def createBalls():
	# BALL(S) PROPERTIES --
	numberOfBalls = 1
	yBalls = 150
	limits = [0, 0, gameFrameWidth, gameFrameHeight]
	for i in range(numberOfBalls):
		x = i*20
		balls.append( Ball(x, yBalls, limits) )

def createBricks():
	# BRICK GROUP PROPERTIES --
	numberOfBricks = 60
	bricksPerRow = 10
	brickWidth = gameFrameWidth/bricksPerRow
	brickHeight = 10
	brickHasStroke = False
	brickStroke = (255)
	brickHasFill = True
	brickFill = (255,0,0)
	yBricks = 50
	rowsColors = [	color(255,0,255), 
					color(255,0,0), 
					color(255,153,0), 
					color(255,255,0), 
					color(0,255,0), 
					color(0,255,255)	]
	
	# CREATE BRICKS
	for i in range(numberOfBricks):
		rowNum = i/bricksPerRow
		# coords
		x = brickWidth*i
		x -= rowNum*bricksPerRow*brickWidth
		y = yBricks+i/bricksPerRow*brickHeight
		# 
		num = min(rowNum, len(rowsColors)-1)
		rowColor = rowsColors[num]
		# create brick
		bricks.append( Brick(x, y, brickWidth, brickHeight, brickHasStroke, brickStroke, brickHasFill, rowColor) )

# be careful with this function - only change if you know what you're doing
# the hard disk could fill up with images in a few minutes
#
#
# press the 'G' key to save frames in TGA pictures in 'saved' folder

def saveScreenshots():
	global frameNum
	frameNum += 1
	if (keyPressed):
		if (key == ord('g') or key == ord('G')) :
			if(frameNum%2==0):
				saveFrame("saved/frame-####.tga")
