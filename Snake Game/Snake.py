import turtle as t
import random as r

ground = t.Screen()
ground.bgpic("ground.gif")
ground.register_shape("left.gif")
ground.register_shape("right.gif")
ground.register_shape("up.gif")
ground.register_shape("down.gif")
ground.register_shape("body.gif")

snake = t.Turtle()
snake.penup()
snake.goto(0,0)
snake.shape("right.gif")
snake.speed(1)

food = t.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.goto(50,50)
food.speed(500)

score_board = t.Turtle()
score_board.penup()
score_board.goto(-40,230)
score_board.hideturtle()

def up():
    if snake.heading() != 270:
        snake.shape("up.gif")
        snake.setheading(90)
    
def down():
    if snake.heading() != 90:
        snake.shape("down.gif")
        snake.setheading(270)
    
def left():
    if snake.heading() != 180:
        snake.shape("left.gif")
        snake.setheading(180)
    
def right():
    if snake.heading() != 0:
        snake.shape("right.gif")
        snake.setheading(0)

def move():
    snake.forward(10)

t.onkeypress(left,"Left")
t.onkeypress(right,"Right")
t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.listen()

Score = 0
Body = []
while True:
    ground.update()

    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        ground.bgpic("game_over.gif")
        food.hideturtle()
        score_board.clear()
        score_board.write("Score : {}".format(Score),font=('Helvetica',15,'bold'))
        break
    
    for i in Body:
        if i.distance(snake) < 10:
            ground.bgpic("game_over.gif")
            food.hideturtle()
            break
        
    if snake.distance(food) < 10:
        Score = Score + 5
        score_board.clear()
        score_board.write("Score : {}".format(Score),font=('Helvetica',15,'bold'))
        x = r.randint(-285,285)
        y = r.randint(-285,285)
        food.setpos(x,y)
        
        body = t.Turtle()
        body.penup()
        body.speed(500)
        body.shape("body.gif")
        Body.append(body)
        
    for i in range(len(Body)-1,0,-1):
        x = Body[i-1].xcor()
        y = Body[i-1].ycor()
        Body[i].goto(x,y)
        
    if len(Body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        Body[0].goto(x,y)
    move()

t.done()
