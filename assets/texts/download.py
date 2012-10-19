#!/usr/bin/env python
"""
Download files from a file
"""
import time
import os

f = open('files.txt', 'r')
files = f.read().split("\n")

for f in files:
	f.strip()
	if f == "":
		continue
	else:
		print "getting", f
		os.system("cd downloads && wget " + f)
		time.sleep(1)
