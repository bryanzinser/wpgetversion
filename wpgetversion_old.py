#!/usr/bin/env python
# encoding: utf-8
"""
wpgetversion.py

Created by Bryan Zinser on 2012-01-31.

Version 0.1
"""

import sys
import urllib

script, yourversion = sys.argv

def getyourversion(b):
	p = urllib.urlopen(b)
	#find and format your WordPress version
	for line in p:
		if "generator" in line:
			awesome = line.split('"')
			for what in awesome:
				if "WordPress" in what:
					awesome = what[10:]
	return awesome

def getlatestversion():	
	p = urllib.urlopen("http://wordpress.org")
	#find and format latest Wordpress version
	for line in p:
		if "Download&nbsp;WordPress&nbsp;" in line:
			awesome = line.split(';')
			awesome = awesome[-1]
			awesome = awesome[:-10]
	return awesome

if yourversion[:7] != "http://":
	if yourversion[:8] == "https://":
		print "Please use http://, but since you're so nice I'll do it for you!"
		yourversion = "http://" + yourversion[8:]
	else:
		yourversion = "http://" + yourversion

mine = getyourversion(yourversion)
theirs = getlatestversion()

if mine == None:
	print "Can't find your version info."
else:
	if mine == theirs:
		print "You're running the latest version, Good Job!"
	else:
		print "You need to update. You're running version \"%s\" and the latest version is \"%s\"" % (mine, theirs)
	