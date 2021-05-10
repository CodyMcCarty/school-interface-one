# school.py
from .student import Student
from .staff import Staff


class School:

    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_staff_from_csv()
        self.students = Student.load_student_from_csv()

    # def __str__(self):
    #     for peer in self.students:
    #         print (peer)
