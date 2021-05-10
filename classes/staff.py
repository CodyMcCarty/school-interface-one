# staff.py

from .person import Person

class Staff(Person):

    @classmethod
    def load_staff_from_csv(cls):
        my_file_name = "..\data\staff.csv"
        return super().load_ppl_from_csv(my_file_name)

    def __init__(self, name, age, password, role, staff_id):
        super().__init__(name, age, password, role)
        self.staff_id = staff_id

