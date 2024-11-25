import leaderboard as lb

# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand

# -----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name: ")

fillcolor = "pink"
size = 2
shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
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
		manage_leaderboard()
  
	else:
		counter.write("Timer: " + str(timer), font = font_setup, align = "center")
		timer -= 1
		counter.getscreen().ontimer(countdown, counter_interval)

def manage_leaderboard():

	global score
	global spot

  # get the names and scores from the leaderboard file
	leader_names_list = lb.get_names(leaderboard_file_name)
	leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
	if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
		lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
		lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

	else:
		lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
	

# -----events----------------
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
spot.onclick(spot_clicked)
wn.mainloop()
