#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl
import random

painter = trtl.Turtle()
painter.speed(0)
painter.penup()

# Add a loop with a zero-iteration condition
x = 1
while x == 0:
    painter.shape("circle")
    painter.stamp()

# Add an infinite loop
while x == 1:
    x1 = random.randint(-300, 300)
    y = random.randint(-300, 300)
    
    painter.color("green")
    painter.shape("square")
    painter.stamp()
    painter.goto(x1, y)


wn = trtl.Screen()
wn.mainloop()
