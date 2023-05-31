from db_manager import DB_Manager
from Student import Student
from Teacher import Teacher
import datetime


class APP:
    def __init__(self):
        self.db = DB_Manager()

# Sınıf ekle - sil 
# Ders ekle - sil 
# Ders - sınıf için işlem
    def init_app(self):
        while True:
            print("========== MENU ==========")
            print("1. Student Transactions")
            print("2. Teacher Transactions")
            print("3. Class Transactions")
            print("4. Lesson Transactions")
            print("5. EXİT (E/e)")
            print("==========================")
            process = input("Your Choice: ")
            if process == "1":
                self.student_transactions()
            elif process == "2":
                self.teacher_transactions()
            elif process == "3":
                self.edit_student()
            elif process == "4":
                self.delete_student()
            elif process == "E" or "e":
                break
            else: 
                print("Wrong Choice.")
    
    def student_transactions(self):
        msg = "*****\n1 - Student List\n2 - Add Student\n3 - Update Student\n4 - Delete Student\n5 - Back To Menu(B/b)"
        while True:
            print(msg)
            process = input("Your Choice: ")
            if process == "1":
                self.display_students()
            elif process == "2":
                self.add_student()
            elif process == "3":
                self.edit_student()
            elif process == "4":
                self.delete_student()
            elif process == "B" or "b" or "5":
                break
            else: 
                print("Wrong Choice.")   

    def teacher_transactions(self):
        msg = "*****\n1 - Teacher List\n2 - Add Teacher\n3 - Update Teacher\n4 - Delete Teacher\n5 - Back To Menu(B/b)"
        while True:
            print(msg)
            process = input("Your Choice: ")
            if process == "1":
                self.display_teachers()
            elif process == "2":
                self.add_teacher()
            elif process == "3":
                self.edit_teacher()
            elif process == "4":
                self.delete_teacher()
            elif process == "B" or "b" or "5":
                break
            else: 
                print("Wrong Choice.") 

    def class_transactions(self):
        msg = "*****\n1 - Class List\n2 - Add Class\n3 - Update Class\n4 - Delete Class\n5 - Back To Menu(B/b)"
        while True:
            print(msg)
            process = input("Your Choice: ")
            if process == "1":
                self.display_class()
            elif process == "2":
                self.add_class()
            elif process == "3":
                self.edit_class()
            elif process == "4":
                self.delete_class()
            elif process == "B" or "b" or "5":
                break
            else: 
                print("Wrong Choice.")

    def lesson_transactions(self):
        msg = "*****\n1 - Lesson List\n2 - Add Lesson\n3 - Delete Lesson\n4 - Back To Menu(B/b)"
        while True:
            print(msg)
            process = input("Your Choice: ")
            if process == "1":
                self.display_lesson()
            elif process == "2":
                self.add_lesson()
            elif process == "3":
                self.delete_lesson()
            elif process == "B" or "b" or "4":
                break
            else: 
                print("Wrong Choice.")
  
    def display_classes(self):
        classes = self.db.get_classes()
        for c in classes:
            print(f'{c.id}: {c.Name}')

    def display_students(self):
        self.display_classes()
        classid = int(input("Which class would you like the list for?: "))

        students = self.db.get_students_by_classid(classid)
        print("Student List: ")
        for std in students:
            print(f'{std.id}-{std.Name} {std.Surname}')
        return classid

    def add_student(self):
        self.display_classes()
        classid = int(input("Which class would you like to add students to?: "))
        number = input("Student Number: ")
        name = input("Student Name: ")
        surname = input("Student Surname: ")
        year = int(input("Student Birthdate Year: "))
        month = int(input("Student Birthdate Month: "))
        day = int(input("Student Birthdate Day: "))

        birthdate = datetime.date(year, month, day)
        gender = input("Student Gender(F/M):")


        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.add_student(student)

    def edit_student(self):
        classid = self.display_students()
        studentid = int(input("Student ID: "))

        student = self.db.get_student_by_id(studentid)
        print("You can only enter the information you want to update, you can leave the ones you don't want blank.")
        student[0].Name = input("Name: ") or student[0].Name
        student[0].Surname = input("Surname: ") or student[0].Surname
        student[0].Gender = input("Gender(F/M): ") or student[0].Gender
        student[0].classid = input("Class ID: ") or student[0].classid
        year = input("Student Birthdate Year: ") or student[0].Birthdate.year
        month = input("Student Birthdate Month: ") or student[0].Birthdate.month
        day = input("Student Birthdate Day: ") or student[0].Birthdate.day

        student[0].Birthdate = datetime.date(year, month, day)
        self.db.edit_student(student[0])

    def delete_student(self):
        classid = self.display_students()
        studentid = int(input("Student ID: "))

        self.db.delete_student(studentid)

    def display_teachers(self):
        teachers = self.db.get_teachers()
        for t in teachers:
            print(f'{t.id}: {t.Name} {t.Surname} --> {t.Branch}')

    def add_teacher(self):
        branch = input("Teacher Branch: ")
        name = input("Teacher Name: ")
        surname = input("Teacher Surname: ")
        year = int(input("Teacher Birthdate Year: "))
        month = int(input("Teacher Birthdate Month: "))
        day = int(input("Teacher Birthdate Day: "))

        birthdate = datetime.date(year, month, day)
        gender = input("Teacher Gender(F/M):")


        teacher = Teacher(None, branch, name, surname, birthdate, gender)
        self.db.add_teacher(teacher)

    def edit_teacher(self):
        self.display_teachers()
        teacherid = int(input("Teacher ID: "))

        teacher = self.db.get_teacher_by_id(teacherid)
       
        print("You can only enter the information you want to update, you can leave the ones you don't want blank.")
        teacher[0].Branch = input("Branch: ") or teacher[0].Branch
        teacher[0].Name = input("Name: ") or teacher[0].Name
        teacher[0].Surname = input("Surname: ") or teacher[0].Surname
        teacher[0].Gender = input("Gender(F/M): ") or teacher[0].Gender
        year = input("Teacher Birthdate Year: ") or teacher[0].Birthdate.year
        month = input("Teacher Birthdate Month: ") or teacher[0].Birthdate.month
        day = input("Teacher Birthdate Day: ") or teacher[0].Birthdate.day

        teacher[0].Birthdate = datetime.date(year, month, day)
        self.db.edit_teacher(teacher[0])

    def delete_teacher(self):
        self.display_teachers()
        teacherid = int(input("Teacher ID: "))

        self.db.delete_teacher(teacherid)



app = APP()
app.init_app()