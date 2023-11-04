# PROJECT 2
# Tip CALCULATOR

print("Welcome to Tip Calculator")
bill = float(input("Enter total bill: "))
tip = int(input("Enter the tip from 10, 15, 20:" ))
people = int(input("Enter no. of people:" ))
tip_in_percent = tip/100
total_tip = bill * tip_in_percent
total_bill = bill + tip_in_percent
bill_per_person = total_bill/people
print(f"Each person has to pay Rupees {bill_per_person}")

