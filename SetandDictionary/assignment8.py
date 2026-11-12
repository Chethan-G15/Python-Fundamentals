"""11)Count frequency of each element in a tuple using dictionary"""
t1 = (10, 20, 10, 30, 20, 10, 40, 30)
frequency ={}
for i in set(t1):
    valCount = t1.count(i)
    frequency.update({i:valCount})
print(frequency)