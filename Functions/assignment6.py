"""# 6)write a program to calculate sum of even numbers in a list """
def sumOfEven(num):
    total = 0

    for i in num:
        if i % 2 == 0:
            total = total + i

    return total

num = [1, 2, 3, 4, 5, 6, 7, 8]

print(sumOfEven(num))