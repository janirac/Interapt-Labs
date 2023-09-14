import random

student_str = "Erin Ashley Janira Shaq Seiku Nate Leo Val Debbie Laura Jordan"
students = student_str.split()
print(students)

while len(students) != 0:
    user_input = input('Hit <enter> to select a new student: ')
    if user_input == '':
        random.shuffle(students)
        print(f'Selected student: {students.pop()}')
       
print('All Students have been called!')