'''
the init method instantiates the object when created
selit will be called when Student is written
it passes any arguments written in.
To store it, we do "self."
'''
class Student:  #  __init__ is a special method that initilaizes or assigns values to parameters
    #  It is also known as the constructor(section of code that executes every time a new customer is created)
    def __init__(self, name, age, grade): #  name age and grade are parameters
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)









s1 = Student('Tim', 19, 95) #  tim, 19, and 95 are arguments
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)


print(course.students[0].name)


print(course.get_avg_grade())









