""" Remove all duplicate from the list and create another list"""
fruits = ["apple","banana","orange","kiwi","cherry","apple","banana"]
list2 =[]
for i in fruits:
    if i not in list2:
        list2.append(i)
print(list2)

