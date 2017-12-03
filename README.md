# honduras_tse_pdf
Creador de PDF De las actas del TSE en Amazon S3 o en su computadora local
Fechtes the API.TSE.HN to retrieve the number of votes for Presidential race, only


# Description

This application runs on Mac/Linux may need to be updated for Windows. Uses PDF Creator, Image processing, 
and JSON request. 

Using python, to connect to the list of S3 buckets related to the Honduran TSE, retrieving all instances of each MER
MER or Mesa Electoral Receptora is a unique ID for each table.

The tables are then fetched from Amzzon S3's bucket, and most likely pushed after the ballots are counted..

TSE uses the format : [ER_ID]106.JPG for president, [MER_ID]606.JPG for alcalde, [MER_ID]405.JPG for diputado. 

## Setup and initial configuration
Run the following programs in multiple nodes in your cloud 

Install PILLOW and FPDF in your machine with Python 2.7
* git clone https://github.com/python-pillow/Pillow.git
* git clone https://github.com/Setasign/FPDF.git

## Configuration after git clone is perfomed
```
cd PILLOW 
python setup.py install
cd ..
cd fpdf
python setup.py install
cd ..
```

## Install all TSE Images and  Resources:
```-
run download.sh 
```

Make sure all JPEGs install with metadata from S3 bucket, the files are in JPEG format from API.TSE.HN The created file structure would be:

```
alcaldes/*
diputados/*
presidente/*
pdfs/*
```

All the "ACTAS" will be pulled from alcaldes/* diputados/* and presidente/* and merged into pdfs, the metadata from the PDF created
comes from the timestamp is arriving from AWS from the header data.


And run the follwing in several machines. 
...
python processtoPDF.py 10000 11000 pdfs/data_1000to11000.csv 
python processtoPDF.py 11001 12000 pdfs/data_1100to12000.csv 
```

and to create a table with the JPEG image sizes, and all teh votes for each prescint.
```
python findresolutions.py 1 18180  > data_mining.csv
```
 
