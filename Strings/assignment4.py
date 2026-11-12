txt = input("Enter the String to Check Vowels")
count = 0
for i in txt:
    if i.lower() in "aeiou":
        count+=1
print("The Number of Vowels are",count)