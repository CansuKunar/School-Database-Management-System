class Teacher:

    def __init__(self, id, Branch, Name, Surname,Birthdate,Gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.Branch = Branch
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Gender = Gender

    @staticmethod
    def create_teacher(tch):
        list = []

        if isinstance(tch, tuple):
            list.append(Teacher(tch[0], tch[1], tch[2], tch[3], tch[4], tch[5]))

        else:
            for i in tch:
                list.append(Teacher(i[0], i[1], i[2], i[3], i[4], i[5]))

        return list
