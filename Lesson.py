class Lesson:

    def __init__(self, id, Name):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.Name = Name

    @staticmethod
    def create_lesson(lsn):
        list = []

        if isinstance(lsn, tuple):
            list.append(Lesson(lsn[0], lsn[1]))
        else:
            for i in lsn:
                list.append(Lesson(i[0], i[1]))

        return list