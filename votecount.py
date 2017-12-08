
import os
import imghdr
from os.path import basename
import sys
import json
import urllib2
from PIL import Image

input = sys.argv[2]
database = sys.argv[1]

import csv 
sn = {}
joh = {}
with open(database, 'rb') as csvfile:
      votingdata = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in votingdata:
	print row; 
	mer_id           = row [0];
	if (len(row) > 3):
		snvotes          = row [8]
		johvotes         = row[10]; 
		sn[int(mer_id)]  = snvotes;
		joh[int(mer_id)] = johvotes;  
	else:
		sn[int(mer_id)]  = 0;
		joh[int(mer_id)] = 0;

total_joh = 0 ;
total_sn =  0 ;
for m in os.listdir(input):
    # print "Checking... "+m
	 mer_id=os.path.splitext(basename(m))[0]
         if (m.endswith("pdf")):		
	    total_sn +=   int(sn[int(mer_id)])
	    total_joh  += int(joh[int(mer_id)])

print "Total SN/ALianza: "
print total_sn;

print "Totl JOH/PNH:  "
print total_joh;

