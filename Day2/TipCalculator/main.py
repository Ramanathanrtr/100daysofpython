print("Welcome to the Tip Calculator!")
totalBill = input("What was the total bill?")
tips = input("How much tip would you like to give 10, 12 or 15?")
shareWith = input("How many people to share the bill?")

billStr = totalBill.split("$")[1]
totalBill = float(billStr) + int(tips)
print(totalBill)
print(totalBill/int(shareWith))