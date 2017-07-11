import turtle

window = turtle.Screen()

pen = turtle.Turtle()
for i in range(4):
    pen.forward(100)
    pen.right(90)

window.exitonclick()
