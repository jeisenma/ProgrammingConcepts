# J Eisenmann 2013 
# jeisenma@accad.osu.edu

def setup():
    global checks
    size(130,310)
    checks = []
    for i in range(10):
        checks.append( CheckBox( Rect(20,10+30*i,20,20,2), "Checkbox %d"%i, i%2 ) )

def draw():
    background(200)
    for check in checks:
        check.draw()

def mousePressed():
    for check in checks:
        check.release()

def keyPressed():
    print(findCheckedBoxes())
    
def findCheckedBoxes():
    results = []
    for i,check in enumerate(checks):
        if check.toggle:
            results.append(i)
            return results
        
class CheckBox:
    """ A checkbox class """
    def __init__(self, place, label, toggle=False ):
        self.place = place
        self.label = label
        self.toggle = toggle
            
    def draw(self):
        strokeWeight(2)
        fill(255)
        self.place.draw()
        if self.toggle:
            line(self.place.x+2, self.place.y+2, self.place.x+self.place.w-2, self.place.y+self.place.h-2)
            line(self.place.x+2, self.place.y+self.place.h-2, self.place.x+self.place.w-2, self.place.y+2)
        fill(0)
        textAlign( LEFT, CENTER )
        textSize( self.place.h/2 )
        text( self.label, self.place.x+3*self.place.w/2, self.place.y+self.place.h*0.45 )
    
    def release(self):
        if self.place.contains(mouseX, mouseY,):
            self.toggle = not self.toggle
            
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
        
