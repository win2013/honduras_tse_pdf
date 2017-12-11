from os.path import basename
import os;
import csv; 

database="data_mining.csv"
database="data_mining_dec09.csv"

def getTimeStamp(mer_id_file):
    #print "######## Timestamp for "+mer_id_file;
    data = ""
    if (os.path.exists(mer_id_file)):
        fdata= open(mer_id_file)
        data = fdata.readlines();
        #print data
        #print "TIMESTAMP: "
        #print " ".join(data[4].split(":")[1:]);
        # dateinfo = data[4].split(":")
        fdata.close();
        return data[4].split(":")[1:];

print ">>>>>>>>>> Posting Date per MER <<<<<<<<<<<<s"
sources = ["presidente", "diputados", "alcalde", "escrutinioesp"]

fdate = ["26 Nov 2017", "27 Nov 2017", "28 Nov 2017", "29 Nov 2017", "30 Nov 2017", 
	 "01 Dec 2017", "02 Dec 2017", "03 Dec 2017", "04 Dec 2017", "05 Dec 2017", 
	 "06 Dec 2017", "07 Dec 2017", "08 Dec 2017", "09 Dec 2017"]

count  = [  ] ; #    0,        0,         0,        0,        0,      0,     0];

actas_pres  = [  ] #   [],       [],        [],       [],       [],     [],    []];
actas_dip   = [  ] #  [],       [],        [],       [],       [],     [],    []]
actas_alc   = [  ] #  [],       [],        [],       [],       [],     [],    []]
actas_esp   = [   ]

fechas = []
for i in fdate:
  for j in range(0,24):
        fechas.append(i+" "+str(j).zfill(2));
        count.append(0);
	actas_pres.append([]);
	actas_dip.append([])
	actas_alc.append([]);
        actas_esp.append([])

print fechas;
#print count; 
#print actas_pres;
#print actas_dip;
#print actas_alc;

sn = {}
joh = {}
with open(database, 'rb') as csvfile:
      votingdata = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in votingdata:
	#print row; 
	mer_id           = row [0];
	if (len(row) > 3):
		snvotes          = row [8]
		johvotes         = row[10]; 
		sn[int(mer_id)]  = snvotes;
		joh[int(mer_id)] = johvotes;  
	else:
		sn[int(mer_id)]  = 0;
		joh[int(mer_id)] = 0;

 
for s in sources:
 for m in os.listdir(s):
    if ("timestamp" in m):
       mer_id = m.split(".")	
       #print "MER_ID  :"+ mer_id[0]
       fecha=getTimeStamp(s+"/"+mer_id[0]+".timestamp.txt")
       if (fecha!=None and len(fecha)>0):
	   # print fecha[0]
	   index = 0;
           if "Nov 2017" in fecha[0] or "Dec 2017" in fecha[0]:
	      index = next(index for (index, d) in enumerate(fechas) if d in fecha[0])	
	      if "presidente" in s:	
	         actas_pres[index].append(mer_id[0]);	
	      if "alcalde" in s:
		 actas_alc[index].append(mer_id[0]);
	      if "diputados" in s:
		 actas_dip[index].append(mer_id[0]);	
	      if "escrutinioesp" in s:
		 actas_esp[index].append(mer_id[0])

              count[index]+=1
        #   else:
	#		print "Not Found..."

print "____________ Fetching and counters _______ "      
print fechas
print count; 	

i = 0	
print "##### PRESIDENTE #####"

csv_pres_count       =  [ ]
csv_alcalde_count    =  [ ]
csv_diputado_count   =  [ ] 
csv_escrutinio_count =  [ ]

count_pres = [] ; 

for x in actas_pres:
   print fechas[i]+":00 GMT --------------------------------------------------"  
   output =""
   count_sn = 0;
   count_joh = 0;
   for y in x:
      count_sn += int(sn[int(y)]);
      count_joh += int(joh[(int(y))])
      output = output + "," + y 
   i = i+1;
   print output
   print "Count .... " +str(len(x));
   csv_pres_count.append(str(len(x)))
   count_pres.append([count_sn, count_joh])

i=0
print "##### DIPUTADOS #####"
for x in actas_dip:
   print fechas[i] +":00 GMT --------------------------------------------------"
   output =""
   for y in x:
       output = output + "," + y 
   i = i+1;
   print output;
   print "Count .... " +str(len(x));
   csv_alcalde_count.append(str(len(x)))
i=0


print "##### ALCALDES #####"
for x in actas_alc:
   print fechas[i]+":00 GMT --------------------------------------------------"
   output =""
   for y in x:
        output  = output + "," + y 
   i = i+1;
   print output; 
   print "Count .... " +str(len(x));
   csv_diputado_count.append(str(len(x)))

i=0;

print "##### ESCRUTINIO ESP #####"
for x in actas_esp:
   print fechas[i]+":00 GMT --------------------------------------------------"
   output =""
   for y in x:
        output  = output + "," + y
   i = i+1;
   print output;
   print "Count .... " +str(len(x));
   csv_escrutinio_count.append(str(len(x)))

print "Name, " +",".join(fechas);
print "##### PRESIDENT ####, "+", ".join(csv_pres_count)
print "##### DIPUTADOS ####, "+", ".join(csv_diputado_count)
print "##### ALCALDES  ####, "+", ".join(csv_alcalde_count)
print "------------------------------------------------------" 
print "Votes Inserted_by_date..."
print count_pres;
