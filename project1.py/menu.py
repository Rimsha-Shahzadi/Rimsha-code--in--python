menu = {
    'Pizza': 250,
    'Pasta': 200,
    'Salad': 150,
    'Burger': 300,
    'Coffe': 80,
}
print("Welcome to Pyhton Restaurant")
print("Pizza: Rs250\nPasta: Rs200\nSalad: Rs150\nBurger: Rs300\nCoffe: Rs80")

total_order = 0
item_1 = input("Enter the name of itam which you want to oredr: ")
if item_1 in menu:
    total_order += menu[item_1] 
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet")

another_order =  input("Do you want to order another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of itam which you want to oredr: ")
    if item_2 in menu:
        total_order += menu[item_2] 
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available yet")
print(f"Your total order amount is: Rs{total_order}")        
   

