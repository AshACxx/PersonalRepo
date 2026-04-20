import time
import numpy as np


from i_grade_list import IGradeList

class StudentGradeList(IGradeList):
    def __init__(self):
        self.__students = []

    def add_students(self, name, email, grade):

        for student in self.__students:
            if student[1] ==  email:
                return"This email already exists"
        
        self.__students.append((name, email, grade))
        return "Student added successfully."

    def size(self):
        return len(self.__students)

    def search(self, email):
        for student in self.__students:
            if student[1] == email: #student[1] stores the email address
                return student
        return None
        
    def delete_student(self,email):
        for i in range(len(self.__students)):
            if self.__students[i][1] == email:
                del self.__students[i]
                return True
        return False
    
    def highest_grade(self):
        if not self.__students:
            return []
        
        #step 1 find the highest grade
        highest_grade =  self.__students[0][2]
        for student in self.__students:
            if student[2] > highest_grade:
                highest_grade = student[2]

        #collecting all the students with highest grades
        top_students = []
        for student in self.__students:
            if student[2] == highest_grade:
                top_students.append(student)
        return top_students
    
student_list = StudentGradeList()

start = time.time()
steps_1 = student_list.add_students("Allen Lapitan", "allen.lapitan@example.com", 85)
end = time.time()
time1 = end - start

print(f"Snippet 1 time taken is {time1} seconds, steps taken are {steps_1}")