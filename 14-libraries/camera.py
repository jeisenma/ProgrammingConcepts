# adapted from the Processing capture example: http://processing.org/reference/libraries/video/Capture.html

from processing.video import Capture

def setup():
	global cam
	size(640, 480)
	cameras = Capture.list()
	
	if len(cameras) == 0:
		print("There are no cameras available for capture.")
		exit()
	else:
		print("Available cameras:")
		for i,camera in enumerate(cameras):
			print(i,camera)
	
	# The camera can be initialized directly using an 
	# element from the array returned by list():
	cam = Capture(this, cameras[1])
	cam.start()

def draw():
  if cam.available():
    cam.read()
  image(cam, 0, 0)
