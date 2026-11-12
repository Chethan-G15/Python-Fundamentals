num = int(input("Enter the number to check palidrome"))
orginal = num
rev = 0
while num>0:
    val = num%10
    rev = rev*10+val
    num = num//10
if orginal == rev:
    print("Palindrome")
else:
    print("not a Palindrome")