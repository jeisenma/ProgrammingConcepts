# J Eisenmann 2013 
# jeisenma@accad.osu.edu

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



class Slider:
    """ A slider class.  Works for vertical or horizontal sliders """
    def __init__(self, place, minVal=0.0, maxVal=1.0):
        self.place = place
        self.minMax = [minVal, maxVal]
        self.isVertical = place.w < place.h    # is the slider vertical?
        self.value = minVal
        self.isDragging = False
        if self.isVertical:
            self.handle = Circle(     place.x+place.w/2, 
                                    place.y+place.h, 
                                    8 )
        else:
            self.handle = Circle(     place.x,
                                    place.y+place.h/2, 
                                    8 )
    
    def update(self):
        if self.isVertical:
            self.value = map(mouseY, self.place.y+self.place.h, self.place.y, self.minMax[0], self.minMax[1])
        else:
            self.value = map(mouseX, self.place.x, self.place.x+self.place.w, self.minMax[0], self.minMax[1])
        self.value = constrain(self.value, self.minMax[0], self.minMax[1])
            
    def draw(self):
        if self.isVertical:
            self.handle.y = map(self.value, 
                                self.minMax[0], self.minMax[1], 
                                self.place.y+self.place.h, self.place.y)
        else:
            self.handle.x = map(self.value, 
                                self.minMax[0], self.minMax[1], 
                                self.place.x, self.place.x+self.place.w)
        strokeWeight(4)
        if self.isVertical:
            line(     self.place.x+self.place.w/2, self.place.y, 
                    self.place.x+self.place.w/2, self.place.y+self.place.h )
        else:
            line(     self.place.x, self.place.y+self.place.h/2, 
                    self.place.x+self.place.w, self.place.y+self.place.h/2 )
        strokeWeight(2)
        self.handle.draw()
    
    def press(self):
        if (self.handle.contains(mouseX, mouseY, tol=14) or
            self.place.contains(mouseX, mouseY,) ):
            self.isDragging = True
            self.update()
    
    def drag(self):
        if self.isDragging:
            self.update()
    
    def release(self):
        self.isDragging = False
        
def setup():
    global sliders
    size(400,200)
    sliders = []
    for i in range(10):
        sliders.append( Slider( Rect(40*i,10,40,180), minVal=100, maxVal=255 ) )

def draw():
    background(200)
    for slidy in sliders:
        slidy.draw()

def mousePressed():
    for slidy in sliders:
        slidy.press()

def mouseDragged():
    for slidy in sliders:
        slidy.drag()

def mouseReleased():
    for slidy in sliders:
        slidy.release()
