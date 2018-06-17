import csv
from pymongo import MongoClient
import http.client
import json
from pprint import pprint
client = MongoClient()
client = MongoClient("mongodb://localhost:27017")
db = client.Naukrijobpostings
#----------------------------------------------------------------------

def csv_reader(file_obj):
    """
    Read a csv file
    """
    count = 0
    c=0
    reader1 = csv.reader(file_obj)
    print(reader1)

    l=[]
    for row in reader1:
        #print(row)
        if("IT-Software" in row[3]):
            l.append(row[0])
            c=c+1
        count=count+1
    print("count of entries in excel"+"->"+str(count))
    print("count of entires having IT in them"+"->"+str(c))



    s=(set(l))
    print("length of diff IT comapnies are"+"->"+str(len(s)))
    industry=s
    c1=0
    for i in s:
        #print(i)
        c1=c1+1
    print("lenght of set"+"->"+str(c1))
    return s
global industry
industry=[]
def csv_reader1(file_obj,industry):
    """
    Read a csv file
    """
    count = 0
    c=0
    count1=0
    reader2 = csv.reader(file_obj)
    print(reader2)

    for row in reader2:
        if(count>3000 and count<=4000):
            print(row)
            print("in")
            if("IT" in row[3]):
                print("in it")
                if(row[0] in industry):
                    print("hurrah")
                    industry_type = row[3]
                    company_name = row[0]
                    c = company_name.split(" ")
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
                    conn = http.client.HTTPConnection("api.glassdoor.com")

                    headers = {
                        't.p': "233203",
                        't.k': "jrTfWk5uhyu",
                        'cache-control': "no-cache",
                        # 'postman-token': "18adc21e-a226-5106-595d-631f3f0c8a70"
                    }
                    conn.request("GET",
                                 "http://api.glassdoor.com/api/api.htm?t.p=233203&t.k=jrTfWk5uhyu&format=json&v=1&action=employers&q" + "=" + s,
                                 headers=headers)
                    res = conn.getresponse()
                    data = res.read()
                    r = data.decode("utf-8")
                    r1=0
                    count_d=0
                    data1 = json.loads(r)
                    print(company_name + "->" + str(data1['success']))
                    education = row[1]
                    experience = row[2]
                    position = row[6]
                    job_description = row[4]
                    if (data1['success'] == True):
                        #print("hurrah")
                        count_d=count_d+1
                        data2 = (data1["response"])
                        if (len(data2) != 0):
                            pprint(data2)
                            d = (data2["employers"])
                            if (len(d) != 0):
                                y = d[0]

                                pprint(d[0])
                                print(y['overallRating'])
                                y1 = y['overallRating']
                                r1=r1+1
                                result = db.jobpostings.insert_one(
                                    {
                                        "company_name": company_name,
                                        "education": education,
                                        "experience": experience,
                                        "position": position,
                                        "industry": industry_type,
                                        "job_description": job_description,
                                        "rating": y1
                                    })
                    else:
                        print("no res")
                    count1=count1+1
            count=count+1
        elif(count<=3000):
            count=count+1
    print("count of companies having IT keyword in them"+str(count))
    print("count of loop"+str(count1))
    print("count of companies which returned true response"+str(count_d))
    print("count of companies which returned rating "+str(r1))
#----------------------------------------------------------------------
if __name__ == "__main__":
    csv_path = "naukri_com-job_sample.csv"
    with open(csv_path,  "rt", encoding="utf8") as f_obj:
        industry=(csv_reader(f_obj))
        print("lenght of industries returned"+str((len(industry))))
    with open(csv_path,  "rt", encoding="utf8") as f_obj:
        csv_reader1(f_obj,industry)


