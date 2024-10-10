#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
direction = 90

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
		new_color = turtle_colors.pop()
		t.fillcolor(new_color)
		t.pencolor(new_color)
		t.penup()
		t.goto(startx, starty)
		t.pendown()
		t.setheading(direction)
		t.right(45)
		t.forward(50)

		# moves where the turtle starts to create new places for shapes by chanign start x and y
		startx = startx + 50
		starty = starty + 50

		startx = t.xcor()
		starty = t.ycor()
  
		direction = t.heading()

wn = trtl.Screen()
wn.mainloop()
