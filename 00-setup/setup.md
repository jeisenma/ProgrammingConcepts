--------------------------------
# Setup
--------------------------------

Here are the links and instructions you will need to work with the same development tools on your own computer.  Everything below is already set up for you at ACCAD.  

## [Scratch][]

- This one runs in a browser.  No need to install.  

## [Python](http://www.python.org/)

- Currently, I recommend downloading the latest 2.7 version.  There are some major changes in 3.0+ that aren't compatible yet with most modules and APIs.

## [Processing-py][processing-py]

- Download [processing-py][]. Unzip it to location on your hard drive. (Remember where!)
- Download & Install [jEdit][].
- Run jEdit and go to Plugins > Plugin Manager.  In the "Install" tab, select and install the following plugins:
	- Console
	- BufferTabs
	- ErrorList
- Save [this keyboard shortcuts file][] to your <USER>/AppData/Roaming/jEdit/keymaps folder (/User/<USER>/.jedit/keymaps on Mac) by right-clicking and choosing save as.
- Save [this XML file][] ([Mac version here][]) to your <USER>/AppData/Roaming/jEdit/console/commando folder (/User/<USER>/.jedit/console/commando on Mac) by right-clicking and choosing save as. 
- (You may need to change the default values for "path to java" and "path to processing-py.jar" to reflect the locations of java and processing-py on your computer.)
- Restart jEdit!
- Go to Utilities > Global Options > Editing and set Tab Width and Indent Width equal to 4
- Go to Utilities > Global Options > Shortcuts and select "p5py" from the "Choose keymap" drop down menu.  Hit "Apply" at the bottom of the window.
- Go to Plugins > Plugin Options, then select Console > Error Patterns.  Hit the "+" button and type "python", hit "Apply".
- Hit the "+" button again and type "processing-py", then edit the "Error Regexp" and "Filename", "Line number", "Error Message" boxes to look [like this](https://raw.github.com/jeisenma/ProgrammingConcepts/master/00-setup/jeditFiles/jEditErrorPatterns.png)
- To test that everything is working
	1. copy this code: "ellipse(50,50,50,50)" without the quotes to a new file
	2. save it as "test.py" 
	3. hit Ctrl+r and hit "OK"
	4. you should see a white circle on a grey background
	5. try deleting the last parenthesis and running again (Ctrl+r and hit "OK") -- you should get an error message in your Error List window
	6. put that parenthesis back and try adding this text on the next line: "print puppies" -- you should get an error message again that points you to the line with the error

<!--

- In jEdit, go to Plugins > Plugin Options.  Create a new error pattern by hitting the plus-sign button and edit to look like [this screenshot](https://www.dropbox.com/s/o37bi4v9wsec40s/jEditErrorPatterns.png?dl=1)
- Download [processing-py][]
- Unzip it to your Desktop
- Find the p5py.exe file inside the folder, right-click on it and choose "Pin to Taskbar"
-->

<!--
- In [Notepad++][] go to Run > Run...
- Copy and paste this command: 
	- java -jar Z:\processing.py-0021\processing-py.jar "$(FULL_CURRENT_PATH)"
- Then hit the "Save" button and name it: "processing-py"
- Assign the keystroke ctrl+R and hit "OK"
-->

## [Processing](http://processing.org/download/)

- Download and unzip it


[Scratch]: http://scratch.mit.edu/projects/editor/?tip_bar=getStarted
[processing-py]: https://github.com/jeisenma/ProgrammingConcepts/blob/master/00-setup/processing.py-0022.zip
[this XML file]: pcad.py?page=00-setup/jeditFiles/PYP5.xml
[Mac version here] pcad.py?page=00-setup/jeditFiles/PYP5_mac.xml
[this keyboard shortcuts file]: pcad.py?page=00-setup/jeditFiles/p5py_keys.props
[jEdit]: http://sourceforge.net/projects/jedit/files/jedit/5.0.0/jedit5.0.0install.jar/download
[Notepad++]: http://notepad-plus-plus.org/download/v6.3.3.html
