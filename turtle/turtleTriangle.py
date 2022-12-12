import turtle

t = turtle.Turtle()
t.speed(3)
t.fillcolor("yellow")


def draw_triangle(x, y):
    t.penup()

    t.goto(x, y)

    t.pendown()
    t.begin_fill()
    t.forward(120)
    t.left(120)
    t.forward(120)
    t.left(120)
    t.forward(120)
    t.left(120)
    t.end_fill()


turtle.onscreenclick(draw_triangle, 1)

turtle.listen()

turtle.done()
