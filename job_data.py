from bs4 import BeautifulSoup
import urllib
import requests
r = requests.get('https://www.indeed.co.in/cmp/%5B24%5D7-Inc.')
r1=r.text
soup = BeautifulSoup(r1,"html.parser")
#print(soup)
x=soup.find_all('div')
print(x)
#for i in x:
#    y=i.find_all('a')
#    for t in y:
#        q=t.get('href')
#        q1=q[7:]
#        #print(q1)
#        q1=q1.split('&')[0]
#        print(q1)
#        if( "glassdoor" in q1):
#            link=q1
 #           break
#print(link)
#r2=requests.get(link)
#soup=BeautifulSoup(r2,"html.parser")
#print(soup)

#for link in soup.find_all('a'):
#    print(link.get('href'))