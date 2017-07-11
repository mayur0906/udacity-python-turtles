import turtle

window = turtle.Screen()

def draw_pattern(pen3):
    pen3.color("blue")
    pen3.speed(16)

    pen3.left(35)
    pen3.forward(50)
    pen3.right(35)
    pen3.forward(50)
    pen3.right(145)
    pen3.forward(50)
    pen3.right(35)
    pen3.forward(50)
    pen3.right(10)

pen = turtle.Turtle()

for i in range(39):
    draw_pattern(pen)
    # pen.left(10)
pen.home()
pen.right(90)
pen.forward(200)

window.exitonclick()
