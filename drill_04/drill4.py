import turtle

count = 5
while(count >= 0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0,100*(6-count))
    turtle.pendown()
    count = count - 1

turtle.penup()
turtle.home()
turtle.left(90)
turtle.pendown()

count = 5
while(count >=0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(100*(6-count),0)
    turtle.pendown()
    count = count - 1

turtle.exitonclick()
