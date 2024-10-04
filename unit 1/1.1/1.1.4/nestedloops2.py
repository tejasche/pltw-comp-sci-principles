import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1

while True:
	move_x = 1
	while x <= 100 and move_x == 1:
		while y < 100:
			x = x + move_x
			y = y + move_y
			painter.goto(x, y)
		move_y = -1

		while y > 0:
			x = x + move_x
			y = y + move_y
			painter.goto(x, y)
		move_y = 1

	move_x = -1

	while move_x == -1:
		move_y = -1
		while y <= 0 and y > -100:
			print("1")
			x = x + move_x
			y = y + move_y
			painter.goto(x, y)
 
		while y < 0:
			move_y = 1
			print("2")
			x = x + move_x
			y = y + move_y
			painter.goto(x, y)

		while x == -200 and y == 0:
			move_x = 1
			break
   
wn = trtl.Screen()
wn.mainloop()