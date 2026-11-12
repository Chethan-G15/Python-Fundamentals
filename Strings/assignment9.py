txt = input("Enter the String ")
result =""
for i in txt:
    if i not in result:
        result+=i
print("After Removing duplicate characters are",result)