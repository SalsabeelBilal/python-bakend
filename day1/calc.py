print("Welcome to the tip calculater")

bill=float(input("What is your total?"))
tip_percent=float(input("How much tip you like to give?"))
people=int(input("how many to split the bill between?"))

tip_amount=(tip_percent/100)*bill
Total_bill=bill+tip_amount
eachpearson=Total_bill/ people

print(f"each should pay:{eachpearson:.2f} JD")