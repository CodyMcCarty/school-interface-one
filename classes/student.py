# student.py

from .person import Person

class Student(Person):
    
    @classmethod
    def load_student_from_csv(cls):
        my_file_name = "..\data\students.csv"
        return super().load_ppl_from_csv(my_file_name)
    
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id








