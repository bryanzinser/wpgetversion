#!/usr/bin/env python
# encoding: utf-8
"""
wpgetversion.py

Created by Bryan Zinser on 2012-01-31.

Version 0.1
"""

to_mail = 'bryan.a.zinser@gmail.com'
from_mail = 'wpgetversion@routescribe.com'

import sys
import urllib
import smtplib
from email.mime.text import MIMEText

script, yourversion = sys.argv

def sendemail(a, b):
	fp = "You need to update. You're running version \"%s\" and the latest version is \"%s\"" % (a, b)
	msg = MIMEText(fp)
	msg['Subject'] = 'Hey update your WordPress install!'
	msg['From'] = from_mail
	msg['To'] = to_mail
	s = smtplib.SMTP('localhost')
	s.sendmail(from_mail, [to_mail], msg.as_string())
	s.quit()

def getyourversion(b):

	p = urllib.urlopen(b)
	#p = str(p)

	for line in p:
		if "generator" in line:
			awesome = line.split(' ')
			awesome = awesome[-2]
			awesome = awesome[:-1]
			return awesome
		#else:
			#return False

def getlatestversion():
	
	p = urllib.urlopen("http://wordpress.org")

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
		sendemail(mine, theirs)
	