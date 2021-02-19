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
        self.name = name;
        self.gender = gender;
        self.data_sheet = data_sheet;
        self.image_url = image_url;
    
    def get_avg_grade(self):
       if self.data_sheet.get_grades_as_list():
           average_grade = sum(self.data_sheet.get_grades_as_list()) / len(self.data_sheet.get_grades_as_list())
       return average_grade;

class DataSheet():
    def __init__(self, courses):
        self.courses = courses;

    def get_grades_as_list(self):
        grades_as_list = []
        for course in self.courses:
            if course.grade is not None:
                grades_as_list.append(course.grade)
        return grades_as_list;

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=0):
        self.name = name;
        self.classroom = classroom;
        self.teacher = teacher;
        self.ETCS = ETCS;
        self.grade = grade;

    # https://www.journaldev.com/22460/python-str-repr-functions:
    # This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object.
    def __str__(self):
        # due to these, we can retriev/print our courses in the general scope.
        if self.grade > 0:
            return 'Name: ' + str(self.name) + ", Classroom: " + str(self.classroom) + ", Teacher: " + str(self.teacher) + ", ETCS: " + str(self.ETCS) + ", Grade: " + str(self.grade)
        else:
            return 'Name: ' + str(self.name) + ", Classroom: " + str(self.classroom) + ", Teacher: " + str(self.teacher) + ", ETCS: " + str(self.ETCS)

    # Python __repr__() function returns the object representation in string format. This method is called when repr() function is invoked on the object. If possible, the string returned should be a valid Python expression that can be used to reconstruct the object again.
    def __repr__(self):
        return self.__str__()

# 7.A. Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url
def writeToCSV(students):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open('python_handin_template/output.csv', 'w', newline=newline) as file_object:
        output_writer = csv.writer(file_object)
        
        for stud in students:
            for course in stud[0].data_sheet.courses:
                output_writer.writerow([
                stud[0].name, stud[0].gender, course.name, course.classroom, course.teacher,
                course.ETCS, course.grade, stud[0].image_url
                ])
    return students;


# 7. Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
def random_students(amount):
    student_list = []
    for amount_entries in range(amount):
        random_names = ['Hans', 'Ingrid', 'Carl']
        random_gender = ['Male', 'Female']
        random_grades = [0, 2, 4, 7, 10, 12]
        random_images = ['https://hatrabbits.com/wp-content/uploads/2017/01/random.jpg', 'https://www.computerhope.com/jargon/r/random-dice.jpg']
        random_courses = [
        Course('Fullstack JavaScript', '272Z', 'Lars', 100, random.choice(random_grades)), 
        Course('IT-Security', '1W', 'Daniel', 100, random.choice(random_grades)),
        Course('Python', '232D', 'Thomas', 100, random.choice(random_grades))
        ]
        
        ## this code-block prevents duplicates on the randomizing
        student_courses = []
        for r in range(random.randrange(1, len(random_courses))):
            rand_course = random.choice(random_courses)
            if rand_course not in student_courses:
                student_courses.append(rand_course)
        random_student = [Student(random.choice(random_names), random.choice(random_gender), DataSheet(student_courses), random.choice(random_images))]
        
        student_list.append(random_student)

        writeToCSV(student_list)

    # 8. Read student data into a list of Students from a csv file:
    aStudent = Student;

    with open('python_handin_template/output.csv') as f:
        students = []
        reader = csv.reader(f)
        coursesData = []
        gradeList = []
        for row in reader:
            #print(row)
            coursesData.append(Course(row[2], row[3], row[4], row[5], int(row[6]))) # maybe there's a better way to select specific rows? (eg. if the rows change in the future, it'll be horrible to correct)
            data_sheet = DataSheet(coursesData)
            aStudent = Student(row[0], row[1], data_sheet, row[7])
            students.append(aStudent)

    for student in students: # note: if a student has two courses, it will pop up twice, cause it's added like that in the CSV.
        # PROBLEM: the problem is that when retrieving like this, the get_avg_grade() will calculate for all, and .courses will show courses for all. eg:
        # 'Hans' has 2 courses, 'Carl' has 1 course. Yet, if we retrieve the element like this, 'Carl' will appear with 2 courses as well.
       print("#####", student.name, student.image_url, student.get_avg_grade(), student.data_sheet.courses)


    return student_list;

student_list = random_students(2)

# for 7, just to show that it matches the CSV file.
for stud in student_list:
    print("Name:", stud[0].name, ", Gender:", stud[0].gender, ", Courses:", stud[0].data_sheet.courses, ", Image url:", stud[0].image_url)