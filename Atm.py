Balance=30000
Amount=int(input("Enter your money: , which you want"))
if(Balance>= Amount):
    print("withdrawal money is",Amount)
else:
    print("cancel your transcation")
remaining=Balance-Amount
print("Remaining balance is :",remaining)
