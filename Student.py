class Student:

    def __init__(self, id, Studentnumber, Name, Surname,Birthdate,Gender, classid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.Studentnumber = Studentnumber
        if len(Name) > 45:
            raise Exception("The name can only have a total of 45 characters.")
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Gender = Gender
        self.classid = classid


    @staticmethod
    def create_student(std):
        list = []

        if isinstance(std, tuple):
            list.append(Student(std[0], std[1], std[2], std[3], std[4], std[5], std[6]))

        else:
            for i in std:
                list.append(Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return list

