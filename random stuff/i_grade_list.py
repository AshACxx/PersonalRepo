class IGradeList:
    def add_students(self, name, email, grade):
        raise NotImplementedError("add_student() must be implemented")
    
    def search(self, email):
        raise NotImplementedError("search() must be implemented")
    
    def delete_students(self, email):
        raise NotImplementedError("delete_students() must be implemented")
    
    def highest_grade(self):
        raise NotImplementedError("highest_grade() must be implemented")
    
    def size(self):
        raise NotImplementedError("size() must be implemented")