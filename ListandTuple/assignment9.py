"""11)Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

expense = [2200,2350,2600,2130,2190]

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""

expense = [2000,2350,2600,2130,2190,5000]

# 1. In Feb, how many dollars you spent extra compare to January?
extraDollerSpent = expense[1]-expense[0]
print("Expence spent in feb compare to jan",extraDollerSpent)

#2.Find out your total expense in first quarter (first three months) of the year.
threeYearExpence =0
for i in range(3):
    threeYearExpence = threeYearExpence +expense[i]
print("Three years Expense are",threeYearExpence)

# 3. Find out if you spent exactly 2000 dollars in any month
for index,value in enumerate(expense):
    if value == 2000:
        print("you have spent exactly 2000 on month ",index+1)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
aprilExpenses = int(input("Enter april Month expences "))
if aprilExpenses > 0:
    expense.append(aprilExpenses)
    print("April Month Expences are added")
print(expense)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this"""
refundAmount = int(input("Enter the refund Amount "))
expense[-1] = expense[-1]-refundAmount
print(expense)
