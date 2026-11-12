"""# 2)factorial of a number"""

n = int(input("Enter the number "))

def facto(n):
    fact =1
    for i in range(1,n+1):
        fact = i*fact
    return fact

print(facto(n))