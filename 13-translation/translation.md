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

Python             | Java                    | JavaScript
------------------ | ----------------------- | ----------------- 
	w = "howdy"    | 	String w = "howdy";  |    var w = "howdy",
	x = 3          |	int x = 3;           |		x = 3,
	y = 4.25       |	float y = 4.25;      |		y = 4.25,
	z = [1, 2, 3]  |	int[] z = {1, 2, 3}; |		z = {1, 2, 3};

java

	String w = "howdy";
	int x = 3;
	float y = 4.25;
	int[] z = {1, 2, 3};

javascript

	var w = "howdy",
		x = 3,
		y = 4.25,
		z = {1, 2, 3};


	- math operators
	- for loops
	- while loops
	- boolean operators
	- conditions 
	- working with arrays (lists)
	- encapsulation
	- importing
- Processing-isms (processing.js works by translating java processing code so I'll only show java and python here)
	- setup/draw framework
	- mouse functions
	- keyboard functions

## Fun places to work with other languages
- [Processing!](http://processing.org)  (Java)
- [Unity3D](http://unity3d.com) (JavaScript)

## Assignment
- convert one of your previous sketches from python to Java (1 point)
- convert one of the java Processsing examples to python (1 point)
- submit both files on Carmen
