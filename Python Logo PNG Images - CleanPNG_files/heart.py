# import turtle
# import math

# t = turtle.Turtle()
# t.speed(0)
# t.color("red")
# turtle.bgcolor("black")

# def corazon(n):
#     x = 16 * math.sin(n) ** 3
#     y = 13 * math.cos(n) -5 * \
#         math.cos(2 * n) -2*math.cos(3 * n) - \
#         math.cos(4 * n)
#     return x, y
# t.penup()
# for i in range(15):
#     t.goto(0 ,0)
#     t.pendown()
#     for n in range(0 ,100, 2):
#         x, y = corazon(n/10)
#         t.goto(x*i, y*i)
#     t.penup()
# t.hideturtle()
# turtle.done()    

# SECOND HEART
# import math
# from turtle import *

# def hearta(k):
#     return 15*math.sin(k)**3

# def heartb(k):
#     return 12*math.cos(k)-5*\
#     math.cos(2*k)-2*\
#     math.cos(3*k)-\
#     math.cos(4*k)

# speed(9000)
# bgcolor("black")

# for i in range(6000):
#     goto(hearta(i)*20, heartb(i)*20)
#     for j in range(5):
#         color("red")
#         goto(0,0)
# done()       

# Animation Haert

# .heart {
#     fill: red;
#     position: relative; top: 5px; width: 50px;
#     animation: pulse 1s ease infinite;
# }

# #heart {
# position: relative; width: 100px; height: 900px;
# text-align: center; font-size: 16px;
# }
# @keyframes pulse {
#     0% {transform: scale(1);}
#     50% {transform: scale(1.3);}
#     100% {transform: scale(1);}
# }

#heart {



