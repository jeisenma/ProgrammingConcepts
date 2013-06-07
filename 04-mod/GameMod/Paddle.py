##########
# PADDLE #
##########

from Rectangle import Rectangle

class Paddle:
    def __init__ (self, frameWidth):
        """ set up the parameters of the paddle (which is really just a rectangle) """
        self.frameWidth = frameWidth
        self.width = 60
        self.height = 5
        self.hasStroke = False
        self.strokeColor = color(255,255,255)
        self.hasFill = True
        self.fillColor = color(255,255,255)
        self.x = frameWidth/2
        self.y = 270
        self.rectangle =  Rectangle(self.width, self.height, self.hasStroke, self.strokeColor, self.hasFill, self.fillColor)
        self.rectangle.setPosition(self.x, self.y)
    
    def display( self, recX ):
        self.updatePosition(recX)
        self.rectangle.setPosition(self.x, self.y)
        self.rectangle.display()
    
    def updatePosition( self, recX ) :
        self.x = mouseX-recX-self.rectangle.width/2
        self.x = constrain(self.x, 0, self.frameWidth-self.rectangle.width)
