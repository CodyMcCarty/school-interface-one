from classes.school import School 
from classes.student import Student
from classes.staff import Staff
import csv

school = School('Ridgemont High')
print(' ', school.name)

print("\nStudents:")
for ppl in school.students:
    print(' ', ppl)

print('\nStaff:')
for ppl in school.staff:
    print(' ', ppl)



