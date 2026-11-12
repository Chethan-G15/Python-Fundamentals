"""#11)armstrong number

153 = 1+125+27 = 153"""

def armstrong(n):
    temp = n
    total = 0
    power = len(str(n))

    while n > 0:
        rem = n % 10
        total = total + rem ** power
        n = n // 10

    if total == temp:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"


num = int(input("Enter a number: "))
print(armstrong(num))