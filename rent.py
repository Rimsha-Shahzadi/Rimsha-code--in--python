 
# First project


rent = int(input("Enter your hostel/flat rent: "))
food = int(input("Enter amount of  food ordered: "))
electricity_spend = int(input("Enter your electricity bill: "))
charge_per_unit = int(input("Enter charge per unit"))
persons = int(input("Enter the number of persons living in room/flat"))

total_bill = electricity_spend * charge_per_unit
output = (food + rent+ total_bill) // persons
print("Each person will pay ", output)

# Srcond project

import random 
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor:")
com_choice = random.choice(item_list)
print(f"User choice = {user_choice},Computer choice = {com_choice}")

if user_choice == com_choice:
    print("Both chooses same:  Match Tie")

elif user_choice == "Rock":
    if com_choice== "Paper":
        print("Paper covers Rock: Computer wins")
    else:
        print("Rock smaeshes scissor: You wins")  
elif user_choice == "Paper":
    if com_choice== "Scissor":
        print("Scissor cuts paper: Computer wins")
    else:
        print("Ppaer covers rock: You wins")
elif user_choice == "Scissor":
    if com_choice== "Paper":
        print("Scissor covers paper: You wins")
    else:
        print("Rock smaeshes scissor: Computer wins")               

