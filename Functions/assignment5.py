"""# 5)sum of digits"""
def sumOfDigits(n):
    total = 0

    while n > 0:
        rem = n % 10
        total = total + rem
        n = n // 10

    return total

n = int(input("Enter the number: "))
print(sumOfDigits(n))