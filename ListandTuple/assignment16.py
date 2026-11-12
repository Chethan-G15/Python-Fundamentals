# 16)write a program to check if the element in the first half of the tuple are sorted in ascending order or not
t1 = (50, 20, 30, 5, 2, 8)
n = int(len(t1)/2)
isTrue = True

for i in range(n-1):
    if t1[i] > t1[i+1]:
        isTrue = False
        break
if isTrue:
    print("The First Half is sorted in ascending order")
else:
    print("The First Half is not sorted in ascending order")
