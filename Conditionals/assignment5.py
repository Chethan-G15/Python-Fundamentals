val1=int(input("Enter val one"))
val2=int(input("Enter val two"))
val3= int(input("Enter val three"))
if val1>val2 and val1>val3:
    print(val1,"is greatest of all three")
elif val2>val1 and val2>val3:
    print(val2,"is greatest of all three")
else:
    print(val3,"is greatest of all three")