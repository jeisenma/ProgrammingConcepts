# J Eisenmann 2013 
# jeisenma@accad.osu.edu

# frequencyModulation
# Adapted from simple example for doing FM (frequency modulation) using two Oscils.
# Use the mouse to control the speed and range of the frequency modulation.
# Author: Damien Di Fede

# import everything necessary to make sound.
from ddf.minim import Minim
from ddf.minim.ugens import Waves, Oscil
	
# setup is run once at the beginning
def setup():
	global minim, out, fm
	# initialize the drawing window
	size( 512, 200 )
	
	# initialize the minim and out objects
	minim = Minim(this)
	out   = minim.getLineOut()
	
	# make the Oscil we will hear.
	# arguments are frequency, amplitude, and waveform
	wave = Oscil( 200, 0.8, Waves.TRIANGLE )
	# make the Oscil we will use to modulate the frequency of wave.
	# the frequency of this Oscil will determine how quickly the
	# frequency of wave changes and the amplitude determines how much.
	# since we are using the output of fm directly to set the frequency
	# of wave, you can think of the amplitude as being expressed in Hz.
	fm = Oscil( 10, 2, Waves.SINE )
	# set the offset of fm so that it generates values centered around 200 Hz
	fm.offset.setLastValue( 200 )
	# patch it to the frequency of wave so it controls it
	fm.patch( wave.frequency )
	# and patch wave to the output
	wave.patch( out )


# draw is run many times
def draw():
	# erase the window to black
	background( 0 )
	# draw using a white stroke
	stroke( 255 )
	# draw the waveforms
	for i in range( out.bufferSize()-1 ):
		# find the x position of each buffer value
		x1  =  map( i, 0, out.bufferSize(), 0, width )
		x2  =  map( i+1, 0, out.bufferSize(), 0, width )
		# draw a line from one buffer position to the next for both channels
		line( x1, 50 + out.left.get(i)*50, x2, 50 + out.left.get(i+1)*50)
		line( x1, 150 + out.right.get(i)*50, x2, 150 + out.right.get(i+1)*50)
	if( dist(pmouseX, pmouseY, mouseX, mouseY) > 0.1 ):
		mouseMoved()


# we can change the parameters of the frequency modulation Oscil
# in real-time using the mouse.
def mouseMoved():
	modulateAmount = map( mouseY, 0, height, 220, 1 )
	modulateFrequency = map( mouseX, 0, width, 0.1, 100 )
	fm.frequency.setLastValue( modulateFrequency )
	fm.amplitude.setLastValue( modulateAmount )
