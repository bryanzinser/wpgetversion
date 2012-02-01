#!/usr/bin/env python
# encoding: utf-8
"""
blah.py

Created by Bryan Zinser on 2012-02-01.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import argparse, urllib, smtplib
from email.mime.text import MIMEText

versions = {}
fuck = []
needsupdated = False
x = ""

def sendemail(x):
	#fp = "You need to update. You're running version \"%s\" and the latest version is \"%s\"" % (a, b)
	msg = MIMEText(x)
	msg['Subject'] = 'Hey update your WordPress install!'
	msg['From'] = args.email[0]
	msg['To'] = args.email[1]
	s = smtplib.SMTP('localhost')
	s.sendmail(args.email[0], [args.email[1]], msg.as_string())
	s.quit()

def getversion(b):
	p = urllib.urlopen(b)
	#find and format your WordPress version
	for line in p:
		if "generator" in line:
			awesome = line.split('"')
			for what in awesome:
				if "WordPress" in what:
					awesome = what[10:]
	return awesome

def getwpversion():	
	p = urllib.urlopen("http://wordpress.org")
	#find and format latest Wordpress version
	for line in p:
		if "Download&nbsp;WordPress&nbsp;" in line:
			awesome = line.split(';')
			awesome = awesome[-1]
			awesome = awesome[:-10]
	return awesome

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Check to see if you\'ve got the latest version of WordPress')
	parser.add_argument('-e', dest="email", metavar='Email', action="store", nargs='+', help="FROM@example.com TO@example.com")
	parser.add_argument('-w', dest="websites", metavar='Website', action="store", nargs='+', help='websites to check')
	args = parser.parse_args()
	if args.email == None:
		for website in args.websites:
			versions[website] = getversion(website)
		for site in versions:
			if versions[site] == getwpversion():
				print "%s is uptodate!" % site
			else:
				print "%s is out of date %s!=%s" % (site, versions[site], getwpversion())
	else:
		for website in args.websites:
			versions[website] = getversion(website)
		for site in versions:
			if versions[site] == getwpversion():
				x = x + "%s is uptodate!" % site
				print "%s is uptodate!" % site
			else:
				x = x + "%s is out of date %s!=%s\n" % (site, versions[site], getwpversion())
				"%s is out of date %s!=%s\n" % (site, versions[site], getwpversion())
				needsupdated = True
		if needsupdated == True:
			sendemail(x)
