"""#10)Remove duplicates from a list (without set)"""
def removeDuplicates(num):
    result = []

    for i in num:
        if i not in result:
            result.append(i)

    return result

num = [1, 2, 3, 2, 4, 1, 5]

print(removeDuplicates(num))