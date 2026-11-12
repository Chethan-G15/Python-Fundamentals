"""# 4)Reverse a string(no slicing)"""

def reverseString(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev

s = input("Enter a string: ")
print(reverseString(s))