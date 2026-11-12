"""19)write a program to convert a number entered by the user into its corresponding number in words use dictionary

i/p: 878
o/p: eight seven eigth"""

numbers ={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
txt =""
n = int(input("Enter the Number"))
while n>0:
    val = n%10
    txt=numbers[val]+" "+txt
    n =n//10
print(txt)