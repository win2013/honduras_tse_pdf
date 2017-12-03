
import os
import imghdr
from os.path import basename
import sys
import json
import urllib2
from PIL import Image

sources=["presidente/" , "alcalde/", "diputados/"];

def info(mer_id):
  #print "Prosssing ... "+str(mer_id)
  try:
      data = json.load(urllib2.urlopen("https://api.tse.hn/prod/ApiActa/Consultar/1/"+mer_id))
  except ValueError, e:
      print ("%s HTTP Error " %str(mer_id))
      return "[ ]"
  return data;

sn_votes=0
joh_votes=0

dw = 0
dh = 0
aw = 0
ah = 0
pw = 0 
ph = 0

mer_init = int (sys.argv[1]);
mer_end  = int (sys.argv[2]);

for m in os.listdir(sources[0]):
    # print "Checking... "+m

    if m.endswith("jpg") or m.endswith("JPG"):
	 if (os.path.exists(sources[0]+"/"+m) and imghdr.what(sources[0]+"/"+m)=="jpeg"):
		cover = Image.open(sources[0]+"/"+m)
		pw, ph =  cover.size
	 if (os.path.exists(sources[1]+"/"+m) and imghdr.what(sources[1]+"/"+m)=="jpeg"):
                cover = Image.open(sources[1]+"/"+m)
                aw, ah =   cover.size
	 if (os.path.exists(sources[2]+"/"+m) and imghdr.what(sources[2]+"/"+m)=="jpeg"):
                cover = Image.open(sources[2]+"/"+m)
                dw, dh =   cover.size	 

	 mer_id=os.path.splitext(basename(m))[0]

         if (int(mer_id)>=mer_init and int(mer_id)<=mer_end):
	    mer_data = info(mer_id) 
            if (len(mer_data["Votos"])>0):
	    	print ("%s, %d, %d, %d, %d, %d, %d, %s, %d, %s, %d, %d, %d, %d" % ( 
			mer_id, 
			pw, 
			ph,
			aw, 
			ah,
			dw,
			dh, 
			mer_data["Votos"][1]["NomPartido"].encode('utf-8').strip(),
            		mer_data["Votos"][1]["NumVotos"],
            		mer_data["Votos"][8]["NomPartido"].encode('utf-8').strip(),
            	        mer_data["Votos"][8]["NumVotos"],
			mer_data["NumVotosValidos"], 
			mer_data["NumPapeletasRecibidas"],
			mer_data["NumVotosTotal"]));
		sn_votes += mer_data["Votos"][1]["NumVotos"]
		joh_votes += mer_data["Votos"][8]["NumVotos"]
	    else:
		print ("%s, %s No DATA " % (str(mer_id), mer_data["NomEstado"]));

print "Total SN/ALianza: "
print sn_votes;

print "Totl JOH/PNH:  "
print joh_votes;

