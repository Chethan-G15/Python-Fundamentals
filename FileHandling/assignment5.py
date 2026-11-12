import csv
marksList =[]
with open("students.csv","r") as f:
    read=csv.reader(f)
    next(read)
    print("All Student List")
    for row in read:
        name,subject,marks = row[0],row[1],int(row[2])
        print(f"{name} - {subject} - {marks}")
        # adding marks to list
        marksList.append(marks)

        #print all marks
        print(marksList)
        first = marksList[0]
        for i in marksList:
            if i > first:
                first = i
        print(name,marks)