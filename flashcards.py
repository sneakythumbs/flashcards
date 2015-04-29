import sys
import fileinput
from pylab import *

header = True
column = -1


prompt = raw_input("Enter the filename(s) to be read:\n")
files = prompt.split(", ")
for line in fileinput.input(files):
	s = line.split("\t|\t")
	
	if header:
		print"Select language to sort by:",
		for word in s[:-1]:
			print "[" + word + ",",
		print s[-1].strip("\r\n") + "]"
		language = raw_input("")
		
		i = 0
		for word in s:
			if language == word.strip("\r\n"):
				column = i
				break;
			i += 1
		if column == -1:
			print "Error: no such language"
			print "Exiting"
			sys.exit()
			
		header = False
		continue;
		
	if not header:
#		print line[:-1]
		continue;

