from turtle import *
from colorsys import *
speed(0)

# calculator = input("Enter number: ")
# print(eval(calculator))
# star = 3
# for i in range(1,star+1):
#     print(" *" * i)
# for i in range(star-1,0,-1):
#     print(" *" * i)
calculator = input("Enter a number: ")
print(eval(calculator))
star = 3
for i in range(1, star+1):
    print(" *" * i)
for i in range(star-1,0 ,-1):
    print(" *" * i)
calender = input("Enter a year:")
print(eval(calender))

for i in range(1,11):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}',end='\t')
