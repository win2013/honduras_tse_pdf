
import os
import imghdr
from os.path import basename
import sys
import json
import urllib2
from PIL import Image
from  shutil import copy2

INPUT = "5174.csv"
DIR   = "5174"

import csv 
sn = {}
joh = {}
with open(INPUT, 'rb') as csvfile:
      votingdata = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in votingdata:
	print row; 
	mer_id = row[0]; votes = row[1];
	try:
	   if (int(mer_id)>=50 and int(votes)>=0 and (row)>0):
	       print "pdfs/"+mer_id.rjust(5,'0')+".pdf  to "+ DIR; 
	       if (os.path.exists("pdfs/"+mer_id.rjust(5,'0')+".pdf")): 
                  copy2("pdfs/"+mer_id.rjust(5,'0')+".pdf", DIR);
	       else:
		  print "Not found.....  pdfs/"+mer_id.rjust(5,'0')+".pdf "
	except ValueError:
    	     #Handle the exception
   	     print 'Error parsing ..... enter an integer in this row'   

