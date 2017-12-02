# honduras_tse_pdf
Creador de PDF De las actas del TSE en Amazon S3 o en su computadora local
# honduras_tse_pdf

Run the following programs in multiple nodes in your cloud 

Install PILLOW and FPDF in your machine with Python 2.7
git clone https://github.com/python-pillow/Pillow.git
git clone https://github.com/Setasign/FPDF.git

cd PILLOW 
python setup.py install
cd ..
cd fpdf
python setup.py install
cd ..

Install all TSE Resources:
run download.sh 

Make sure all install, the files are in JPEG format from API.TSE.HN
The created file structure would be:

alcaldes/*
diputados/*
presidente/*
pdfs/*

All the "ACTAS" will be pulled from alcaldes/* diputados/* and presidente/* and merged into pdfs, the metadata from the PDF created
comes from the timestamp is arriving from AWS from the header data.


And run the follwing in several machines. 

python processtoPDF.py 10000 11000 pdfs/data_1000to11000.csv 
python processtoPDF.py 11001 12000 pdfs/data_1100to12000.csv 

and so on, 

 
