#!/usr/bin/python3




# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
import random
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
wn.setup(width=0.9, height=0.8)

canvas_width = turtle.window_width()
canvas_height = turtle.window_height()

print("Canvas Width:", canvas_width)
print("Canvas Height:", canvas_height)

skk = turtle.Turtle()
x = random.randint(-(canvas_width/2), (canvas_width/2))
y = random.randint(-(canvas_height/2), (canvas_height/2))
print(x,y)
skk.penup()
skk.goto(x,y)
skk.width(10)
skk.pendown()

for i in range(4):
    skk.forward(100)
    skk.right(90)
skk.hideturtle()   
turtle.done()