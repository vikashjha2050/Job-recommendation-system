import PyPDF2
#from pymongo import MongoClient
#client = MongoClient()
#db = client.test

# creating a pdf file object
pdfFileObj = open('resume.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())
x=pageObj.extractText()

lines = list(filter(bool,x.split('\n')))

print(lines)
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
print(custData)

pageObj1 = pdfReader.getPage(1)

# extracting text from page
print(pageObj1.extractText())
x1=pageObj1.extractText()

# closing the pdf file object
pdfFileObj.close()
lines = list(filter(bool,x1.split('\n')))

print(lines)

custData1 = {}
l=[]
for i in range(len(lines)):
    if 'TECHNI' in lines[i]:
        custData1['tech_skills'] = lines[i+4]+ lines[i+5] +lines[i+6] +lines[i+7]+lines[i+8] +lines[i+9] +lines[i+10]+ lines[i+11] +lines[i+12] +lines[i+13]+lines[i+14] +lines[i+15] +lines[i+16]+ lines[i+17] +lines[i+18] +lines[i+19]+lines[i+20]+ lines[i+21] +lines[i+22] +lines[i+23]+lines[i+24] +lines[i+25] +lines[i+26]+ lines[i+27]+lines[i+28]+lines[i+29]
    #for i in custData1['tech_skills']:
     #   l.append(i)
#l=(custData1['tech_skills'])
print(str(custData1['tech_skills']))

