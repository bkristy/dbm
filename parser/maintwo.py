import time
import sys, datetime, os, inspect
import urllib.request, json 

import pymysql.cursors

HOST = 'localhost'
USER = 'root'
PASSWORD = 'wecandowhatever'
DB = 'myproject'

#id = "6200:603:800:4177"
#title = "Acctng Decision Support System"

Id = "6200:603:800:4177"
End_Date = "01/01/2017"
Term = "Fall" 
Description = "Blah Blah accounting"
Title = "Acctng Decision Support System"
Career = "Undergraduate"
Section = "001"
Days = "M W F"
Credit = "3.0"
Start_Time = "1045"
Course = "603:800"
End_Time =  "1145"
Location = "Leigh 311"
Department = "Math"
Instructor_Email = "-"
Start_Date = "01/01/2017"
Instructor = "Joe Smith"
Instruction_Mode = "F"
Campus = "Main"

Duplicate_Id = 0
Non_Duplicate_Id = 0


Id_except = 0
End_Date_except = 0
Term_except = 0
Description_except = 0
Title_except = 0
Career_except = 0
Section_except = 0
Days_except = 0
Credit_except = 0
Start_Time_except = 0
Course_except = 0
End_Time_except = 0
Location_except = 0
Department_except = 0
Instructor_Email_except = 0
Start_Date_except = 0
Instructor_except = 0
Instruction_Mode_except = 0
Campus_except = 0

start = time.time()

try:
	connection = pymysql.connect(host=HOST,
								 user=USER,
								 password=PASSWORD,
								 db=DB,
								 charset='utf8mb4',
								 autocommit=True,
								 cursorclass=pymysql.cursors.DictCursor)
except:
	print("connection not established")
	sys.exit(1)
	
try:
	cur = connection.cursor()
except:
	print("error in con curser")
	pass

try:
	cur.execute("USE myproject")
except:
	print("error executing use myproject")
	pass
#-----------------------------------------------------------
with urllib.request.urlopen("http://www.uakron.edu/academics_majors/class-search/data/courses.json") as url:
    data = json.loads(url.read().decode('utf-8', 'ignore'))
d2 = str(data)
print('count of } ' + str(d2.count('}')))

iterator = 0

for iterator in range(0, d2.count('}') - 1):
	iterator = iterator + 1
	d3 = d2.split('{')[iterator+1].split('}')[0]
	
	try:
		Id = d3.split("'Id': '")[1].split("',")[0]
	except:
		Id = "0000:000:000:0000"
		Id_except += 1

	try:
		End_Date = d3.split("'End_Date': '")[1].split("',")[0]
	except:
		End_Date = "00/00/0000"
		End_Date_except += 1
	
	try:
		Term = d3.split("'Term': '")[1].split("',")[0] 
	except:
		Term = "UNKNOWN"
		Term_except += 1
		
	try:
		Description = d3.split("'Description': '")[1].split("',")[0]
	except:
		Description = "UNKNOWN"
		Description_except += 1

	try:
		Title = d3.split("'Title': '")[1].split("',")[0]
	except:
		Title = "UNTITLED"
		Title_except += 1

	try:
		Career = d3.split("'Career': '")[1].split("',")[0]
	except:
		Career = "UNKNOWN"
		Career_except += 1

	try:
		Section = d3.split("'Section': '")[1].split("',")[0]
	except:
		Section = "000"
		Section_except += 1

	try:
		Days = d3.split("'Days': '")[1].split("'")[0]
	except:
		Days = "M T W TH F S Su"
		Days_except += 1

	try:
		Credit = d3.split("'Credit': '")[1].split("',")[0]
	except:
		Credit = "0.0"
		Credit_except += 1

	try:
		Start_Time = d3.split("'Start_Time': '")[1].split("',")[0]
	except:
		Start_Time = "0000"
		Start_Time_except += 1

	try:
		Course = d3.split("'Course': '")[1].split("',")[0]
	except:
		Course = "0000:000"
		Course_except += 1

	try:
		End_Time = d3.split("'End_Time': '")[1].split("',")[0]
	except:
		End_Time = "0000"
		End_Time_except += 1

	try:
		Location = d3.split("'Location': '")[1].split("',")[0]
	except:
		Location = "UNKNOWN"
		Location_except += 1

	try:
		Department = d3.split("'Department': '")[1].split("',")[0]
	except:
		Department = "UNKNOWN"
		Department_except += 1

	try:
		Instructor_Email = "-"
	except:
		Instructor_Email = "-"
		Instructor_Email_except += 1

	try:
		Start_Date = d3.split("'Start_Date': '")[1].split("',")[0]
	except:
		Start_Date = "00/00/0000"
		Start_Date_except += 1

	try:
		Instructor = d3.split("'Instructor': '")[1].split("',")[0]
	except:
		Instructor = "NOT LISTED"
		Instructor_except += 1

	try:
		Instruction_Mode = d3.split("'Instruction_Mode': '")[1].split("',")[0]
	except:
		Instruction_Mode = "?"
		Instruction_Mode_except += 1

	try:
		Campus = d3.split("'Campus': '")[1].split("',")[0]
	except:
		Campus = "UNKNOWN"
		Campus_except += 1
	
#-----------------------------------------------------------
	if d2.count(Id) > 1:
		Duplicate_Id += 1
	else:
		Non_Duplicate_Id += 1
		try:
			sql = """INSERT INTO Coursestest(Id, End_Date, Term, Description, Title, Career, Section, Days, Credit, Start_Time, Course, End_Time, Location, Department, Instructor_Email, Start_Date, Instructor, Instruction_Mode, Campus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
			cur.execute(sql, (Id, End_Date, Term, Description, Title, Career, Section, Days, Credit, Start_Time, Course, End_Time, Location, Department, Instructor_Email, Start_Date, Instructor, Instruction_Mode, Campus))
		except:
			print("error adding info to database" + str(Id))
			pass

connection.close()
stop = time.time()

print("Execution time:          "+str(stop - start))
print("Duplicate_Id:            "+str(Duplicate_Id))
print("Non_Duplicate_Id:        "+str(Non_Duplicate_Id))
print("Id_except:               "+str(Id_except))
print("End_Date_except:         "+str(End_Date_except))
print("Term_except:             "+str(Term_except))
print("Description_except:      "+str(Description_except))
print("Title_except:            "+str(Title_except))
print("Career_except:           "+str(Career_except))
print("Section_except:          "+str(Section_except))
print("Days_except:             "+str(Days_except))
print("Credit_except:           "+str(Credit_except))
print("Start_Time_except:       "+str(Start_Time_except))
print("Course_except:           "+str(Course_except))
print("End_Time_except:         "+str(End_Time_except))
print("Location_except:         "+str(Location_except))
print("Department_except:       "+str(Department_except))
print("Instructor_Email_except: "+str(Instructor_Email_except))
print("Start_Date_except:       "+str(Start_Date_except))
print("Instructor_except:       "+str(Instructor_except))
print("Instruction_Mode_except: "+str(Instruction_Mode_except))
print("Campus_except:           "+str(Campus_except))
