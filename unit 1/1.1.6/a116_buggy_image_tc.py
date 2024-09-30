#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

# Create a spider body
body = trtl.Turtle()
body.pensize(40)
body.circle(20)

# Configure the spider legs
legsnum = 8
distance = 70
angle = 360 / legsnum
body.pensize(5)

# Draw the spider legs
iteration = 0
while (iteration < legsnum):
  body.goto(0,20)
  body.setheading(angle*iteration)
  body.forward(distance)
  iteration = iteration + 1
  
body.hideturtle()
wn = trtl.Screen()
wn.mainloop()