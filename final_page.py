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
import re, math
from collections import Counter

WORD = re.compile(r'\w+')
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


text1 = 'This is a foo bar sentence .'
text2 = 'This sentence is similar to a foo bar sentence .'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print('Cosine:', cosine)
client = MongoClient()
client = MongoClient("mongodb://localhost:27017")
db = client.NaukriProfile
col=db.userprofile.find()
pr=['C/C++', ' Java', '  HTML', ' CSS', 'Python        MySql  Android Studio', ' Zeplin', ' JIRA  SDK             :   Vuforia (augmented reality sdk)  Linux', ' Windows ']
count=0
company=[]
for i in col:
    count=count+1
    print(i['skill'])
    new=i['skill'].lower()
    new1=new.split(",")
    print(new1)
    c=0
    str1 = ''.join(pr)
    vector1 = text_to_vector(i['skill'])
    vector2 = text_to_vector(str1)
    cosine = get_cosine(vector1, vector2)
    print(cosine)
    if(cosine>0.1):
        company.append(i['organization'])
print(count)
print(company)
print("lenght of company is"+"->"+str(len(set(company))))
conn = http.client.HTTPConnection("api.glassdoor.com")

headers = {
    't.p': "233203",
    't.k': "jrTfWk5uhyu",
    'cache-control': "no-cache",
    #'postman-token': "18adc21e-a226-5106-595d-631f3f0c8a70"
    }
for i in set(company):
    c = i.split(" ")
    s = ""
    if (len(c) == 1):
        s = c[0]
    else:
        for i in range(0, len(c)):
            if (i == 0):
                s = c[i] + "%20"
            elif (i == (len(c) - 1)):
                s = s + c[i]
            else:
                s = s + c[i] + "%20"
    print(s)
    conn.request("GET", "http://api.glassdoor.com/api/api.htm?t.p=233203&t.k=jrTfWk5uhyu&format=json&v=1&action=employers&q"+"="+s, headers=headers)

    res = conn.getresponse()
    data = res.read()
    r=data.decode("utf-8")
    data1=json.loads(r)
    l_rating=[]
    print(data1['success'])
    if (data1['success'] == True):
        # print("hurrah")

        data2 = (data1["response"])
        if (len(data2) != 0):
            pprint(data2)
            d = (data2["employers"])
            if (len(d) != 0):
                y = d[0]

                pprint(d[0])
                print(y['overallRating'])
                y1 = y['overallRating']
                print(y1)
                l_rating.append(y1)

print(len(l_rating))