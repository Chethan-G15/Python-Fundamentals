marks1 = int(input("Enter marks one "))
marks2 =int(input("Enter marks two"))
marks3 = int(input("Enter marks three"))
avg = (marks1+marks2+marks3)/3
if avg>=40 and marks1>= 33 and marks2>=33 and marks3>=33:
    print("Student is passed")
else:
    print("Student is Fail")
print("The Average marks of Student is",avg)