import time


from student__grade_list import StudentGradeList

grade_list = StudentGradeList()
print(grade_list.add_students("John Mcarthy", "john@example.com", 85))
print(grade_list.add_students("Allen Lapitan", "allen.lapitan@example.com", 90))
print(grade_list.add_students("Allen Lapitan", "allen.lapitan@example.com", 90))
print(grade_list.add_students("Ash Chera", "ash.chera@example.com", 95))
print(grade_list.add_students("Tyler Brady", "tyler.brady@example.com", 88))
print(grade_list.add_students("Olu Ad", "olu.ad@example.com", 82))
print("\n")
student = grade_list.search('allen.lapitan@example.com')

print(student)  # Output: ('John Mcarthy', 'john@example.com', 85)
print("\n")

delete_email = 'john@example.com'
is_deleted = grade_list.delete_student(delete_email)
print(f"{delete_email} was deleted: {is_deleted}")  # Output:\


highest_grade = grade_list.highest_grade()
print(highest_grade)


print("Size:", grade_list.size())
