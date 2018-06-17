from flask import Flask, render_template, redirect, url_for, request
import csv
app = Flask(__name__)

@app.route('/stu')
def student():
   return render_template('student.html')


@app.route('/stu21', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        cgpa = request.form['cgpa']
        pref1 = request.form['pref1']
        pref2 = request.form['pref2']
        pref3 = request.form['pref3']
        pref4 = request.form['pref4']
        pref5 = request.form['pref5']
        pref6 = request.form['pref6']
        print(pref1)

        with open('person.csv', 'a') as csvfile:
            fieldnames = ['cgpa', 'skills1','skills2','skills3','skills4','skills5',"name"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'cgpa': cgpa, 'skills1': pref1,'skills2': pref2,'skills3': pref3,'skills4': pref4,'skills5': pref5, "name":pref6})

        csvfile.close()

    return render_template('student.html')


if __name__ == '__main__':
    app.run()