from flask import Flask, render_template, redirect, url_for, request
import csv
app = Flask(__name__)

@app.route('/stu')
def student():
   return render_template('studentinput.html')


@app.route('/stu21', methods=['GET', 'POST'])
def upload_studentdata():
    if request.method == 'POST':
        cgpa = request.form['cgpa']
        s1 = request.form['skills1']
        s2 = request.form['skills2']
        s3 = request.form['skills3']
        s4 = request.form['skills4']
        s5 = request.form['skills5']
        s6 = request.form['skills6']
        print(pref1)

        with open('person.csv', 'a') as csvfile:
            fieldnames = ['cgpa', 'skills1','skills2','skills3','skills4','skills5',"name"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'cgpa': cgpa, 'skills1': s1,'skills2': s2,'skills3': s3,'skills4': s4,'skills5': s5, "name":s6})

        csvfile.close()

    return render_template('studentinput.html')


if __name__ == '__main__':
    app.run()
