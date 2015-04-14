# J Eisenmann 2013
# jeisenma@accad.osu.edu

# create a list for storing snowmen
snowmen = []

def setup():
    size(800,400)

def draw():
    background(240,240,250)
    # draw all the snowmen in the list
    for snowman in snowmen:
        snowman.draw()
        
def mousePressed():
    # fake depth with size (small in the back, large in the front)
    howBig = map(mouseY, 0, height, 1, 100)
    # make a new snowman and add it to the list
    snowmen.append( Snowman(    PVector(mouseX, mouseY), howBig,
                                segments=round(random(2,3))
                            ) )

class Snowman:
    """ Snowman class: draws a snowman """
    def __init__(   self,
                    pos,
                    base,
                    segments=3,
                    shade=255
                ):
        """ segments: number of body parts (typically 3)
            shade: fill color of snowman (typically white)
            base: diameter of the base segment
            pos: position of the bottom of the snowman """
        self.segments = segments
        self.shade = shade
        self.base = base
        self.pos = pos
    
    def draw(self):
        """ draws the snowman """
        fill(self.shade)
        pushMatrix()
        translate(self.pos.x,self.pos.y)
        for i in range(int(self.segments)):
            # make the diameter decrease when i increases
            diam = map(i, 0, self.segments-1, self.base, self.base*0.35)
            translate(0,-diam/2)
            ellipse(0,0,diam,diam)
            translate(0,-diam*0.4)
        popMatrix();

