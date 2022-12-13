import turtle


def draw_tree(branches, distance):
    if branches > 0:
        # Setting the colours of the leaves
        red = 255 // branches
        green = 100 // branches
        blue = 200 // branches

        t.pendown()
        t.color(red, green, blue)
        t.forward(distance)

        # Branches to the right
        t.right(angle)
        draw_tree(branches - 1, distance * 0.8)

        # Branches to the left
        t.left(angle * 2)
        draw_tree(branches - 1, distance * 0.8)

        # Returning to the previous colour
        t.color(red, green, blue)

        # Returning to the previous position
        t.right(angle)
        t.backward(distance)


# The angle of each branch
angle = 30

t = turtle.Turtle()
turtle.colormode(255)
t.speed("fastest")
t.penup()

# Positioning the turtle
t.seth(90)
t.goto(0, -200)

draw_tree(10, 80)

# Keeping the screen open
turtle.done()
