"""Program to find Factorial"""
factNum =int(input("Enter the Number to find Factorial"))
result =1
for i in range(1,factNum+1):
    result = result*i
print(result)