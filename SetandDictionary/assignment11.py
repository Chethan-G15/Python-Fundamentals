"""13)write a program to check if a dictionary is contained in another dictionary for ex if 

d1 = {1:11,2:12}
d2 = {1:11,2:12,3:13,4:15}
then d1 is contained in d2"""
d1 = {1: 11, 2: 12}
d2 = {1: 11, 2: 12, 3: 13, 4: 15}

flag = True

for key, value in d1.items():
    if key not in d2 or d2[key] != value:
        flag = False
        break

if flag:
    print("d1 is contained in d2")
else:
    print("d1 is not contained in d2")