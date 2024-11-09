import math #math library
import random #random number
import turtle
from PIL import Image, ImageOps #image library

# set up the screen
turtle.bgcolor("lightgreen")
turtle.title("Snake Game")
turtle.penup()
turtle.hideturtle()
turtle.setup(600, 600)
turtle.goto(0, 275)

# setup images
turtle.register_shape("snakeimg.gif")
turtle.register_shape("appleimg.gif")
snakeimg = Image.open("snakeimg.gif")
appleimg = Image.open("appleimg.gif")
snakeimg = ImageOps.expand(snakeimg, border = 100, fill = (255, 255, 255, 0)) #increase the size of the image without changing the snake

degree = 0

# setup the border
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.setpos(-290, -290)
border.pensize(20)
border.pencolor("red")
border.pendown()

#create the border
for i in range(4):
	border.forward(580)
	border.left(90)

#create apple and snake objects
apple = turtle.Turtle()
apple.color("red")
apple.shapesize(0.5)
apple.penup()
apple.shape("appleimg.gif")

snake = turtle.Turtle()
snake.penup()
snake.shape("snakeimg.gif")

#give the snake movement functionality
def up():
	snake.forward(20)

def down():
	snake.backward(20)

def right():
	global degree
	degree -= 20
	snake.setheading(degree)
	rotatedsnake = snakeimg.rotate(degree)
	rotatedsnake.save("rotatedsnake.gif")
	turtle.register_shape("rotatedsnake.gif")
	snake.shape("rotatedsnake.gif")

def left():
	global degree
	degree += 20
	snake.setheading(degree)
	rotatedsnake = snakeimg.rotate(degree)
	rotatedsnake.save("rotatedsnake.gif") #save the rotated image for later use
	turtle.register_shape("rotatedsnake.gif")
	snake.shape("rotatedsnake.gif")

def fast():
	global speed
	speed += 1

def slow():
	global speed
	speed -= 1

#function to easily display text
def text(text):
	turtle.clear()
	turtle.write(str(text), font = ("Roboto", 16), align = "center")

#set the difficulty identified by the user
difficulty = turtle.textinput("Difficulty", "Enter difficulty level (easy, medium or hard): ")
correct = True
while correct:
	if difficulty == "easy":
		speed = 1
		correct = False

	elif difficulty == "medium":
		speed = 2
		correct = False

	elif difficulty == "hard":
		speed = 3
		correct = False

	else:
		difficulty = turtle.textinput("Difficulty", "Enter a correct value (easy, medium or hard): ")

#check for user input and bind functoins to the input keys
# turtle.onkey(up, "Up")
# turtle.onkey(down, "Down")
turtle.onkey(fast, "a")
turtle.onkey(slow, "s")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.listen()
 
scoren = -1  

running = True
while running:
	snake.forward(speed)
	#check for collision with the border and end game if so
	if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
		turtle.goto(0, 252)
		text(f"\nGame Over\n  Score: {scoren}") #display game over and score
		running = False

	#check for collision with the apple and increase score
	if math.hypot(snake.xcor() - apple.xcor(), snake.ycor() - apple.ycor()) < 50:
		apple.setpos(random.randint(-275, 275), random.randint(-275, 275))
		scoren += 1
		text(f"Score: {scoren}")

turtle.mainloop()