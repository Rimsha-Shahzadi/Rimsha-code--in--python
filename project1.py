menu = {
    "Pasta": 400,
    "Pizza": 800,
    "Burger": 300,
    "Salad": 100,
    "Coffee": 80
}
print("Welcome to the Pyhton Restaurant")
print("Pasta: Rs400\nPizza: Rs800\nSalad: Rs100\nBurger: Rs300\nCoffee: Rs80")

total_order = 0
item_1= input("Enter the name of item you want to order: ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    (f"Ordered {item_1} is not availble")

another_order = input("Do you want to oredr another item? Yes/No") 
if another_order == "Yes":
    item_2 = input("Enter the name of item you want to orde")
    if item_2 in menu:
       total_order += menu[item_2]
       print(f"Your item {item_2} has been added to your order")
    else:
        (f"Ordered {item_2} is not availble")
print(f"Your total order amount is: Rs{total_order}")        




