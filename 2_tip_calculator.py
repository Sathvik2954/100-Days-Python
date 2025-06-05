print("Welcome to Tip Calculator !!! ")
bill=float(input("What was the total bill ? \n"))
tip=int(input("What Percentage tip would you like to give? 10 12 15 \n"))
people=int(input("How many People to split the bill? "))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_person=total_bill/people
final_amount=round(bill_person,2)
print(f"Each person should pay: Rs {final_amount}")
