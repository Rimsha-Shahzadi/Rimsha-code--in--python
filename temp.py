# temp = float(input("Enter the temperature: "))
# if temp <=36:
#     print("Cold temperature:  ")
# elif temp <=37.5:
#     print("Normal temperature: ") 
# elif temp > 37.5:
#     print("Hot temmperature: ")
# else:
#     print("Invsalid input try again: ")

star = 3
for i in range(1,star+1):
    print("* " * i)
calculator = input("Enter a number:")
print(eval(calculator))

table = input("Enter a number to print a table:  ")
for i in range(1,11):
    print(f"{table} * {i} = {table*i}")