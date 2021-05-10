# staff.py

from .person import Person

class Staff(Person):
    
    def __init__(self, name, age, password, role, staff_id):
        super().__init__(name, age, password, role)
        self.staff_id = staff_id