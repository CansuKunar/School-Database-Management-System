import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DB_Manager:

    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def get_student_by_id(self, id):
        sql = "SELECT * From Student WHERE id = %s"
        value = (id,)

        self.cursor.execute(sql, value)
        try:
            std = self.cursor.fetchone()
            return Student.create_student(std)
        except mysql.connector.Error as err:
            print("Error:", err)     

    def get_students_by_classid(self, classid):
        sql = "SELECT * From Student WHERE classid = %s"
        value = (classid,)

        self.cursor.execute(sql, value)
        try:
            std = self.cursor.fetchall()
            return Student.create_student(std)
        except mysql.connector.Error as err:
            print("Error:", err) 
    
    def add_student(self, student: Student):
        sql = "INSERT INTO Student(Studentnumber, Name, Surname,Birthdate,Gender,Classid) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (student.Studentnumber, student.Name, student.Surname, student.Birthdate, student.Gender, student.classid)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Added {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def edit_student(self, student: Student):
        sql = "UPDATE STUDENT SET studentnumber = %s, Name = %s , Surname = %s,Birthdate = %s,Gender = %s, Classid = %s WHERE id = %s"
        values = (student.Studentnumber, student.Name, student.Surname, student.Birthdate, student.Gender, student.classid, student.id)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Updated {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def delete_student(self, studentid):
        sql = "DELETE From Student WHERE id = %s"
        values = (studentid,)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Deleted {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_teachers(self):
        sql = "SELECT * From Teacher"

        self.cursor.execute(sql)
        try:
            tch = self.cursor.fetchall()
            return Teacher.create_teacher(tch)
        except mysql.connector.Error as err:
            print("Error:", err) 

    def get_teacher_by_id(self,id):
        sql = "SELECT * From Teacher WHERE id = %s"
        value = (id,)

        self.cursor.execute(sql, value)
        try:
            tch = self.cursor.fetchone()
            return Teacher.create_teacher(tch)
        except mysql.connector.Error as err:
            print("Error:", err) 

    def add_teacher(self, teacher: Teacher):
        sql = "INSERT INTO TEACHER(Branch, Name, Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = (teacher.Branch, teacher.Name, teacher.Surname, teacher.Birthdate, teacher.Gender)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Added {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)
 
    def edit_teacher(self, teacher: Teacher):
        sql = "UPDATE TEACHER SET Branch = %s, Name = %s , Surname = %s,Birthdate = %s,Gender = %s WHERE id = %s"
        values = (teacher.Branch, teacher.Name, teacher.Surname, teacher.Birthdate, teacher.Gender, teacher.id)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Updated {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def delete_teacher(self, teacherid):
        sql = "DELETE From Teacher WHERE id = %s"
        values = (teacherid,)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Deleted {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_classes(self):
        sql = "SELECT * From Class"

        self.cursor.execute(sql)
        try:
            cls = self.cursor.fetchall()
            return Class.create_class(cls)
        except mysql.connector.Error as err:
            print("Error:", err) 

    def add_class(self, classes: Class):
        pass
    def get_lesson():
        pass



    def __del__(self):
        self.connection.close()
        print("Database connection closed.")

# db = DB_Manager()
# student = db.get_student_by_id(7)
# student[0].Name = "Jake"
# # student = Student(None, 402, 'Victoria', 'Anderson', '2002-10-17', 'F', 4)

# # db.add_student(student)
# db.edit_student(student[0])
# student = db.get_student_by_id(1)

# print(student.Name)

# student = db.get_students_by_classid(1)
# print(student[3].Name)