# honduras_tse_pdf

Creator of PDF files from "TSE" in the Amazon S3 bucked, storing all data in your local filesystem.

The app techtes the API.TSE.HN to retrieve the number of votes for Presidential race, only


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
cd Pillow 
python setup.py install
cd ..
cd fpdf
python setup.py install
cd ..
```

## Install all TSE Images and  Resources:
```
chnod +x  downloads.sh 
./downloads.sh
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
```
python processtoPDF.py 10000 11000 pdfs/data_1000to11000.csv 
python processtoPDF.py 11001 12000 pdfs/data_1100to12000.csv 
```

### Finding Image Resoultions and Votind Data

You can  create a table with the JPEG image sizes, and all the votes for each prescint in CSV format.
This is a quick and dirty way of doing that by redirecting output to the CSV file, but we can use CSV module on python.
additionally, the app extracts the resolution of all images and inersts them as P_W and P_H: President Width and HEIGHT
and so on. 

```
python findresolutions.py 1 18180  > data_mining.csv
```
 
### Dropbox with all PDF files

* [Dropbox] ("https://www.dropbox.com/sh/cbqdmiu72er8c6a/AAAqmEAL4AZUrXcQziM7GLjja?dl=0") -- Repository with all PDF Files
