import turtle
bg = turtle.Screen()
bg.bgcolor("black")
turtle.pensize()
turtle.hideturtle()
turtle.penup()
turtle.goto(-165, -180)
turtle.color("white")
turtle.pendown()
turtle.forward(330)

turtle.penup()
turtle.goto(-155, -150)
turtle.color("white")
turtle.pendown()
turtle.forward(305)

turtle.penup()
turtle.goto(-145, -120)
turtle.color("pink")
turtle.pendown()
turtle.forward(280)

turtle.penup()
turtle.goto(-95, -100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(190)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(190)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

positions = [-75, -25, 25, 75]
color = ["red", "blue", "yellow","green"]
for i, pos in enumerate(positions):
    turtle.penup()
    turtle.goto(pos, 20)
    turtle.color(color[i])
    turtle.pendown()
    turtle.forward(20)

for pos in positions:
    turtle.penup()
    turtle.goto(pos, 30)
    turtle.color("red")
    turtle.pendown()
    turtle.forward(3)
turtle.penup()
turtle.goto(10, -60)
turtle.pendown()

circle_color = ["red", "blue", "yellow", "green", "brown", "blue", "purple", "grey"]
for each_color in circle_color:
    angle = 360 / len(circle_color)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)
turtle.penup()
turtle.goto(-160, 50)
turtle.color("white")
turtle.pendown()
turtle.write("HAPPY BIRTHDAY RIMSHA", font=("Poppiness", 25, "bold"))
turtle.color("lightblue")
turtle.done()

