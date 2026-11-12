"""17)Merge two dictionaries (without using update())
"""
d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}

result = {}

for key, value in d1.items():
    result[key] = value

for key, value in d2.items():
    result[key] = value

print(result)