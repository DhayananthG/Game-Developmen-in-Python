import turtle as t

ground = t.Screen()
ground.bgpic("ground.png")
ground.register_shape("right.gif")
ground.register_shape("left.gif")
ground.register_shape("ball.gif")

Right_Player = t.Turtle()
Right_Player.shape("right.gif")
Right_Player.penup()
Right_Player.goto(400,-200)

Left_Player = t.Turtle()
Left_Player.shape("left.gif")
Left_Player.penup()
Left_Player.goto(-400,200)


score_board_R= t.Turtle()
score_board_R.penup()
score_board_R.goto(-330,300)
score_board_R.hideturtle()

score_board_L = t.Turtle()
score_board_L.penup()
score_board_L.goto(190,300)
score_board_L.hideturtle()


ball = t.Turtle()
ball.shape("ball.gif")
ball.penup()
ball.speed(1.5)

def left_up():
    y = Left_Player.ycor()
    Left_Player.sety(y+15)

def left_down():
    y = Left_Player.ycor()
    Left_Player.sety(y-15)
    
def left_Player_Right():
    x = Left_Player.xcor()
    Left_Player.setx(x+15)

def left_Player_Left():
    x = Left_Player.xcor()
    Left_Player.setx(x-15)

def right_up():
    y = Right_Player.ycor()
    Right_Player.sety(y+15)

def right_down():
    y = Right_Player.ycor()
    Right_Player.sety(y-15)

def right_Player_Right():
    x = Right_Player.xcor()
    Right_Player.setx(x+15)

def right_Player_Left():
    x = Right_Player.xcor()
    Right_Player.setx(x-15)
    

t.onkeypress(left_up,"w")
t.onkeypress(left_down,"s")
t.onkeypress(left_Player_Right,"d")
t.onkeypress(left_Player_Left,"a")

t.onkeypress(right_up,"Up")
t.onkeypress(right_down,"Down")
t.onkeypress(right_Player_Right,"Right")
t.onkeypress(right_Player_Left,"Left")
t.listen()


dx =5
dy =-5
Right_Score = 0
Left_Score = 0
while True:
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x+dx,y+dy)
    
    if Right_Player.distance(ball) < 20:
        dx = -dx
        Right_Score = Right_Score + 5
        score_board_R.clear()
        score_board_R.write("Right Score : {}".format(Right_Score),font=('Helvetica',15,'bold'))
    if Left_Player.distance(ball) < 20:
        dx = -dx
        Left_Score = Left_Score + 5
        score_board_L.clear()
        score_board_L.write("Left Score : {}".format(Left_Score),font=('Helvetica',15,'bold'))

    if ball.ycor() < -280:
        dy = -dy
    if ball.ycor() > 280:
        dy = -dy
    if ball.xcor() < -470:
        dx = -dx
    if ball.xcor() > 470:
        dx = -dx
t.done()
