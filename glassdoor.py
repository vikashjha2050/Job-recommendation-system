import http.client
import json
from pprint import pprint
conn = http.client.HTTPConnection("api.glassdoor.com")

headers = {
    't.p': "233203",
    't.k': "jrTfWk5uhyu",
    'cache-control': "no-cache",
    #'postman-token': "18adc21e-a226-5106-595d-631f3f0c8a70"
    }

conn.request("GET", "http://api.glassdoor.com/api/api.htm?t.p=233203&t.k=jrTfWk5uhyu&format=json&v=1&action=employers&q=Accenture", headers=headers)

res = conn.getresponse()
data = res.read()
r=data.decode("utf-8")
data1=json.loads(r)
print(data1['success'])
if(data1['success'] == True):
    print("hurraj")
data2=(data1["response"])
pprint(data2)
d=(data2["employers"])
y=d[0]
pprint(d[0])
print(y['overallRating'])






