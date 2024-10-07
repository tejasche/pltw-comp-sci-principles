#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []


# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  defines where the turtles will start (x and y coordinates)
startx = 0
starty = 0

# for loop to move the turtles to each new location 
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(45)     
  t.forward(50)

# moves where the turtle starts to create new places for shapes by chanign start x and y
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()