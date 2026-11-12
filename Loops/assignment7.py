"""Star printing in rows and columns"""
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of coloums"))
for i in range(row):
    for j in range(col):
        print("*",end=" ")
    print()