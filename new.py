# from turtle import *
# from colorsys import *
# speed(0)

# calculator = input("Enter number: ")
# print(eval(calculator))
# star = 3
# for i in range(1,star+1):
#     print(" *" * i)
# for i in range(star-1,0,-1):
#     print(" *" * i)
# calculator = input("Enter a number: ")
# print(eval(calculator))
# star = 3
# for i in range(1, star+1):
#     print(" *" * i)
# for i in range(star-1,0 ,-1):
#     print(" *" * i)
# import calender 
# print(calender.calender(2026))

# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} * {j} = {i*j}',end='\t')


# from turtle import *
# from datetime import datetime
# bgcolor("white")
# hideturtle()
# penup()

# today = datetime.now().strftime("%Y-%m-%d")
# goto(0, 0)
# write(f"Today's Date: {today}",
#         align="center",
#         font=("Arial", 18, "bold"))

# done()

# import calender
# print(calender.calendar(2026))


# import calendar
# print(calendar.calendar(2026))
# calculator = input("Enetr a number: ")
# print(eval(calculator))
name: str = "Rimsha Shahzadi"
print(name)
print(type(name))
print(id(name))
print(dir(name))
print([i for i in dir(name) if "__" not in i])
