import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
from Lesson import Lesson
from ClassLesson import ClassLesson

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

    def display_teachers_with_classes(self):
        sql = "SELECT teacher.id, teacher.name, teacher.surname, class.name FROM Teacher LEFT JOIN Class  ON teacher.id = class.teacherid"

        self.cursor.execute(sql)
        
        try:
            teachers = self.cursor.fetchall()
            print("Teachers with Classes:")
            for teacher in teachers:
                print(f"Teacher ID: {teacher[0]}, Name: {teacher[1]} {teacher[2]}, Class: {teacher[3]} ")
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

    def get_class_by_id(self, classid):
        sql = "SELECT * From Class WHERE id = %s"
        value = (classid, )

        self.cursor.execute(sql, value)
        try:
            cls = self.cursor.fetchone()
            return Class.create_class(cls)
        except mysql.connector.Error as err:
            print("Error:", err) 

    def add_class(self, classes: Class):
        sql = "INSERT INTO CLASS(Name, teacherid) VALUES (%s, %s)"
        values = (classes.Name, classes.Teacherid )
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Added {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def edit_class(self, classes: Class):
        sql = "UPDATE CLASS SET Name = %s, Teacherid = %s WHERE id = %s"
        values = (classes.Name, classes.Teacherid, classes.id)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Updated {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def delete_class(self, classid):
        sql = "DELETE From Class WHERE id = %s"
        values = (classid,)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Deleted {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_lesson(self):
        sql = "SELECT * From Lesson"

        self.cursor.execute(sql)
        try:
            lsn = self.cursor.fetchall()
            return Lesson.create_lesson(lsn)
        except mysql.connector.Error as err:
            print("Error:", err) 

    def add_lesson(self, lesson: Lesson):
        sql = "INSERT INTO Lesson(Name) VALUES (%s)"
        values = (lesson.Name, )
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Added {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def delete_lesson(self, lessonid):
        sql = "DELETE From Lesson WHERE id = %s"
        values = (lessonid,)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Deleted {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def classlesson(self, classid):
        sql = """
        SELECT Teacher.id, Teacher.Name, Teacher.Surname, Lesson.id, Lesson.Name
        FROM Classlesson 
        JOIN Teacher ON Classlesson.teacherid = Teacher.id
        JOIN Lesson ON Classlesson.lessonid = Lesson.id
        WHERE Classlesson.classid = %s
    """
        values = (classid,)

        self.cursor.execute(sql, values)
        try:
            lessons = self.cursor.fetchall()
            if len(lessons) > 0:
                print("Teachers in Class ID", classid, ":")
                for result in lessons:
                    teacher_id = result[0]
                    teacher_name = result[1]
                    teacher_surname = result[2]
                    lesson_id = result[3]
                    lesson_name = result[4]
                    print("Teacher ID:",teacher_id,"Teacher Name:", teacher_name,teacher_surname,"\tLesson ID:",lesson_id, "Lesson Name:", lesson_name)
            else:
                print("No teachers found for Class ID", classid)
        except mysql.connector.Error as err:
            print("Error:", err) 

    def add_classlesson(self, classlesson: ClassLesson):
        sql = "INSERT INTO Classlesson(classid, lessonid, teacherid) VALUES (%s,%s,%s)"
        values = (classlesson.classid, classlesson.lessonid,classlesson.Teacherid)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Added {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def delete_classlesson(self, classid, lessonid, teacherid):
        sql = "DELETE From Classlesson WHERE classid = %s AND lessonid = %s AND teacherid = %s"
        values = (classid, lessonid, teacherid)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'Deleted {self.cursor.rowcount} records.')
        except mysql.connector.Error as err:
            print("Error:", err)

    def __del__(self):
        self.connection.close()
        print("Database connection closed.")









