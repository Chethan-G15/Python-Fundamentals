totalAmount = int(input("enter total amount"))
memberShipType = input("Enter MemberShiip type (Gold/Silver/None)")

if memberShipType == "Gold":
    finalAmount = totalAmount*20/100
    payamount = totalAmount-finalAmount
elif memberShipType =="Silver":
    finalAmount = totalAmount*10/100
    payamount = totalAmount-finalAmount
else:
    finalAmount = totalAmount-200
    payamount = totalAmount-200


print("You need to pay",payamount)