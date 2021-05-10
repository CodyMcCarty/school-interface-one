# student.py

from .person import Person

class Student(Person):
    
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id