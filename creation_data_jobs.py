import requests
import csv
from pymongo import MongoClient
import json
from pprint import pprint
client = MongoClient()
client = MongoClient("mongodb://localhost:27017")
db = client.Naukrijobpostings
col=db.jobpostings.find()
count=0
global d
d={}
cmp_count=0
with open('names.csv', 'w') as csvfile:
    fieldnames = ['company', 'education', 'experience', 'industry', 'jobdescription', 'joblocation', 'jobtitle',
                  'numberofpositions', 'skills', 'rating','pay']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in col:
        if(count==0):
            print(i)
            print(i['company_name']+"->"+i['rating'])
            #count=count+1
            cmp_count=0
            csv_path = "naukri_com-job_sample.csv"
            with open(csv_path, "rt", encoding="utf8") as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:

                    company=row[0]
                    education=row[1]
                    experience=row[2]
                    industry=row[3]
                    jobdescription=row[4]
                    joblocation=row[6]
                    jobtitle=row[7]
                    numberofpositions=row[8]
                    skills=row[11]
                    pay=row[9]
                    #print("company name"+company)
                    if((i['company_name']==company) and (cmp_count==0)):
                        print("hurrah")
                        print(company)
                        cmp_count=cmp_count+1
                        d={'company':company,'education':education,'experience':experience,'industry':industry,'jobdescription':jobdescription,'jobtitle':jobtitle,'numberofpositions':numberofpositions,'skills':skills,'rating':i['rating'],'pay':pay}


                        pprint(d)
                        writer.writerow(d)

