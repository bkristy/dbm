import time
import sys, datetime, os, inspect
import urllib.request, json 
with urllib.request.urlopen("http://www.uakron.edu/academics_majors/class-search/data/courses.json") as url:
    data = json.loads(url.read().decode('utf-8', 'ignore'))
    ##print(data)  ## data came in okay.
	
##--------------------------------------------------------------------
def console_logger():
    log_name = ('Log.{:%Y-%m-%d.%H.%M.%S}'.format(datetime.datetime.now()) + '.txt')
    class Logger(object):
        def __init__(self):
            self.terminal = sys.stdout
            self.log = open("logs/"+log_name, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass

    sys.stdout = Logger()
    print("console log started, " + log_name) 
##--------------------------------------------------------------------
console_logger()

d2 = str(data)
print('count of } ' + str(d2.count('}')))


iterator = 0

duplicate_ids = 0

Id_except = 0
End_Date_except = 0
Term_except = 0
description_except = 0
Title_except = 0
Section_except = 0
days_except = 0
End_Time_except = 0
location_except = 0
Department_except = 0
instructor_email_except = 0
start_date_except = 0
instructor_except = 0
instruction_mode_except = 0
campus_except = 0

for iterator in range(0, d2.count('}')):

	d3 = d2.split('{')[iterator+1].split('}')[0]
	#print(d3)

	
	try:
		id = d3.split("'Id': '")[1].split("',")[0]
	except:
		id = ""
		Id_except += 1
		pass
	
	
		
	try:
		end_date = d3.split("'End_Date': '")[1].split("',")[0]
	except:
		end_date = ""
		End_Date_except += 1
		pass
	
	try:
		term = d3.split("'Term': '")[1].split("',")[0]
	except:
		term = ""
		Term_except += 1
		pass
	
	try:
		description = d3.split("'Description': '")[1].split("',")[0]
	except:
		description = ""
		description_except += 1
		pass
		
	try:
		title = d3.split("'Title': '")[1].split("',")[0]
	except:
		title = ""
		Title_except += 1
		pass
		
	try:
		section = d3.split("'Section': '")[1].split("',")[0]
	except:
		section = ""
		Section_except += 1
		pass
		
	try:
		days = d3.split("'Days': '")[1].split("',")[0]
	except:
		days = ""
		days_except += 1
		pass
	
	try:
		end_time = d3.split("'End_Time': '")[1].split("',")[0]
	except:
		end_time = ""
		End_Time_except += 1
		pass
	
	try:
		location = d3.split("'Location': '")[1].split("',")[0]
	except:
		location = ""
		location_except += 1
		pass
	
	try:
		department = d3.split("'Department': '")[1].split("',")[0]
	except:
		department  = ""
		Department_except += 1
		pass
		
	try:
		instructor_email = d3.split("'Instructor_Email': '")[1].split("',")[0]
	except:
		instructor_email = ""
		instructor_email_except += 1
		pass
	
	try:
		start_date  = d3.split("'Start_Date': '")[1].split("',")[0]
	except:
		start_date = ""
		start_date_except += 1
		pass
	
	try:
		instructor  = d3.split("'Instructor': '")[1].split("',")[0]
	except:
		instructor  = ""
		instructor_except += 1
		pass
	
	try:
		instruction_mode  = d3.split("'Instruction_Mode': '")[1].split("',")[0]
	except:
		instruction_mode = ""
		instruction_mode_except += 1
		pass
	
	try:
		campus  = d3.split("'Campus': '")[1].split("',")[0]
	except:
		campus = ""
		campus_except += 1
		pass
	
	iterator += 1
	
	if d2.count(id) > 1:
		#print(str(id))
		duplicate_ids += 1
	
		print("-----------------------------------------------")
		print("Id:               " + id)
		print("End Date:         " + end_date)
		print("Term:             " + term)
		print("description:      " + description)
		print("Title:            " + title)
		print("Section:          " + section)
		print("days:             " + days)
		print("End Time:         " + end_time)
		print("location:         " + location)
		print("Department:       " + department)
		print("instructor email: " + instructor_email)
		print("start date:       " + start_date)
		print("instructor        " + instructor)
		print("instruction mode: " + instruction_mode)
		print("campus:           " + campus)
	
	

print("Id_except:               " + str(Id_except))
print("End_Date_except:         " + str(End_Date_except))
print("Term_except:             " + str(Term_except))
print("description_except:      " + str(description_except))
print("Title_except:            " + str(Title_except))
print("Section_except:          " + str(Section_except))
print("days_except:             " + str(days_except))
print("End_Time_except:         " + str(End_Time_except))
print("location_except:         " + str(location_except))
print("Department_except:       " + str(Department_except))
print("instructor_email_except: " + str(instructor_email_except))
print("start_date_except:       " + str(start_date_except))
print("instructor_except:       " + str(instructor_except))
print("instruction_mode_except: " + str(instruction_mode_except))
print("campus_except:           " + str(campus_except))
print("duplicate ids:           " + str(duplicate_ids))


# d3 = d2.split('{')[2].split('}')[0]
# #print(d3)

# id = d3.split("'Id': '")[1].split("',")[0]
# end_date = d3.split("'End_Date': '")[1].split("',")[0]
# term = d3.split("'Term': '")[1].split("',")[0]
# description = d3.split("'Description': '")[1].split("',")[0]
# title = d3.split("'Title': '")[1].split("',")[0]
# section = d3.split("'Section': '")[1].split("',")[0]
# days = d3.split("'Days': '")[1].split("',")[0]
# end_time = d3.split("'End_Time': '")[1].split("',")[0]
# location = d3.split("'Location': '")[1].split("',")[0]
# department = d3.split("'Department': '")[1].split("',")[0]
# instructor_email = d3.split("'Instructor_Email': '")[1].split("',")[0]
# start_date  = d3.split("'Start_Date': '")[1].split("',")[0]
# instructor  = d3.split("'Instructor': '")[1].split("',")[0]
# instruction_mode  = d3.split("'Instruction_Mode': '")[1].split("',")[0]
# campus  = d3.split("'Campus': '")[1].split("',")[0]
# print("-----------------------------------------------")
# print("Id:               " + id)
# print("End Date:         " + end_date)
# print("Term:             " + term)
# print("description:      " + description)
# print("Title:            " + title)
# print("Section:          " + section)
# print("days:             " + days)
# print("End Time:         " + end_time)
# print("location:         " + location)
# print("Department:       " + department)
# print("instructor email: " + instructor_email)
# print("start date:       " + start_date)
# print("instructor        " + instructor)
# print("instruction mode: " + instruction_mode)
# print("campus:           " + campus)


