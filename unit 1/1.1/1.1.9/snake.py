import math
import random
import turtle

turtle.bgcolor("gray")
snake = turtle.Turtle()
master2 = turtle.Turtle()
snakeimg = "snakeimg.gif"
turtle.register_shape(snakeimg)

master2.penup()
master2.setpos(-300, -300)
master2.pendown()
snake.penup()

for i in range(4):
    master2.forward(600)
    master2.left(90)

apple = turtle.Turtle()
apple.color("red")
apple.shapesize(3)
apple.penup()
apple.shape("circle")


def up():
    snake.forward(20)


def down():
    snake.backward(20)


def right():
    snake.right(20)


def left():
    snake.left(20)


def fast():
    global speed
    speed += 1


def slow():
    global speed
    speed -= 1


# turtle.onkey(up, "Up")
# turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(fast, "a")
turtle.onkey(slow, "s")

snake.color("yellow")
snake.shapesize(3)
snake.shape("snakeimg.gif")

turtle.listen()

speed = 1

while True:
    snake.forward(speed)
    if snake.xcor() > 300 or snake.xcor() < -300:
        snake.right(30)

    if snake.ycor() > 300 or snake.ycor() < -300:
        snake.left(30)

    d = math.hypot(snake.xcor() - apple.xcor(), snake.ycor() - apple.ycor())

    if d < 50:
        apple.setpos(random.randint(-300, 300), random.randint(-300, 300))


turtle.mainloop()
