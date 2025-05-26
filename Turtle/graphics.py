# from turtle import*
# import colorsys
# speed(0)
# hideturtle()
# bgcolor('black')
# tracer(5)
# width(2)
# h = 0.001
# for i in range(90):
#   color(colorsys.hsv_to_rgb(h,1,1))
#   forward(100)
#   left(240)
#   forward(100)
#   right(120)
#   circle(50)
#   left(60)
#   forward(100)
#   h += 0.02
#   color(colorsys.hsv_to_rgb(h,1,1))
#   forward(100)
#   right(60)
#   forward(100)
#   left(120)
#   circle(-50)
#   forward(100)
#   right(60)
#   forward(100)
#   left(2)
#   h += 0.02
# done()

# Python program to draw star
# using Turtle Programming


# import turtle
# star = turtle.Turtle()

# star.right(75)
# star.forward(100)

# for i in range(4):
#     star.right(144)
#     star.forward(100)
    
# turtle.done()

# Python program to draw 
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.speed(1000)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)