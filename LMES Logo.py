import turtle as t

#Creating a Turtle and hiding it
pointer = t.Turtle()
pointer.hideturtle()


#Creating a Turtle and hiding it
eye = t.Turtle()
eye.hideturtle()


#Creating a Screen to Project our Tuetle objects
screen = t.Screen()
pointer.width(10)


#penup is a function in which the pointer will goto the co-ordinate points without marking line from origin line
#pendown is used to mark lines while going to next co-ordinate points
pointer.penup()
pointer.goto(-115,45)
pointer.pendown()

#selected yellow color for the Turtle variable and started filling color
pointer.fillcolor("yellow")
pointer.begin_fill()
pointer.goto(125,45)        
pointer.left(90)
pointer.forward(65)     #moving 65 pixels forward


for i in range(180):
    pointer.forward(2.1)
    pointer.left(1)     #turning left by 1 pixel
pointer.forward(65)     #end_fill is used to stop filling color
pointer.end_fill()

pointer.forward(125)
for i in range(180):    #180 to create semi-circle using for loop
    pointer.forward(2.1)
    pointer.left(1)
pointer.forward(125)

pointer.penup()
pointer.backward(125)
pointer.left(90)
pointer.forward(43)
pointer.pendown()
pointer.left(90)

for i in range(180):        #180 to create semi-circle using for loop
    pointer.forward(1.4)
    pointer.right(1)

eye.width(25)       #setting 25pixels as width of the Turtle boject Eye
eye.penup()
eye.goto(-125,45)
eye.forward(70)
eye.right(90)
eye.forward(30)
eye.pendown()

eye.forward(60)

eye.penup()
eye.left(90)
eye.forward(115)
eye.left(90)
eye.pendown()

eye.forward(60)
t.done()    #it's mandatory when we use Turtle



'''
 Hello Peeps,This Program is a basic logo creation using turtle(a python package).
 In this program,i have a created Logo for LMES Academy using all the function in Turtle package
 By Reading the Program,You can understand What's happening in this program

 Thank You
 LinkedIn - G S Dhayananth
'''
