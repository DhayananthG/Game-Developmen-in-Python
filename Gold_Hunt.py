import turtle as t
import random as r

sea = t.Screen()
#before using any gif,we should add those gid's to screen it's mandatory
sea.register_shape("left.gif")
sea.register_shape("right.gif")
sea.register_shape("coin.gif")
sea.bgpic("background.gif")

hunter = t.Turtle()
hunter.shape("left.gif")
hunter.penup()
hunter.goto(0,-120)

#the coin turtle should be defined after hunter,the only the coin will not fall behind left.gif and right.gif
coin = t.Turtle()
coin.shape("coin.gif")
coin.speed(50)
coin.penup()
coin.goto(-200,200)

score_board = t.Turtle()
score_board.penup()
score_board.goto(-40,240)
score_board.hideturtle()

def right():
    hunter.shape("right.gif")
    hunter.forward(8)

def left():
    hunter.shape("left.gif")
    hunter.backward(8)

#these functions should be written before the While Condition,then only keys will work
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
t.listen()

def move():
    y = coin.ycor()
    coin.sety(y-1)

score = 0 
while True:
    sea.update()
    move()
    if coin.ycor() < -300:
        x = r.randint(-280,280)
        coin.goto(x,280)
    if hunter.distance(coin) < 50:
        score = score + 5
        score_board.clear()
        score_board.write("Score : {}".format(score),font=('Helvetica',15,'bold'))
        x = r.randint(-280,280)
        coin.goto(x,280)
        
t.done()
