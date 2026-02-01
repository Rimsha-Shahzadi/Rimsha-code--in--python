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
# name: str = "Rimsha Shahzadi"
# print(name)
# print(type(name))
# print(id(name))
# print(dir(name))
# print([i for i in dir(name) if "__" not in i])

# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# root.geometry("500x500")
# image  =Image.open('img.jpg')
# photo = ImageTk.PhotoImage(image)
# Label(image=photo).pack()
# root.mainloop()

# from datetime import date
# def calculate_age(birth_year,birth_month,birth_day):
#     today = date.today()
#     birth_date = date(birth_year, birth_month, birth_day)
#     age_years = today.year - birth_date.year
#     age_month = today.month - birth_date.month
#     age_days = today.day - birth_date.day
#     if age_days < 0:
#         age_month -=1
#         age_days +=30
#     if age_month < 0:
#         age_years -=1
#         age_month +=12
#     return age_years, age_month, age_days
# print("____Age Calculator____")

# year = int(input("Enter your birth year (YYYY): "))
# month = int(input("Enter your birth month (MM): "))
# day = int(input("Enter your birth day (DD): "))
# year,month,day = calculate_age(year, month, day)
# print(f"\n Your age is: ")
# print(f"Your Age is {year} years, {month} months, and {day} days.")

calculator = input("Enter a number: ")
print(eval(calculator))