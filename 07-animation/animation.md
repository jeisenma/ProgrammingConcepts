--------------------------------
# Animation: bringing things to life with motion
--------------------------------

## Discussion
- types of animation:
	- Prerecorded -- based on numbers or images
	- Procedural -- driven by math, physics, or rules
- animation principles
- special considerations for interaction
	- ease-in/ease-out
	- overlapping 
- Perlin noise vs. randomness

## Programming Concepts
- Functions and parameters
- Loops and lists (again!)

## Examples
 - [Animated Sprite][] ([data](pcad.py?page=07-animation/animatedSprite/data.zip))
 - [Recorded Motion][] ([variable length animations][])
 - [Making Waves][]
 - [The Many Adventures of Sine][]
 - [Bouncing ball][]
 - [Springs][]

## Lab
- [Noisy Worm][] - Create a worm out of a series of circles.  Move the head of the worm with a noise function.  Make the rest of the worm's body follow the head by remembering previous head positions.
- Just for fun: [a similar idea, but with a jiggly killer whale!](http://img0.liveinternet.ru/images/attach/c/5//3970/3970473_sprite198.swf)

## Reading
- [LPTHW: 34](http://learnpythonthehardway.org/book/ex34.html)
- [Animation Principles](https://www.cs.washington.edu/education/courses/459/12au/exercises/animation_principles.html)
- Optional further reading:
	- [John Lasseter's original paper applying 12 Disney principles to computer animation](http://dl.acm.org/citation.cfm?id=37407)
	- [The Uses and Abuses of Cartoon Style in Animation](http://journal.animationstudies.org/leslie-bishko-the-uses-and-abuses-of-cartoon-style-in-animation/)
	- [Computer Animation: Algorithms and Techniques](http://books.google.com/books?id=DudZtbOD2gMC&lpg=PP1&dq=0124158420&pg=PP1#v=onepage&q&f=false)

## Assignments
- Interactive Animation Sketch
	- make your monster respond to mouse/keyboard input with appealing animation (1 point)
	- you can use prerecorded keyframes or procedural rules... or both! (1 point)
	- use at least one custom function with at least one parameter to update the monster's pose  (2 points)
- Save it to a file called animation.py and submit it on Carmen. (4 points total)

[Animated Sprite]: pcad.py?page=07-animation/animatedSprite/animatedSprite.py
[Recorded Motion]: pcad.py?page=07-animation/recordedMotion.py
[variable length animations]: pcad.py?page=07-animation/recordedMotionVariableLength.py
[Making Waves]: pcad.py?page=07-animation/waves.py
[The Many Adventures of Sine]: pcad.py?page=07-animation/theManyAdventuresOfSine.py
[Bouncing ball]: pcad.py?page=07-animation/bouncy.py
[Springs]: pcad.py?page=07-animation/springy.py
[Noisy Worm]: pcad.py?page=07-animation/worm.py