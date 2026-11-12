num = int(input("Enter the number to find sum"))
result =0
while num>0:
    val= num % 10
    result = result+val
    num = num//10
print(result)