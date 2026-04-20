from studentListADT import studentListADT

class StudentList(studentListADT):
    def __init__(self):
        self._students = []

    def add_students(self,name):
        self._students.append(name)

    