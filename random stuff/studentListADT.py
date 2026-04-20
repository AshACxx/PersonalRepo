class StudentListADT:
    def add_students(self, name):
        raise NotImplementedError("add_student() must be implemented")
    
    def get_students(self):
        raise NotImplementedError("get_studentss() must be implemented")
    
    def update_students(self, old_name, new_name):
        raise NotImplementedError("update_students() must be implemented")
    
    def remove_students(self, name):
        raise NotImplementedError("remove_students() must be implemented")
    