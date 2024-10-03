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
angle = 180 / legsnum
body.pensize(5)

# Draw the spider legs

leg = 0
while (leg < legsnum):
	body.goto(0,20)
	if leg < 4:
		body.setheading(angle*leg - 35)
		body.forward(distance)
	
	else:
		body.setheading(angle*leg + 55)
		body.forward(distance)
	leg = leg + 1
	
body.goto(-13, 10)
body.shape("circle")
body.pensize(6)
body.color("red")
body.stamp()
body.penup()
body.goto(13, 10)
body.pendown()
body.stamp()
 
body.hideturtle()
wn = trtl.Screen()
wn.mainloop()