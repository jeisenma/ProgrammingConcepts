--------------------------------
# Translation: becoming a polyglot
--------------------------------

## Making the transfer
- the concepts are almost entirely the same
- the syntax will be different (e.g. "int x = 3;" instead of "x=3")
- you may have to type more stuff
	- ![java vs python](pcad.py?page=13-translation/javaVsPython_moreTyping.png)

## Examples 
### Core Concepts (python / java / javascript)
#### variable declaration

<textarea rows="5" cols="42" style="float:left;">
w = "howdy"
x = 3
y = 4.25
z = [1, 2, 3]
</textarea>
<textarea rows="5" cols="42" style="float:left;">
String w = "howdy";
int x = 3;
float y = 4.25;
int[] z = {1, 2, 3}; 
</textarea>
<textarea rows="5" cols="42" style="float:left; clear:none;">
var	w = "howdy",
	x = 3,
	y = 4.25,
	z = {1, 2, 3};
</textarea>	 

<br>
#### math operators

<textarea rows="5" cols="42" style="float:left;">
x = 3\*\*2
y = abs(2.3-4.25)
z = (x+y)\*2/3
</textarea>
<textarea rows="5" cols="42" style="float:left;">
float x,y,z;
x = pow(3,2);
y = abs(4.25-2.3);
z = (x+y)\*2/3;
</textarea>
<textarea rows="5" cols="42" style="float:left;">
var x,y,z;
x = Math.pow(3,2);
y = Math.abs(4.25-2.3);
z = (x+y)\*2/3;
</textarea>		<br><br><br>

#### for loops

<textarea rows="5" cols="42" style="float:left;">
for i in range(10):
	print "looping... ", i
</textarea>
<textarea rows="5" cols="42" style="float:left;">
for(int i=0; i<10; i++){
	println("looping... "+i);
}
</textarea>
<textarea rows="5" cols="42" style="float:left;">
for(var i=0; i<10; i++){
	console.log("looping... "+i);
}
</textarea>		<br><br><br>

#### while loops

<textarea rows="7" cols="42" style="float:left;">
i=10
while i > 0:
	print "looping... ", i
	i -= 1
</textarea>
<textarea rows="7" cols="42" style="float:left;">
int i=10;
while( i > 0) {
	println("looping... "+i);
	i--;
}
</textarea>
<textarea rows="7" cols="42" style="float:left;">
var i=10;
while( i > 0 ) {
	console.log("looping... "+i);
	i--;
}
</textarea>		<br><br><br>

#### boolean operators and conditions

<textarea rows="10" cols="42" style="float:left;">
if x < 5 and (y == 3 or z >= 0.5):
	print "yes"
elif not( i%2 == 0 ):
	print "maybe"
else:
	print "no way"
</textarea>
<textarea rows="10" cols="42" style="float:left;">
if( x < 5 && (y == 3 || z >= 0.5) ) {
	println("yes");
}
else if (i%2 != 0) {
	println("maybe");
}
else {
	println("no way");
}
</textarea>
<textarea rows="10" cols="42" style="float:left;">
if( x < 5 && (y == 3 || z >= 0.5) ) {
	console.log("yes");
}
else if (i%2 != 0) {
	console.log("maybe");
}
else {
	console.log("no way");
}
</textarea>		<br><br><br>

#### working with arrays (lists)

<textarea rows="9" cols="42" style="float:left;">
numbers = range(10)
letters = ['a', 'b', 'c']
for num in numbers[2:]:
	print num
for letter in letters:
	print letter
for i,letter in enumerate(letters):
	print "letter #", i, " is ", letter
</textarea>
<textarea rows="9" cols="42" style="float:left;">
for(int i=2; i<10; i++) {
	println(i);
}
String[] letters = {'a', 'b', 'c'};
for( String letter : letters ) {
	println(letter);
}
for( int i=0; i<letters.length; i++ ) {
	println("letter #"+i+" is "+letters[i]);
}
</textarea>
<textarea rows="9" cols="42" style="float:left;">
for(var i=2; i<10; i++) {
	console.log(i);
}
var letters = ['a', 'b', 'c'];
for( var letter in letters ) {
	console.log(letter);
}
for( var i=0; i<letters.length; i++ ) {
	console.log("letter #"+i+" is "+letters[i]);
}
</textarea>		<br><br><br>

#### functions

<textarea rows="5" cols="42" style="float:left;">
def doStuff(a,b):
	x = a\*b
	return x
print doStuff(3,4)
</textarea>
<textarea rows="5" cols="42" style="float:left;">
float doStuff(float a, float b) {
	float x = a\*b;
	return x;
}
println(doStuff(3,4));
</textarea>
<textarea rows="5" cols="42" style="float:left;">
function doStuff( a, b ) {
	var x = a\*b;
	return x;
}
console.log(doStuff(3,4));
</textarea>		<br><br><br>

#### encapsulation

<textarea rows="12" cols="42" >
class Thing:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def stringify(self):
		return "%s, %s"%(self.x,self.y)
	def add(self,z):
		return self.x+self.y+z
myThing = Thing(3.1,4)
print myThing.stringify()
print myThing.add(5.1)
</textarea>
<textarea rows="12" cols="42" style="float:left;">
class Thing {
	float x, y;
	Thing(ix,iy) {
		x = ix;
		y = iy;
	}
	String stringify() {
		return self.x+" "+self.y;
	}
	float add(self,z) {
		return self.x+self.y+z;
	}
}
Thing myThing = new Thing(3.1,4);
println(myThing.stringify());
println(myThing.add(5.1));
</textarea>
<textarea rows="12" cols="42" style="float:left;">
function Thing(x,y) {
	this.x = x;
	this.y = y;
	this.stringify = function() {
		return self.x+" "+self.y;
	};
	this.add = function(z) {
		return this.x+this.y+z;
	};
}
var myThing = new Thing(3.1,4);
console.log(myThing.stringify());
console.log(myThing.add(5.1));
</textarea>		<br><br><br>

#### importing

<textarea rows="4" cols="42" style="float:left;">
from random import \*
</textarea>
<textarea rows="4" cols="42" style="float:left;">
import processing.pdf.\*;
</textarea>
<textarea rows="4" cols="42" style="float:left;">
put this in the HTML head:
<script type="text/javascript" src="somefile.js"></script>
</textarea>		<br><br><br>


### Processing-isms
#### setup/draw framework

<textarea rows="8" cols="42" style="float:left;">
def setup():
	size(400,400)

def draw():
	background(200)
	ellipse(width/2, height/2, 100, 100)
</textarea>
<textarea rows="8" cols="42" style="float:left;">
void setup() {
	size(400,400);
}

void draw() {
	background(200);
	ellipse(width/2, height/2, 100, 100);
}
</textarea>		<br><br><br>

#### mouse functions

<textarea rows="9" cols="42" style="float:left;">
def mousePressed():
	print "mouse pressed at: ", mouseX, mouseY
	
def mouseDragged():
	print "mouse dragged from: ", pmouseX, pmouseY, " to: ", mouseX, mouseY
	
def mouseReleased():
	print "mouse released at: ", mouseX, mouseY
</textarea>
<textarea rows="9" cols="42" style="float:left;">
void mousePressed() {
	println("mouse pressed at: "+mouseX+" "+mouseY);
}
void mouseDragged() {
	println("mouse dragged from: "+pmouseX+" "+pmouseY+" to: "+mouseX+" "+mouseY);
}	
void mouseReleased() {
	println("mouse released at: "+mouseX+" "+mouseY);
}
</textarea>		<br><br><br>


## Fun places to work with other languages
- [Processing!](http://processing.org)  (Java)
- [Unity3D](http://unity3d.com) (JavaScript)
- [JSFiddle](http://jsfiddle.net/) (JavaScript+CSS+HTML)

## Assignment
- convert one of your previous sketches from python to Java so it runs in java Processing (1 point)
- convert one of the more interesting [java Processsing examples](http://www.processing.org/examples/) to python (at least 10 lines of code) (1 point)
- put your .pde file and your .py file into a single zip and submit that on Carmen
