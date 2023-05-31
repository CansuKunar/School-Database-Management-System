class Class:

    def __init__(self, id, Name, Teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.Name = Name
        self.Teacherid = Teacherid

    @staticmethod
    def create_class(cls):
        list = []

        if isinstance(cls, tuple):
            list.append(Class(cls[0], cls[1], cls[2]))
        else:
            for i in cls:
                list.append(Class(i[0], i[1], i[2]))

        return list