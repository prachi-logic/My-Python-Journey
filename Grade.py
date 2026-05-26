#make grade calculator
Java=int(input("Enter your marks java:"))
DBMS=int(input("Enter your marks DBMS:"))
Statistics=int(input("Enter your marks Statistics:"))
Math=int(input("Enter your marks Math:"))
English=int(input("Enter your marks English:"))
sum=(Java+DBMS+Statistics+Math+English)
percentage=(sum/500*100)
if(percentage>=90):
    print("Your Grade is A+")
elif(percentage>=80):
    print("Your Grade is A")
elif(percentage>=70):
    print("Your Grade is B")
elif(percentage>60):
    print("Your Grade is C")
elif(percentage>50):
    print("Your Grade is D")
else:
    print("You are fail")
print("Best of luck for your future")
