"""14) Find maximum and minimum in a tuple without using built-in functions"""
t1 = (1,10,0,33,0,45,8,0)
maxval = t1[0]
minval = t1[0]
for i in t1:
    if i > maxval:
        maxval = i
for i in t1:
    if i < minval:
        minval = i
print("The Maximum number in Tuple is",maxval)
print("The Minimum number in tuple is",minval)