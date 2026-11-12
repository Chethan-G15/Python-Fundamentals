"""14)write a program to find highest 2 values in a dictionary"""
d1 = {
    "apple": 100,
    "banana": 250,
    "orange": 150,
    "mango": 300,
    "grapes": 200
}

values = sorted(d1.values(), reverse=True)

print("Highest value:", values[0])
print("Second highest value:", values[1])