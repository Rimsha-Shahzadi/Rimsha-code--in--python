# Question1 
# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end=" ")
#     print() 
#  
# Question2

# r = 5
# for i in range(1, r+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()    

# Question3
# n = 5
# for i in range(n,0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()  
#   
#  # Question 4                 
# r = 6
# for i in range(1, 6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()    
 
#  # Question 5
# n = 5
# for i in range(n,0,-1):
#     for j in range(i,0, -1):
#         print(j, end=" ")
#     print() 
#    
 # Question 6
# def lines():
#     line= int(input("Enter a number of lines:"))
#     for i in range(1,line+1):
#         for j in range(i):
#             print("*", end=" ")
        # print() 
    # return f"The {line} lines of  triangle has been created"  
# triangle = lines()
# print(triangle)

#Practice Problem 1
# num = int(input("Enter a number to print a table:"))

# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")
  
def lines():
    line = int(input("Enter a number of lines:"))
    for i in range(1,line+1):
        for j in range(i):
            print("*", end = " ")
        print()
    return f"The {line} lines of triangle has beeen created"
triangle = lines()
print(triangle)