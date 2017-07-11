import turtle

window = turtle.Screen()
window.bgcolor("blue")

def draw_square():
    pen = turtle.Turtle()
    pen.shape("triangle")
    pen.color("red")
    pen.speed(1)

    for i in range(4):
        pen.forward(100)
        pen.right(90)

def draw_circle():
    pen2 = turtle.Turtle()
    pen2.circle(100)

draw_square()
draw_circle()

window.exitonclick()
