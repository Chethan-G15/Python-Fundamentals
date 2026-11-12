"""#6)for the dictionary below

# students = {'anand':85,'deepak':80,'dhanush':88}

# #add new student

# #change existing students marks

# #print individual students 

# #loop over each student and print their names along with marks

"""
students = {'anand':85,'deepak':80,'dhanush':88}

# #add new student
students.update({'kiran':90})
print(students)

# #change existing students marks
students['deepak'] =85
print(students)

# #print individual students 
for name in students.keys():
    print(name)

# #loop over each student and print their names along with marks
for name,marks in students.items():
    print("Name of student is",name,"Marks of Student is",marks)