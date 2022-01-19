import turtle

#Programmet tegner et smilefjes ved hjelp av turtle

#Hode
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
turtle.circle(250)

#Øyne
turtle.penup()
turtle.goto(-100, 75)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(100, 75)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#Nese
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.forward(50)
turtle.goto(0, -50)
turtle.right(-180)
turtle.forward(50)
turtle.right(180)
turtle.left(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

#Munn
turtle.penup()
turtle.goto(0, -175)
turtle.left(100)
turtle.pendown()
turtle.forward(175)
turtle.left(180)
turtle.forward(175)
turtle.left(280)
turtle.forward(175)
turtle.hideturtle()

turtle.done()