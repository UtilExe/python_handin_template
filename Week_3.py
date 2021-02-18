### Ex 1 Classes
# 1. Create 3 classes: Student, DataSheet and Course
# 2. A student has a data_sheet and a data_sheet has multiple courses in particular order
# 3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
# 4. In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
# 5. In DataSheet create a method to get_grades_as_list()
# 6. In student create a method: get_avg_grade()
# 7. Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
#    A. Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url
# 8. Read student data into a list of Students from a csv file:
#    A. loop through the list and print each student with name, img_url and avg_grade.
#    B. sort the list by avg_grade
#    C. create a bar chart with student_name on x and avg_grade on y-axis
# 9. Make a method on Student class that can show progression of the study in % (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))
# 10. Show a bar chart of distribution of study progression on x-axis and number of students in each category on y-axis. (e.g. make 10 categories from 0-100%)
# Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next course in the list
import random;
import csv;
import platform;

class Student(): 
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
       if self.data_sheet.get_grades_as_list():
           average_grade = sum(self.data_sheet.get_grades_as_list()) / len(self.data_sheet.get_grades_as_list())
       return average_grade;

class DataSheet():
    def __init__(self, courses):
        self.courses = courses
    
    def get_grades_as_list(self):
        grades_as_list = []
        for course in self.courses:
            if course.grade is not None:
                grades_as_list.append(course.grade)
        return grades_as_list;

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

#Genders
genders = ['male', 'female']
#Courses goes here
grades = [-3, 0, 2, 4, 7, 10, 12]
math = Course('Mathemathics', 'Classroom-A1', 'Mr. Peterson', 30, grades)
music = Course('Music', 'Classroom-A2', 'Mrs. Barnes', 10, grades)
english = Course('English', 'Classroom-A3', 'Mr. Davis', 30, grades)
economics = Course('Economics', 'Classroom-A4', 'Ms. Hinton', 20, grades)
courses = [math, music, english, economics]

names = [
    'Henry',
    'Mads',
    'Odalf',
    'Frederik',
    'Christian',
    'Jacob'
]


# 7. Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
def create_students(amount):
    # issue atm: sometimes the same course name and data gets added twice.
    students = []
    for i in range(amount):
        students_courses = []
        for r in range(random.randrange(1, len(courses))):
            students_courses.append(random.choice(courses))
        
        for course in students_courses:
            course.grade = random.choice(grades)
        
        data_sheet = DataSheet(students_courses)

        name = random.choice(names)
        gender = random.choice(genders)
        image_url = 'https://google.com'
        student = Student(name, gender, data_sheet, image_url)
        students.append(student)
    
    # A. Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open('python_handin_template/output.csv', 'w') as file_object:
        for stud in students:
            for course in students_courses:
            # is there a better way to retrieve data, than cherry picking the attributes 1 by 1? __dict__ seems to be an option.
            #                     stud_name,        course_name,        teacher,               ETCS,                    classroom,               grade,                    img_url
                file_object.write(str(stud.name + "," + course.name + "," + course.teacher + "," + str(course.ETCS) + "," + course.classroom + "," + str(course.grade) + "," + stud.image_url) + '\n')

    return students;
    
students = create_students(2)

for student in students:
    for course in student.data_sheet.courses:
        print("Student:", student.name, ", Course:", course.name, ", Grade:", course.grade)
    print("The Average grade:", student.get_avg_grade())
    #print("List of grades: ", student.data_sheet.get_grades_as_list())