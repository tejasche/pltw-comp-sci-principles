#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()

apple.penup()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(pear_image)
  wn.update()

def falling():
  apple.goto(apple.xcor(), apple.ycor()-1)

#-----function calls-----
draw_apple(apple)
wn.onkeypress(falling, "a")

wn.mainloop()