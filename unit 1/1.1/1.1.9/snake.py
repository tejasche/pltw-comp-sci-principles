import math
import random
import turtle
import pillow

turtle.bgcolor("lightgreen")
turtle.title("Snake Game")
turtle.register_shape("snakeimg.gif")
turtle.register_shape("appleimg1.gif")
turtle.penup()
turtle.hideturtle()
turtle.setup(600, 600)
turtle.goto(-38, 260)

border = turtle.Turtle()
border.penup()
border.setpos(-300, -300)
border.pendown()

for i in range(4):
    border.forward(600)
    border.left(90)

apple = turtle.Turtle()
apple.color("red")
apple.shapesize(.5)
apple.penup()
apple.shape("appleimg1.gif")

snake = turtle.Turtle()
snake.penup()
snake.shape("snakeimg.gif")

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
    
def text(text):
    turtle.clear()
    turtle.write(str(text), font=("Arial", 16, "normal"))


# turtle.onkey(up, "Up")
# turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(fast, "a")
turtle.onkey(slow, "s")
turtle.listen()

speed = 1
scoren = -1

while True:
    snake.forward(speed)
    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        turtle.goto(-38, 245)
        text(f"Game Over \n  Score: {scoren}")
        break

    d = math.hypot(snake.xcor() - apple.xcor(), snake.ycor() - apple.ycor())

    if d < 50:
        apple.setpos(random.randint(-300, 300), random.randint(-300, 300))
        scoren += 1
        text(f"Score: {scoren}")


turtle.mainloop()
