def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def average(num1, num2):
    return num1 + num2 /2

print("Please select an operation: \n " \
      "1. Addition\n " \
      "2. Subtraction\n " \
      "3. Multiply\n " \
      "4. Divide\n " \
      "5. Average\n " )

select=int(input("Select an operation(1,2,3,4,5): "))
number1 = int(input("Enter first number:"))
number2 =int(input("Enter second number:"))
if select ==1:
    print(number1, "+", number2,"=", \
        add(number1,number2))
elif select ==2:
    print(number1, "-", number2,"=", \
        sub(number1,number2))
elif select ==3:
    print(number1, "*", number2,"=", \
        multiply(number1,number2))
elif select ==4:
    print(number1, "/", number2,"=", \
        divide(number1,number2))
elif select ==5:
    print("(",number1, "+", number2, ")", "/", "2","=", \
        average(number1,number2))
else:
    print("Invalid operation please try again")    

# Practice Calculator
# def add(num1,num2):
#     return num1 + num2 
# def sub(num1,num2):
#     return num1 - num2 
# def divide(num1,num2):
#     return num1 / num2 
# def multiply(num1,num2):
#     return num1 * num2 
# def average(num1,num2):
#     return num1 + num2 / 2 
# print("Please selrct an operator: \n " \
#       "1. Addition\n " \
#       "2. Subtraction\n " \
#       "3. Multiply\n " \
#       "4. Divide\n " \
#       "5. Average\n " ) 
# select = int(input("Select an operation(1,2,3,4,5): "))
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# if select == 1:
    # print(number1, "+",number2,"=",\
        # add(number1+number2))
