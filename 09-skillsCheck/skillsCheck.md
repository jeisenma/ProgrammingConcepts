--------------------------------
# Skills Check: review of the programming basics

--------------------------------

Make a directory called skillsCheck in your sketchbook directory. Inside this directory make a new sketch for each problem below. 

Compress the skillsCheck directory and email it to me.

## ForLoop1

Write a for loop that prints numbers from 0 up to (and including) 10.

## ForLoop2
- Copy the previous sketch and change it so that the counting starts at 10 and goes down to 0.

## Lists1
- In the setup() function, create a list of 20 random integers between 0 and 255.  Use that list inside the draw() function to color 20 squares arranged in a row across the middle of the screen.

## Lists2
- Create a list that will hold positions of circles placed on the screen with mouse clicks. The screen should start empty, allowing the user to place a circle by clicking with the mouse. The center of each circle should be at the click location and stored as a PVector in the list. You must place a call to background(255) in the draw() function.

## Animation
- Start by copying the previous sketch. Use the sin() function to animate the size of each circle. The diameter should range between 20 and 40. (hint: use the map function to change the values that come out of the sine function) Use frameCount*0.01 as the argument to the sin() function. All the circles should be pulsing in unison.

## Encapsulation
- Create a class for your pulsing circles. It should have the following properties:

	1. position where its located on the screen
	2. diameter the current size of the circle
	3. color the color of the circles fill
	4. pulseFreq the frequency of the pulsing motion
- The class should have three functions:

	1) \_\_init\_\_ the constructor which takes a parameter for position and generates a random color and a random pulseFreq between 0.01 and 0.06.
	2) update this function updates the diameter using the sin() function like this:
		- sin(frameCount*pulseFreq)
		You will need to use the map() function like before to map the values.
	3) display draw the circle on the screen using the properties
	
- You will need to create a separate main file for this sketch that will import the file that
contains the Circle class. In the main file, call the Circle() constructor when the mouse is
pressed. All circles should be stored in a list.
