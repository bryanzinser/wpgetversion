#!/usr/bin/env python
# encoding: utf-8
"""
wpgetversion.py

Created by Bryan Zinser on 2012-01-31.
"""

import sys
import os
import urllib

def getyourversion():

	p = urllib.urlopen("http://pktmaniac.info")
	#p = str(p)

	for line in p:
		if "generator" in line:
			awesome = line.split(' ')
			awesome = awesome[-2]
			awesome = awesome[:-1]
			return awesome

def getlatestversion():
	
	p = urllib.urlopen("http://wordpress.org")

	for line in p:
		if "Download&nbsp;WordPress&nbsp;" in line:
			awesome = line.split(';')
			awesome = awesome[-1]
			awesome = awesome[:-10]
			return awesome
			
mine = getyourversion()
theirs = getlatestversion()

if mine == theirs:
	print "Latest version"
else:
	print "you need to update %s %s" % (mine, theirs)
	