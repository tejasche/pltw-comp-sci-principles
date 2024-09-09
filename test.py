import turtle
import random

shape = input("What shape would you like to draw? ").lower()
color = input("What color would you like the shapes to be? ").lower()
quantity = int(input("How many shapes would you like to draw? "))

t = turtle.Turtle()

t.shape(shape)
t.color(color)

for i in range(quantity):  
    distance = random.randint(50, 100)
    angle = random.randint(50, 150)
    
    t.pendown()
    t.stamp()
    t.penup()
    t.forward(distance)
    t.right(angle)
    
w = turtle.Screen()
w.mainloop()