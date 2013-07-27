--------------------------------
# Libraries: letting other people do the hard work
--------------------------------

## Discussion
- review of importing modules in python
- the Java-processing equivalent
- \* doesn't work yet, you have to import things by name (see examples)

## Programming Concepts
- libraries
- data streams
 
## Installing libraries to processing.py
- Download and unzip the processing library you want (or use the [Processing Library Manager][] to get it into your sketchbook)
- Then copy the library folder into this folder:
	- PROCESSING.PY_INSTALLATION_FOLDER/libraries/processing/
- You can be certain you've copied the right folder from the library by making sure it's got a 'library' folder inside of it (one level down).  This 'library' folder should have one or more .jar files in it.

[Processing Library Manager]: http://wiki.processing.org/w/How_to_Install_a_Contributed_Library

## Examples
- [synthesizing sound with Minim][]	
- [scrubbing through a movie][] ([data](pcad.py?page=14-libraries/data/transit.mov))
- [getting a camera feed][]
- [blob tracking][] ([faster Java version][])

[synthesizing sound with Minim]: pcad.py?page=14-libraries/minim.py
[scrubbing through a movie]: pcad.py?page=14-libraries/movie.py
[getting a camera feed]: pcad.py?page=14-libraries/camera.py
[blob tracking]: pcad.py?page=14-libraries/blobs.py
[faster Java version]: pcad.py?page=14-libraries/blobs.pde
