import csv
import pandas as pd

cgpa=5
pref1="algorithm"
pref2="c"
pref3="java"

a = [[5.6, "java", "c", "c++", "algorithm", "NAME= VIKASH KUMAR"],
     [7.5, "android", "java", "c++", "hive", "NAME= sashawat yadav"],
     [9.6, "android", "php", "sql", "c", "NAME= priyesh jalan"]]

csv_path = "person.csv"

df = pd.read_csv(csv_path)
saved_column = df.skills
print(saved_column)

def simple(mat):
    weight = [4,3,2,1]
    print(weight)

    score=[0 for x in range (len(mat))]
    for i in range(len(mat)):
        for j in range (4):
          score[i]=score[i]+mat[i][j]*weight[i]
        cga[i].insert(0,score[i])

    print(score)
    print(cga)

    cga.sort(key = lambda x: x[0],reverse=True)
    print(cga)
    return cga

def skillfun(mat):
    weight = [1,4,3,2]
    print(weight)

    score=[0 for x in range (len(mat))]
    for i in range(len(mat)):
        for j in range (4):
          score[i]=score[i]+mat[i][j]*weight[i]
        cga[i].insert(0,score[i])

    print(score)
    print(cga)

    cga.sort(key = lambda x: x[0],reverse=True)
    print(cga)
    return cga

def equalfun(mat):
    weight = [1,1,1,1]
    print(weight)

    score=[0 for x in range (len(mat))]
    for i in range(len(mat)):
        for j in range (4):
          score[i]=score[i]+mat[i][j]*weight[i]
        cga[i].insert(0,score[i])

    print(score)
    print(cga)

    cga.sort(key = lambda x: x[0],reverse=True)
    print(cga)
    return cga

cga=[]
for i in range(len(a)):
    print(a[i][0])
    if(a[i][0]>cgpa):
        cga.append(a[i])
print(cga)

mat = [[0 for x in range(4)] for y in range(len(cga))]
for i in range(len(cga)):
    for j in range(len(cga[i])):
        if (cga[i][j]==pref1):
            mat[i][1]=1
        if (cga[i][j]==pref2):
           mat[i][2]=1
        if (cga[i][j]==pref3):
           mat[i][3]=1

for i in range(len(cga)):
    mat[i][0]=cga[i][0]

print(mat)
check1=""
check2=""
if(check1=="skill12"):
   skillfun(mat)
elif(check2=="equal12"):
    equalfun(mat)
else:
    simple(mat)