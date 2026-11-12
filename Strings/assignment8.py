txt=input("Enter the text ")
uppercount = 0
lowecount = 0
specialcount =0
for i in txt:
    if i in "ABCDEFGHITKLMMOPQRSTUVWXYZ":
        uppercount+=1
    elif i in "abcdefghijklmnopqrstuvwxyz":
        lowecount+=1
    else:
        specialcount+=1
print("Number of upper case in a String",uppercount)
print("Number of Lower case in a String",lowecount)
print("Number of special charcter in a String",specialcount)

