from fpdf import FPDF
from PIL import Image
import os # I added this and the code at the end
import imghdr
import sys
from os.path import basename

import csv
from pprint import pprint
import json
import urllib2

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("-s", "--start", help="Comenar en Acta ",
#                    action="store_true")

start_id = 0;
end_id   = 18180;
database_name = "pdfs/data.csv"
flag_NO_METADATA = False

arg_len=len(sys.argv)
if (arg_len  >    1):
    start_id = int(sys.argv[1])
    if (start_id<0):
        start_id = 0;
    print "START of Index" + str( start_id );
    end_id = int(sys.argv[2]);
    if (end_id<0):
        end_id = 0
    print "END of Index "+ str( end_id ) ;
    if arg_len > 3:
        database_name = sys.argv[3]
        print "Chooisng output for database name "+database_name

ofile = open(database_name, "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

row=[];

def metadata(mer_id):
    print "Retrieving ...  "+mer_id
    try:
        data = json.load(urllib2.urlopen("https://api.tse.hn/prod/ApiActa/Consultar/1/"+mer_id))
    except ValueError, e:
        return "[ ]"
    return data;

def getTimeStamp(mer_id_file):
    print "######## Timestamp for "+mer_id_file;
    data = ""
    if (os.path.exists(mer_id_file)):
        fdata= open(mer_id_file)
        data = fdata.readlines();
        print data
        print "TIMESTAMP: "
        print " ".join(data[4].split(":")[1:]);
        # dateinfo = data[4].split(":")
        fdata.close();
        return data[4].split(":")[1:];
    return data;

def makePdf(pdfFileName, images, timestamps, mer_metadata):
    cover = Image.open(images[0])
    width, height = cover.size
    data = [mer_metadata["NomCentroVotacion"].encode('utf-8').strip(),
            mer_metadata["NomMunicipio"].encode('utf-8').strip(),
            mer_metadata["NomDepartamento"].encode('utf-8').strip()]
    row= sum([images, timestamps,data], [])
    writer.writerow(row);
    print "IMAGES >>>>>>>>>>>>>>>>>>>>>>>>>>"
    print images
    print "MER_ METADATA >>>>>>>>>>>>>>>>>>>"
    print mer_metadata
    print "TIMESTAMPS >>>>>>>>>>>>>>>>>>>>>>>"
    print timestamps

    pdf = FPDF(unit="pt", format=[width, height+70])
    c=0;
    for page in images:
        pdf.add_page()

        if (os.path.exists(str(page)) and imghdr.what(str(page))):
            pdf.image(str(page), 0, 0)
        else:
            pdf.set_font("Arial", size=64)
            pdf.cell(1000,100, "NOT FOUND......  ")
        pdf.set_font("Arial", size=32)
        if (c==0):
           pdf.set_xy(500,1500)
        if (c==1):
            pdf.set_xy(400,1200)
        if (c==2):
            pdf.set_xy(500,1500)
        pdf.cell(100, 15,   "GMT Time: "+str(timestamps[c]))
        pdf.ln(0.15)
        pdf.set_xy(400,10)
        pdf.cell(100, 15, mer_metadata["NomCentroVotacion"])
        pdf.set_xy(1000,10)
        pdf.ln(0.15)
        pdf.set_xy(1400, 10)
        pdf.cell(100, 15, mer_metadata["NomMunicipio"])
        pdf.ln(0.15)
        pdf.set_xy(2000,10)
        pdf.set_text_color(255,17,0);
        pdf.cell(100, 15, txt=mer_metadata["NomDepartamento"])
        pdf.ln(0.15)
        if (len(mer_metadata["Votos"])<=0):
           pdf.set_xy(2000,1500)
           pdf.set_text_color(255,17,0);
           pdf.cell(100,15, "VOTER Information MISSING")
        else:
          pdf.set_xy(2000,1500)
          pdf.set_text_color(0,43,0)
          pdf.cell(100,15, mer_metadata["Votos"][1]["NomPartido"].encode('utf-8').strip())
          pdf.set_xy(2500,1500)
          pdf.cell(100,15, str(mer_metadata["Votos"][1]["NumVotos"]))
          pdf.set_xy(2000,1550)
          pdf.cell(100,15, mer_metadata["Votos"][8]["NomPartido"].encode('utf-8').strip())
          pdf.set_xy(2000,1600)
          pdf.cell(100,15, str(mer_metadata["Votos"][8]["NumVotos"]))
        c=c+1;

    pdf.output(pdfFileName + ".pdf", "F")

print "---------------------------------"
print "PDF Generator for ELECTIONS 2017"
print "--------------------------------"
sources = ["presidente/", "diputados/", "alcalde/"];
# this is what I addedsources = ["presidente/", "diputados/", "alccalde/"];
mer_ids_jpgs = []
mer_ids = []
for m in os.listdir(sources[0]):
    if m.endswith("jpg") or m.endswith("JPG") and imghdr.what(sources[0]+"/"+m)=="jpeg":
         mer_ids_jpgs.append(sources[0]+"/"+m);

#print mer_ids_jpgs;


#print mer_ids;

for mer_id_jpg in mer_ids_jpgs[int(start_id):]:
  image_files = []
  timestamps  = []
  mer_id = os.path.splitext(basename(mer_id_jpg))
  print "MER_ID  :"+ mer_id[0]
  for data in sources:
       image_files.append(data +"/"+mer_id[0]+".JPG");
       timestamps.append(getTimeStamp(data+"/"+mer_id[0]+".timestamp.txt"))

  mer_metadata = []
  print "Retrieving METADATA for MER : "+mer_id[0]
  if (flag_NO_METADATA):
       print "NO METADATA FLAG TURNED ON"
  else:
       mer_data = metadata(mer_id[0])
  print "Creating ... "
  pprint(mer_data);
  #print image_files;
  print timestamps;
  if (not os.path.exists("pdfs/"+mer_id[0]+".pdf")):
      print "*************** Making a new pdf "
      makePdf("pdfs/"+mer_id[0], image_files, timestamps, mer_data)
  else:
      if (len(mer_data["Votos"])>0):
         data = [mer_data["NomCentroVotacion"].encode('utf-8').strip(),
              mer_data["NomMunicipio"].encode('utf-8').strip(),
              mer_data["NomDepartamento"].encode('utf-8').strip(),
              mer_data["Votos"][1]["NomPartido"].encode('utf-8').strip(),
              mer_data["Votos"][1]["NumVotos"],
              mer_data["Votos"][8]["NomPartido"].encode('utf-8').strip(),
              mer_data["Votos"][8]["NumVotos"]]
      else:
          data = [mer_data["NomCentroVotacion"].encode('utf-8').strip(),
                  mer_data["NomMunicipio"].encode('utf-8').strip(),
                  mer_data["NomDepartamento"].encode('utf-8').strip(),
                  "NOT FOUND",
                  0,
                  "NOT FOUND",
                  0]

      row= sum([image_files, timestamps,data], [])
      writer.writerow(row);
      print "******   pdfs/"+mer_id[0]+"   already created "

ofile.close()
print "Done... "
