from turtle import *
from colorsys import *
speed(0)
bgcolor('black')
pensize(2)
h = 0
penup()
goto(0, 0)
pendown()
for i in range(36):
    color(hsv_to_rgb(h, 1, 1))
    h = (h + 0.028) % 1
    penup()
    forward(150)
    pendown()
    begin_fill()
    for _  in range(5):
        forward(50)
        right(144)
    end_fill()
    penup()
    goto(0, 0)
    right(10) 
done()   
