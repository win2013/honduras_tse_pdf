import uuid
import Image
import math
import os
from fpdf import FPDF

width = 800;
height = 600;
pdf = FPDF(unit="pt", format=[width, height+70])

DIRMER       ="/mnt/glusterfs/afp_news/lredondo/MER/1/" 
pdfFileName  ="ATX_Info_only_MER"

DIR          ="/mnt/glusterfs/afp_news/lredondo/Actas2018TSE/1/" 
DIR	     = DIRMER
#pdfFileName  ="ATX_Info_fake"
#FAKEMERS     ="fake_mers.csv";

#fakes        = [line.rstrip('\n') for line in open(FAKEMERS)]        


counter = 0;
STEPS   = 60;
TOTAL   = height;
TOTAL_PAGES = 2000;
pages   = 0;
working_slice = [None]*100
CSV_ONLY =  False;
acta_type ="104"


filecsv = open("mers_id.csv", "w");

filecsv.write("int_mer_id, ACTA_TYPE, WITH, HEIGHT, DPI_X, DPI_Y, IN_MER\n");
idx = 0;
print "Listing ..."+DIR
for img in os.listdir(DIR):
#    print img+ "  "+str(pages+1)+"/"+str(TOTAL_PAGES);
    mer_id = img[:8];
    idx+=1	

    if (img.endswith("jpg")):
	IN_MER="NO"
        if (os.path.exists(DIRMER+img)):
                IN_MER="YES"
	acta_type = mer_id[5:9];

        print str(idx)+"  "+DIR+img+ "  "+acta_type+"  "+str(pages+1)+"/"+str(TOTAL_PAGES)+" IN_MER ="+IN_MER;
	cover = Image.open(DIR+img);
	w, h = cover.size; 
	info   = cover.info
	try:
    	   x, y  = info['dpi']
	except KeyError, e:
	   x=-1;
	   y=-1;
	#cover.convert('1') 	

        bbox  = (0, 0, 512, 25)

	filecsv.write(mer_id[:5]+"," + mer_id[5:9] +","+str(w)+","+str(h)+","+str(x)+","+str(y)+","+IN_MER+"\n");
	if (CSV_ONLY):
		continue;
		
	if (counter==0):
               pdf.add_page();

	pdf.set_xy(0,counter);
	pdf.set_font("Arial", size=12)
        pdf.cell(10,10, img+"     "+str(w)+"x"+str(h)+"   DPI: "+str(x)+"x"+str(y)+" IN MER : "+IN_MER )

	tmpid = str(uuid.uuid4());
        working_slice = cover.crop(bbox)
	working_slice.save(tmpid+".png","PNG");
	pdf.set_xy(20, counter+14)
	pdf.image(tmpid+".png", 20, counter+14);
	os.remove(tmpid+".png");
	counter += STEPS;
	if (counter>=TOTAL):
		 counter =  0;
		 pages   += 1

	if (pages>=TOTAL_PAGES):
		 break;
	#cover.close();
    else:
	print mer_id +" Error"
	filecsv.write(mer_id[:5]+","+" Error\n")

print "Writing.........   "+pdfFileName
if (not CSV_ONLY):	
  pdf.output(pdfFileName + ".pdf", "F")
  pdf.close()
print ".... Done..." 
filecsv.close();
