from classes.school import School 
from classes.student import Student
from classes.staff import Staff

school = School('Ridgemont High') 
test_student = Student('Jim', 22, 'password', 'student', 789)

print(school.name)
print(test_student.name)