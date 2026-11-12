"""16)Invert a dictionary (swap keys and values)

i/p: d = {"a": 1, "b": 2, "c": 3}

o/p : Inverted: {1: 'a', 2: 'b', 3: 'c'}"""

ordinalDictionary = {"a": 1, "b": 2, "c": 3}
newDictionary = {}
for key,val in ordinalDictionary.items():
    newDictionary[val] = key
print(newDictionary)