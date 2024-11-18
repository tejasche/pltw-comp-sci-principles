# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand

# -----game configuration----
fillcolor = "pink"
size = 2
shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False

# -----initialize turtle-----
spot = trtl.Turtle()
spot.shape(shape)
spot.shapesize(size)
spot.fillcolor(fillcolor)
spot.penup()

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 225)

counter = trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(0, 200)


# -----game functions--------
def spot_clicked(x, y):
	global timer_up
	if timer_up == False:
		update_score()
		change_position()
  
	else:
		spot.hideturtle()


def change_position():
	newxpos = rand.randint(-200, 200)
	newypos = rand.randint(-150, 150)
	spot.hideturtle()
	spot.goto(newxpos, newypos)
	spot.showturtle()


def update_score():
	global score
	score += 1
	score_writer.clear()
	score_writer.write(score, font = font_setup, align = "center")


def countdown():
	global timer, timer_up
	counter.clear()
	if timer <= 0:
		counter.write("Time's Up", font = font_setup, align = "center")
		timer_up = True
  
	else:
		counter.write("Timer: " + str(timer), font = font_setup, align = "center")
		timer -= 1
		counter.getscreen().ontimer(countdown, counter_interval)

# -----events----------------
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
spot.onclick(spot_clicked)
wn.mainloop()
