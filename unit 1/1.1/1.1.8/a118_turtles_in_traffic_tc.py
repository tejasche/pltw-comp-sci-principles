#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    # horizontal adding turtle to the list and assigning color and location
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)
    # horizontal adding turtle to the list and assigning color and location
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)

    tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
hvel = 3
vvel = 3
shorter = True

for step in range(50):
    for h in horiz_turtles:
        for v in vert_turtles:
            h.forward(hvel)
            v.forward(vvel)
            
            if hvel <= 5:
                shorter = True
            
            if hvel <= 10 and shorter:
                hvel += 1
                vvel += 1
                
            if hvel > 10:
                hvel -= 1
                vvel -= 1
                shorter = False
                
            if abs(h.xcor() - v.xcor()) < 20:
                newshape = turtle_shapes.pop()
                h.fillcolor("red")
                h.shape(newshape)
                horiz_turtles.remove(h)
                
            if abs(h.ycor() - v.ycor()) < 20:
                newshape = turtle_shapes.pop()
                v.fillcolor("gray")
                v.shape(newshape)
                vert_turtles.remove(v)
                
            if h.xcor() >= 350:
                horiz_turtles.remove(h)
                
            if v.ycor() >= 350:
                vert_turtles.remove(v)

wn = trtl.Screen()
wn.mainloop()