from flask import Flask, render_template, request,redirect,url_for
from werkzeug.utils import secure_filename
import PyPDF2
from pprint import pprint
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
import numpy as np
from sklearn.cluster import MeanShift, KMeans
from sklearn import preprocessing, cross_validation
import pandas as pd
from pprint import pprint
from collections import Counter
WORD = re.compile(r'\w+')

app = Flask(__name__)
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

def algo2():
    df = pd.read_csv('names.csv', encoding="ISO-8859-1")
    # df = pd.read_excel('titanic.xls')
    original_df = pd.DataFrame.copy(df)
    df.drop(['education', 'jobdescription'], 1, inplace=True)
    df.fillna(0, inplace=True)

    def handle_non_numerical_data(df):
        # handling non-numerical data: must convert.
        columns = df.columns.values

        for column in columns:
            text_digit_vals = {}

            def convert_to_int(val):
                return text_digit_vals[val]

            # print(column,df[column].dtype)
            if df[column].dtype != np.int64 and df[column].dtype != np.float64:

                column_contents = df[column].values.tolist()
                # finding just the uniques
                unique_elements = set(column_contents)
                # great, found them.
                x = 0
                for unique in unique_elements:
                    if unique not in text_digit_vals:
                        # creating dict that contains new
                        # id per unique string
                        text_digit_vals[unique] = x
                        x += 1
                # now we map the new "id" vlaue
                # to replace the string.
                df[column] = list(map(convert_to_int, df[column]))

        return df

    df = handle_non_numerical_data(df)
    # df.drop(['], 1, inplace=True)

    X = np.array(df.drop(['rating'], 1).astype(float))
    X = preprocessing.scale(X)
    y = np.array(df['rating'])

    clf = MeanShift()
    clf.fit(X)
    labels = clf.labels_
    cluster_centers = clf.cluster_centers_
    original_df['cluster_group'] = np.nan
    for i in range(len(X)):
        original_df['cluster_group'].iloc[i] = labels[i]
    n_clusters_ = len(np.unique(labels))
    survival_rates = {}
    for i in range(n_clusters_):
        temp_df = original_df[(original_df['cluster_group'] == float(i))]
        # print(temp_df.head())

        survival_cluster = temp_df[(temp_df['rating'] == 1)]

        survival_rate = len(survival_cluster) / len(temp_df)
        # print(i,survival_rate)
        survival_rates[i] = survival_rate

    #print(survival_rates)
    l=original_df[(original_df['cluster_group'] == 1)]
    pprint(original_df[(original_df['cluster_group'] == 1)])
    #pprint(original_df[(original_df['cluster_group'] == 2)])
    #pprint(original_df[(original_df['cluster_group'] == 3)])
    l.apply(lambda y: y.tolist(), axis=1)
    s1=l['company']

    print("company belongs"+s1)
    return s1



def algo(s):

    client = MongoClient("mongodb://localhost:27017")
    db = client.NaukriProfile
    col = db.userprofile.find()
    count = 0
    company = []
    for i in col:
        count = count + 1
        print(i['skill'])
        new = i['skill'].lower()
        new1 = new.split(",")
        print(new1)
        c = 0

        vector1 = text_to_vector(i['skill'])
        vector2 = text_to_vector(s)
        cosine = get_cosine(vector1, vector2)
        print(cosine)
        if (cosine > 0.1):
            company.append(i['organization'])
    print(count)
    print(company)
    print("lenght of company is" + "->" + str(len(set(company))))
    conn = http.client.HTTPConnection("api.glassdoor.com")

    headers = {
        't.p': "233203",
        't.k': "jrTfWk5uhyu",
        'cache-control': "no-cache",
        # 'postman-token': "18adc21e-a226-5106-595d-631f3f0c8a70"
    }
    count_cmp=0
    l_rating=[]
    print(count_cmp)
    for i in set(company):
        if(count_cmp<=50):
            count_cmp=count_cmp+1
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
            #print(s)
            conn.request("GET",
                         "http://api.glassdoor.com/api/api.htm?t.p=233203&t.k=jrTfWk5uhyu&format=json&v=1&action=employers&q" + "=" + s,
                         headers=headers)

            res = conn.getresponse()
            data = res.read()
            r = data.decode("utf-8")
            data1 = json.loads(r)

            #print(data1['success'])
            if (data1['success'] == True):
                # print("hurrah")

                data2 = (data1["response"])
                if (len(data2) != 0):
                    #pprint(data2)
                    d = (data2["employers"])
                    if (len(d) != 0):
                        y = d[0]

                        #pprint(d[0])
                        #print(y['overallRating'])
                        y1 = y['overallRating']
                        #print(y1)
                        l_rating.append(y1)

    #print(len(l_rating))
    #print(l_rating)
    with open('final.csv', 'w',encoding="utf-8") as csvfile:
        fieldnames = ['company', 'education', 'experience', 'industry', 'jobdescription', 'joblocation', 'jobtitle',
                      'numberofpositions', 'skills', 'rating', 'pay']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print("hi")
        with open("names.csv",  "rt") as f_obj:
            reader2 = csv.reader(f_obj)
            for row in reader2:
                company = row[0]
                print(company)
                education = row[1]
                experience = row[2]
                industry = row[3]
                jobdescription = row[4]

                jobtitle = row[6]

                skills = row[7]
                pay = row[9]
                rat=row[8]
                print(rat)
                if(rat in l_rating):
                    print("hurrah")
                    d = {'company': company, 'education': education, 'experience': experience, 'industry': industry,
                         'jobdescription': jobdescription, 'jobtitle': jobtitle,
                         'skills': skills, 'rating': rat, 'pay': pay}

                    writer.writerow(d)




def readPDF(var):
    pdfFileObj = open(var, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    x=pageObj.extractText()
    lines = list(filter(bool,x.split('\n')))

    custData = {}
    for i in range(len(lines)):
        if 'CAREER OBJECTIVE' in lines[i]:
            custData['career_objective'] = lines[i+2] + lines[i+3]
        elif 'EDUCATION' in lines[i]:
            custData['education'] =lines[i+15] +lines[i+16]+ lines[i+17] +lines[i+18] +lines[i+19]+lines[i+20]+ lines[i+21] +lines[i+22] +lines[i+23]+lines[i+24] +lines[i+25] +lines[i+26]+ lines[i+27] +lines[i+28] +lines[i+29]+lines[i+30]+ lines[i+31] +lines[i+32] +lines[i+33]+lines[i+34] +lines[i+35] +lines[i+36]+ lines[i+37] +lines[i+38] +lines[i+39]+lines[i+40]+ lines[i+41] +lines[i+42] +lines[i+43]+lines[i+44] +lines[i+45] +lines[i+46]+ lines[i+47] +lines[i+48] +lines[i+49]
        elif 'EXPERIENCE' in lines[i]:
            custData['experience'] = lines[i+2] +lines[i+3] +lines[i+4]+ lines[i+5] +lines[i+6] +lines[i+7]+lines[i+8] +lines[i+9] +lines[i+10]+ lines[i+11] +lines[i+12] +lines[i+13]+lines[i+14] +lines[i+15] +lines[i+16]+ lines[i+17] +lines[i+18] +lines[i+19]+lines[i+20]+ lines[i+21] +lines[i+22] +lines[i+23]+lines[i+24] +lines[i+25] +lines[i+26]+ lines[i+27]
        elif 'PROJECTS' in lines[i]:
            custData['projects']= lines[i+2] +lines[i+3] +lines[i+4]+ lines[i+5] +lines[i+6] +lines[i+7]+lines[i+8] +lines[i+9] +lines[i+10]+ lines[i+11] +lines[i+12] +lines[i+13]+lines[i+14] +lines[i+15]

    pageObj1 = pdfReader.getPage(1)
    x1=pageObj1.extractText()
    pdfFileObj.close()
    lines = list(filter(bool, x1.split('\n')))
    #print(lines)
    for i in range(len(lines)):
        if 'TECHNI' in lines[i]:
            custData['tech_skills'] = lines[i+5] +lines[i+6] +lines[i+7] +lines[i+9] +lines[i+10] +lines[i+12] +","+lines[i+13]+lines[i+14] +","+lines[i+15] +lines[i+16] +lines[i+18]+"," +lines[i+19]+lines[i+20]+ lines[i+21]+"," +lines[i+22] +lines[i+23]+lines[i+24] +lines[i+25]+"," +lines[i+28]+lines[i+29]


    # print(custData)
    # print(custData1)
    return custData

@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print(f.filename + "  " + 'file uploaded successfully')
        #return f.filename + " + 'file uploaded successfully'
        #READING
        mystr=readPDF(f.filename)
        s=(mystr['tech_skills'])
        algo(s)
        t=algo2()
        print("result"+t)
        return render_template('uploader.html',result=mystr,new=t)

if __name__ == '__main__':
    app.run()
