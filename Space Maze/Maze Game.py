import turtle as t

space = t.Screen()
space.addshape("spaceman.gif")
space.addshape("left.gif")
space.addshape("right.gif")
space.addshape("up.gif")
space.addshape("down.gif")
space.addshape("win.gif")
space.bgpic("space.gif")

rocket = t.Turtle()
rocket.shape("up.gif")
rocket.penup()
rocket.goto(180,-230)
rocket.speed(1)

spaceman = t.Turtle()
spaceman.shape("spaceman.gif")
spaceman.penup()
spaceman.goto(-100,260)

def up():
    rocket.shape("up.gif")
    rocket.setheading(90)
    
def down():
    rocket.shape("down.gif")
    rocket.setheading(270)
    
def left():
    rocket.shape("left.gif")
    rocket.setheading(180)
    
def right():
    rocket.shape("right.gif")
    rocket.setheading(0)

def move():
    rocket.forward(1)

t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(left,"Left")
t.onkeypress(right,"Right")
t.listen()

while True:
    space.update()
    if rocket.distance(spaceman) < 10:
        space.bgpic("win.gif")
        break
    else:
        move()
t.done()
