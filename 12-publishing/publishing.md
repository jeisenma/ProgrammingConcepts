--------------------------------
# Publishing your work
--------------------------------

## Screen captured video ##
- Processing's Movie Maker tool
- Quicktime can also convert an image sequence to a movie

## Building an application for the desktop ##
- Add these two lines to the top of your main python file:
	- import launcher
	- launcher.create()
- This is still in development and may or may not work, depending on what's in your sketch

## Building for the web ##
- I've patched together a couple of web frameworks people have made
	- One is called "skulpt" and it lets you run python code in a browser as JavaScript
	- The other is called Processing.js which is a JavaScript implementation of Processing
- The prototype of this is [located here](http://accad.osu.edu/~jeisenma/teaching/playground/)
- Currently not all Processing functions and classes have been included.  I'm working on that...
- Another limitation is that the libraries will not work because they are based on Java (which is neither python nor JavaScript and will not run natively in the browser)

## Releasing your code into the wild ##
- There are a growing number of ways to share your code with the world
	- [GitHub](https://github.com/)
	- [OpenProcessing](http://www.openprocessing.org/) (Java code only)
	
