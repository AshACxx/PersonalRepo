class Student:
    def __init__(self, fname, lname, age, student_id):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.student_id = student_id

    def greet(self):
        print(f"Hello my name is {self.fname} {self.lname} and i am {self.age} years old and my student number is {self.student_id}")


s1 = Student (
    fname = "Ash",
    lname = "Chera",
    age = "20",
    student_id = "C24385641"
)

s2 = Student (
    fname = "Allen",
    lname = "Lapitan",
    age = "18",
    student_id = "C24288561"
)

s1.greet()
s2.greet()
