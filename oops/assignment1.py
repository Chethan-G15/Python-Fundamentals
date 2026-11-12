# Class Name: Student
# Attributes (inside constructor __init__):

# name → student’s name 

# roll_number → student’s roll number 

# math → marks in Math 

# english → marks in English 

# science → marks in Science 

# Methods:

# describe() → print the student’s name, roll number, and marks for all subjects.

# get_average() → calculate and return the average of the three subjects.

# get_grade() → assign a grade based on the average:

# = 90 → "A"

# 75–89 → "B"

# 50–74 → "C"

# < 50 → "Fail"

class Student:
    def __init__(self,name,roll_number,math,english,science):
        self.name = name
        self.roll_number = roll_number
        self.math = math
        self.english = english
        self.science = science
# describe() → print the student’s name, roll number, and marks for all subjects.
    def describe(self):
        print("The Name of the Student is",self.name)
        print("The Roll Number is", self.roll_number)
        print("Marks of Maths Subject is",self.math)
        print("Marks of English Subject is",self.english)
        print("Marks of Science Subject is",self.science)
# get_average() → calculate and return the average of the three subjects.
    def get_average(self):
        return self.math+self.english+self.science/3

# get_grade() → assign a grade based on the average:

# = 90 → "A"

# 75–89 → "B"

# 50–74 → "C"

# < 50 → "Fail"

    def  get_grade(self):
        if self.get_average == 90:
            print("A grade")
        elif self.get_average>=75 and self.get_average <=89:
            print("B grade")
        elif self.get_average >=50 and self.get_average <=74:
            print("C grade")
        else:
            print("Fail")

# Tasks for students:

# Create at least two students with different marks.

# Call describe(), get_average(), and get_grade() for each student.

# Update one subject’s marks directly for a student and print the updated details.

student1 = Student("Arun",1001,70,75,70)

student2 =Student("Bhuvan",1002,70,89,75)

student1.describe()
print("After updation of marks ")
student1.science =75
student1.describe()

student2.describe()