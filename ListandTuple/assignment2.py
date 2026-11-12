""" adding marks to list using loop 2"""
marks =[]
for i in range(1,7):
    print("Enter student",i,"Marks")
    mark =int(input("Enter marks"))
    marks.append(mark)
    marks.sort()
print(marks)