num = int(input("Enter the num value"))
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()