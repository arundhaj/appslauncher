# Whenever I start my machine, I wanted these applications and files to be loaded.
# This script works on Windows 7 machine

import os, sys
import webbrowser
import yaml

# get the path of the script and find the path of the config file.
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
configfile = os.path.join(dirname, "config.yaml")

stream = open(configfile, 'r')

conf = yaml.load(stream)

for key in conf:
	if key == "file":
		for file in conf[key]:
			try: 
				os.startfile(file)
			except:
				print 'Failed to open', file
				print sys.exc_info()[0]
	elif key == "app":
		for app in conf[key]:
			try:
				os.startfile(app)
			except:
				print 'Failed to open', app
				print sys.exc_info()[0]
	elif key == "uri":
		for uri in conf[key]:
			try:
				webbrowser.open(uri)
			except: 
				print 'Failed to open', uri
				print sys.exc_info()[0]
	else:
		print "nothing"