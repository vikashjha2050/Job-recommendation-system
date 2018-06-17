import requests
import csv
import pymongo
from pymongo import MongoClient
import json
import csv
import http.client
import json
import PyPDF2
from pprint import pprint
URL="http://52.172.44.219:4040/testingNaukariCandidate.php"
r=requests.get(url=URL)
p=r.json()
l=(p.keys())
print(l)
global count
count=0
l=sorted(l)
print(l)
client = MongoClient()
client = MongoClient("mongodb://localhost:27017")
db = client.NaukriProfile
count=0
n=[]
company=[]
n1=[]
c1=0
names=[]
global custData1
custData1={}
def resume():
    pdfFileObj = open('resume.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    x = pageObj.extractText()
    lines = list(filter(bool, x.split('\n')))

    custData = {}
    for i in range(len(lines)):
        if 'CAREER OBJECTIVE' in lines[i]:
            custData['career_objective'] = lines[i + 2] + lines[i + 3]
        elif 'EDUCATION' in lines[i]:
            custData['education'] = lines[i + 15] + lines[i + 16] + lines[i + 17] + lines[i + 18] + lines[i + 19] + \
                                    lines[i + 20] + lines[i + 21] + lines[i + 22] + lines[i + 23] + lines[i + 24] + \
                                    lines[i + 25] + lines[i + 26] + lines[i + 27] + lines[i + 28] + lines[i + 29] + \
                                    lines[i + 30] + lines[i + 31] + lines[i + 32] + lines[i + 33] + lines[i + 34] + \
                                    lines[i + 35] + lines[i + 36] + lines[i + 37] + lines[i + 38] + lines[i + 39] + \
                                    lines[i + 40] + lines[i + 41] + lines[i + 42] + lines[i + 43] + lines[i + 44] + \
                                    lines[i + 45] + lines[i + 46] + lines[i + 47] + lines[i + 48] + lines[i + 49]
        elif 'EXPERIENCE' in lines[i]:
            custData['experience'] = lines[i + 2] + lines[i + 3] + lines[i + 4] + lines[i + 5] + lines[i + 6] + lines[
                i + 7] + lines[i + 8] + lines[i + 9] + lines[i + 10] + lines[i + 11] + lines[i + 12] + lines[i + 13] + \
                                     lines[i + 14] + lines[i + 15] + lines[i + 16] + lines[i + 17] + lines[i + 18] + \
                                     lines[i + 19] + lines[i + 20] + lines[i + 21] + lines[i + 22] + lines[i + 23] + \
                                     lines[i + 24] + lines[i + 25] + lines[i + 26] + lines[i + 27]
        elif 'PROJECTS' in lines[i]:
            custData['projects'] = lines[i + 2] + lines[i + 3] + lines[i + 4] + lines[i + 5] + lines[i + 6] + lines[
                i + 7] + lines[i + 8] + lines[i + 9] + lines[i + 10] + lines[i + 11] + lines[i + 12] + lines[i + 13] + \
                                   lines[i + 14] + lines[i + 15]

    pageObj1 = pdfReader.getPage(1)
    x1 = pageObj1.extractText()
    pdfFileObj.close()
    lines = list(filter(bool, x1.split('\n')))
    print(lines)
    #custData1 = {}
    for i in range(len(lines)):
        if 'TECHNI' in lines[i]:
            custData1['tech_skills'] = lines[i + 5] + lines[i + 6] + lines[i + 7] + lines[i + 9] + lines[i + 10] + \
                                       lines[i + 12] + lines[i + 13] + lines[i + 14] + lines[i + 15] + lines[i + 16] + \
                                       lines[i + 18] + lines[i + 19] + lines[i + 20] + lines[i + 21] + lines[i + 22] + \
                                       lines[i + 23] + lines[i + 24] + lines[i + 25] + lines[i + 28] + lines[i + 29]

    print(custData)
    print(custData1)


#print("length of company in excel"+str(len(c)))
resume()
l1=(custData1['tech_skills'])
result1=l1.split(",")
print(result1)
skills=['C++','Python','Html']
for i in l:
    #print(i)


    if(count==112):
        print(str(i)+"hello")

    else:
       name = (p[i]["candidateName"])
       print(name)
       names.append(name)
       c1=c1+1
       exp=(p[i]["experience"])
       current_ctc=p[i]["current_ctc"]
       current_loc=p[i]["location"]
       des_loc=p[i]["preferred_location"]
       skill=p[i]["key_skills"]

       if(len(exp)>0 and (exp!="Fresher")):
          w=(p[i]["work_experience"])
          w1=p[i]["work_summary"]
          #print(w1)
          #print(w1["industry"])
          if("IT" in w1["industry"]):
              for k in range(0,len(w)):
              #print(w[k]["organization"])
                  org=w[k]["organization"]
                  n.append(w[k]["organization"])
                  #res=db.userprofile.insert_one(
                   # {
                    #    "CandidateName":name,
                     #   "experience":exp,
                      #  "ctc":current_ctc,
                       # "location":current_loc,
                        #"desiredlocation":des_loc,
                        #"organization":org,
                        #"skill":skill


#                    }
 #               )
          #print(str(i)+"name"+p[i]["candidateName"]+"Count val"+str(count))

    count=count+1
naukriset=(set(n))
l=[]
print("Count of names"+str(c1))
print("count of set names"+str(len(set(names))))
#print(n1)
#print(len(naukriset))
#print(len(c))
#print(len(naukriset.intersection(c)))
#comp=naukriset.intersection(c)
#print(comp)