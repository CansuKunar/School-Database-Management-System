import mysql.connector

mydb = mysql.connector.connect(
    user = 'root',
    password = '**********',
    host = 'localhost', 
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE School_Database") 

from connection import connection

connection = connection
cursor = connection.cursor()

sql = "CREATE TABLE if not exists Class(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(45),Teacherid INT NOT NULL);"
cursor.execute(sql)

sql1 = "CREATE TABLE if not exists Student(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,Studentnumber INT NOT NULL, Name VARCHAR(100) NOT NULL, Surname VARCHAR(45) NOT NULL, Birthdate DATETIME, Gender CHAR(1),classid INT NOT NULL);"
cursor.execute(sql1)

sql2 = "ALTER TABLE Student Add FOREIGN KEY(classid) REFERENCES Class(id);"
cursor.execute(sql2)

sql3 = "CREATE TABLE if not exists Teacher(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,Branch VARCHAR(45) NOT NULL, Name VARCHAR(100) NOT NULL, Surname VARCHAR(45) NOT NULL, Birthdate DATETIME , Gender CHAR(1));"
cursor.execute(sql3)

sql4 = "CREATE TABLE if not exists Lesson(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(45));"
cursor.execute(sql4)

sql5 = "CREATE TABLE if not exists Classlesson(classid INT NOT NULL, lessonid INT NOT NULL, teacherid INT NOT NULL, PRIMARY KEY(classid, lessonid, teacherid));"
cursor.execute(sql5)

sql6 = "ALTER TABLE Classlesson Add FOREIGN KEY(classid) REFERENCES Class(id);"
cursor.execute(sql6)

sql7 = "ALTER TABLE Classlesson Add FOREIGN KEY(lessonid) REFERENCES Lesson(id);"
cursor.execute(sql7)

sql8 = "ALTER TABLE Classlesson Add FOREIGN KEY(teacherid) REFERENCES Teacher(id);"
cursor.execute(sql8)

print("\tDATABASE AND TABLES ARE CREATED")
