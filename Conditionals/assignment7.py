balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient balance")

elif withdraw % 100 != 0:
    print("Enter amount in multiples of 100")

elif withdraw + 10 > balance:
    print("Insufficient balance for transaction charge")

else:
    balance = balance - withdraw - 10
    print("Withdrawal successful")
    print("Remaining balance:", balance)