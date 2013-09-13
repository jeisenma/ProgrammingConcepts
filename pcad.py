## This is the mod_python script responsible for serving up the web pages.
## It grabs markdown files from the github repo and translates them to HTML.

## You will need to change the githubRoot and the webRoot

from mod_python import apache, util
from mod_python.Session import Session
import markdown
import urllib2
import sys

githubRoot = "https://raw.github.com/jeisenma/ProgrammingConcepts/master/"
webRoot = "http://accad.osu.edu/~jeisenma/"

def index(req,page="README"):
	# make sure the html fetch operation doesn't timeout too early
	sess = Session(req)
	sess.set_timeout(20)
	sess.save()

        # use the README page as the course index
	if page == "index":
		page = "README"
		
	# fetch the markdown text from dropbox
	link = "%s%s"%(githubRoot,page)
	#req.write(link)
	try:
		if page.endswith('.md') or page == 'README':
			# this is an HTML page
			req.content_type = "text/html"
			# give the page a title
			req.write("<title>ACCAD 5102</title>")
			# grab the stylesheet
			req.write("<style>%s</style>"%urllib2.urlopen("%sscreen.css"%webRoot).read())
			response = urllib2.urlopen(link)
                        #req.write(response.read())
			req.write(markdown.markdown(response.read(), ['tables']))
		else:
			util.redirect(req, link)
	except:
##		raise
##		req.write("error")
##		e = sys.exc_info()[0]
##		req.write(e)
		req.write("<br>This page does not exist yet")

