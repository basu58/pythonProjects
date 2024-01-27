import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("black")

t.pensize(5)
t.color("red")
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

t.penup()
t.goto(-90, 30)
t.pendown()
t.left(90)
t.pensize(5)
t.pencolor("white")
t.forward(270)
t.right(150)
t.forward(30)
t.backward(30)
t.right(60)
t.forward(30)

t.pensize(1)
t.penup()
t.goto(-90,30)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.forward(30)
t.right(150)
t.forward(50)
t.right(30)
t.forward(30)
t.right(120)
t.forward(30)
t.right(30)
t.forward(50)
t.right(150)
t.forward(30)
t.end_fill()

t.penup()
t.goto(-260, -120)
t.pendown()
t.write("Happy Valentines", font=("Arial", 50, "bold"))

t.penup()
t.goto(-60, -210)
t.pendown()
t.write("Day", font=("Arial", 50, "bold"))

t.hideturtle()
turtle.done()