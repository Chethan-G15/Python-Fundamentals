"""15)Group strings by their starting letter

Input: ["apple", "ant", "ball", "bat", "cat"]

o/p:
{
 'a': ['apple', 'ant'],
 'b': ['ball', 'bat'],
 'c': ['cat']
}"""
words = ["apple", "ant", "ball", "bat", "cat"]

result = {}

for i in words:
    key = i[0]

    if key in result:
        result[key].append(i)
    else:
        result[key] = [i]

print(result)