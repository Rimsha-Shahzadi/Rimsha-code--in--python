foods = []
prices = []
total = 0
while True:
    food = input("Enter food to buy : ")
    if food.lower() == 'q':
       break
    else:
      price = float(input(f"Enter price for {food}: "))
      foods.append(food)
      prices.append(price)
    #   total += price
price("----YOUR CART----")
print("\nYour foods")
for food in foods:
   print(f"{food}, \t", end=" ")
print()  
for price in prices:
   total += price
print(f" Your total is {total}") 
 