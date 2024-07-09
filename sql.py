import sqlite3

##connect to sqlite
connection = sqlite3.connect("student.tb")

##create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

##create table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);


"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('krisha Murari','Data analytics','A',90)''')
cursor.execute('''Insert Into STUDENT values('Rishikesh','Data Science','B',99)''')
cursor.execute('''Insert Into STUDENT values('Manibhushan','Machine learning','A',86)''')
cursor.execute('''Insert Into STUDENT values('Prateek giri goshwami','DEVOPS','A',80)''')
cursor.execute('''Insert Into STUDENT values('Vikash Tailor','Machine learning','A',85)''')
cursor.execute('''Insert Into STUDENT values('Akash Kumar','Data Science','A',96)''')
cursor.execute('''Insert Into STUDENT values('Pradyumna','Machine learning','B',98)''')
cursor.execute('''Insert Into STUDENT values('Riya singh','Data analytics','A',97)''')
cursor.execute('''Insert Into STUDENT values('Navya','DEVOPS','A',97)''')
cursor.execute('''Insert Into STUDENT values('Ummeda Ram','Cyber security','A',94)''')
cursor.execute('''Insert Into STUDENT values('Dumpa Dasu','Data analytics','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sashi pratap singh shekhawat','Data Science','B',96)''')
cursor.execute('''Insert Into STUDENT values('Yuvraj Harishchandra','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Kunal','Cyber security','A',93)''')
cursor.execute('''Insert Into STUDENT values('Subhash bairwa','Machine learning','A',81)''')
cursor.execute('''Insert Into STUDENT values('krishna kumar','Data Science','A',87)''')
cursor.execute('''Insert Into STUDENT values('Supriy','Data Science','B',80)''')
cursor.execute('''Insert Into STUDENT values('shrustidhar','Machine learning','A',84)''')
cursor.execute('''Insert Into STUDENT values('sanjeev','DEVOPS','A',90)''')
cursor.execute('''Insert Into STUDENT values('Guru prakash','Cyber security','A',95)''')
cursor.execute('''Insert Into STUDENT values('Saurabh Ranjan','DEVOPS','A',90)''')
cursor.execute('''Insert Into STUDENT values('Amit vyam','Data analytics','A',85)''')
## Display all the records
print("The inserted records are")

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close()    