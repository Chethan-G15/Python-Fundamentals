txt =input("Enter the text to check Palidrome ")
rev =""
for i in txt:
    rev =i+rev
if txt == rev:
    print("Palindrom")
else:
    print("Not a Palindrome")