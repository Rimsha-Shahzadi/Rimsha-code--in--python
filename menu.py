# menu = {
#     'Pizza': 250,
#     'Pasta': 200,
#     'Salad': 150,
#     'Burger': 300,
#     'Coffe': 80,
# }
# print("Welcome to Pyhton Restaurant")
# print("Pizza: Rs250\nPasta: Rs200\nSalad: Rs150\nBurger: Rs300\nCoffe: Rs80")

# total_order = 0
# item_1 = input("Enter the name of itam which you want to oredr: ")
# if item_1 in menu:
#     total_order += menu[item_1] 
#     print(f"Your item {item_1} has been added to your order.")
# else:
#     print(f"Ordered item {item_1} is not available yet")

# another_order =  input("Do you want to order another item? (Yes/No)")
# if another_order == "Yes":
#     item_2 = input("Enter the name of itam which you want to oredr: ")
#     if item_2 in menu:
#         total_order += menu[item_2] 
#         print(f"Your item {item_2} has been added to your order.")
#     else:
#         print(f"Ordered item {item_2} is not available yet")
# print(f"Your total order amount is: Rs{total_order}")        


# Step-1 Create functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def avg(num1, num2):
    return (num1 + num2) / 2

# Step-2 User input
print("Please select a operation: \n " \
      "1. Addition\n " \
      "2. Subtraction\n " \
      "3. Multiply\n " \
      "4. Divide\n " \
      "5. Average\n ")

select = int(input("Select operation (1,2,3,4,5): "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Step-3 Print The Result
if select == 1:
    print(f"Sum of two numbers are: ", \
           add(number1, number2))


