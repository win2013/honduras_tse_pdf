
echo "Creading and downloading files from TSE - Amazon's S3 bucket"
mkdir presidente
mkdir diputados
mkdir alcalde

cd presidente
curl -o "#1.JPG" https://s3.amazonaws.com/uploadtrailhn/[00001-18128]104.JPG
curl -I -o "#1.timestamp.txt" https://s3.amazonaws.com/uploadtrailhn/[00001-18128]104.JPG

cd..
cd diputados
curl -o "#1.JPG" https://s3.amazonaws.com/uploadtrailhn/[00001-18128]405.JPG
curl -I -o "#1.timestamp.txt" https://s3.amazonaws.com/uploadtrailhn/[00001-18128]405.JPG
cd ..

cd alcalde
curl -o "#1.JPG" https://s3.amazonaws.com/uploadtrailhn/[00001-18128]606.JPG
curl -I -o "#1.timestamp.txt" https://s3.amazonaws.com/uploadtrailhn/[00001-18128]505.JPG

