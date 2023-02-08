#Extracting data from web URL
echo "Extracting data"

wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz"

echo "Unzipping data"

gunzip -f web-server-access-log.txt.gz > extract.txt

cut -d"#" -f1-4 extract.txt 

#Transforming data
echo "Transforming Data"
tr "#" "," < extract.txt > transform.csv

#Load data into Postgres Database
echo "\c template1;\COPY access_log  FROM '/home/project/server_access/transform.csv' DELIMITERS ',' CSV;" | psql --username=postgres --host=localhost
