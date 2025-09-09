rent = int(input("Enter your hostel/flat rent: "))
food = int(input("Enter amoount of  food ordered: "))
electricity_spend = int(input("Enter your electricity bill: "))
charge_per_unit = int(input("Enter charge per unit"))
persons = int(input("Enter the number of persons living in room/flat"))

total_bill = electricity_spend * charge_per_unit
output = (food + rent+ total_bill) // persons
print("Each person will pay ", output)