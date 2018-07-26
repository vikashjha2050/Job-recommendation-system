from flask import Flask, render_template, redirect, url_for, request
from sklearn import preprocessing
import pandas as pd

app = Flask(__name__)

def algocomp(cgpa,pref1,pref2,pref3,skill12,equal12):
    # a = [[5.6, "java", "c", "c++", "algorithm", "NAME= VIKASH KUMAR"],
    #      [7.5, "android", "java", "c++", "hive", "NAME= sashawat yadav"],
    #      [9.6, "android", "php", "sql", "c", "NAME= priyesh jalan"]]
    # print(cgpa)
    # print(pref1)

    csv_path = "person.csv"
    a = pd.read_csv(csv_path)
    a=a.values.tolist()
    print(a)

    def simple(mat):
        print("simple wala called")
        weight = [4, 3, 2, 1]
        print(weight[0])

        for i in range(len(mat)):
            mat[i][0]=mat[i][0]/10
        print(mat)

        score = [0 for x in range(len(mat))]
        print(score)
        for i in range(len(mat)):
            for j in range(4):
                score1 = mat[i][j] * weight[j]
                print(score1)
                score[i]=score1+score[i]
                print(score[i])
            cga[i].insert(0, score[i])

        print(score)
        cga.sort(key=lambda x: x[0], reverse=True)
        print(cga)
        return cga

    def skillfun(mat):
        print("skill wala called")
        weight = [1, 4, 3, 2]
        print(weight)

        for i in range(len(mat)):
            mat[i][0]=mat[i][0]/10
        print(mat)

        score = [0 for x in range(len(mat))]
        for i in range(len(mat)):
            for j in range(4):
                score1 = mat[i][j] * weight[j]
                score[i]=score1+score[i]
            cga[i].insert(0, score[i])

        print(score)
        cga.sort(key=lambda x: x[0], reverse=True)
        print(cga)
        return cga

    def equalfun(mat):
        print("equal wala called")
        weight = [1, 1, 1, 1]
        print(weight)

        for i in range(len(mat)):
            mat[i][0]=mat[i][0]/10
        print(mat)

        score = [0 for x in range(len(mat))]
        for i in range(len(mat)):
            for j in range(4):
                score1 = mat[i][j] * weight[j]
                score[i]=score[i]+score1
            cga[i].insert(0, score[i])

        print(score)

        cga.sort(key=lambda x: x[0], reverse=True)
        print(cga)
        return cga

    cga = []
    for i in range(len(a)):
        print(a[i][0])
        if a[i][0] > float(cgpa):
            cga.append(a[i])
    print(cga)

    mat = [[0 for x in range(4)] for y in range(len(cga))]
    for i in range(len(cga)):
        for j in range(len(cga[i])):
            if (cga[i][j] == pref1):
                mat[i][1] = 1
            if (cga[i][j] == pref2):
                mat[i][2] = 1
            if (cga[i][j] == pref3):
                mat[i][3] = 1

    for i in range(len(cga)):
        mat[i][0] = cga[i][0]

    print(mat)
    if (skill12 == "skill12"):
        t=skillfun(mat)
        return t
    elif (equal12 == "equal12"):
        t=equalfun(mat)
        return t
    else:
        t=simple(mat)
        return t

@app.route('/put')
def student():
   return render_template('companyinput.html')


@app.route('/comp21', methods=['GET', 'POST'])
def uploadcompdata():
    if request.method == 'POST':
        cgpa = request.form['cgpa']
        pref1 = request.form['pref1']
        pref2 = request.form['pref2']
        pref3 = request.form['pref3']
        skill12 = request.form.get('skill2')
        equal12 = request.form.get('equal2')
        array=[cgpa,pref1,pref2,pref3]
        print(array)
        final = algocomp(cgpa,pref1,pref2,pref3,skill12,equal12)
        print(final)
        return render_template('resultcomp.html',result=final,result2=array)

if __name__ == '__main__':
    app.run()
