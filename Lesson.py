class Lesson:

    def __init__(self, id, Name):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.Name = Name