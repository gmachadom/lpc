import turtle
import math


def draw_squares(n):
    start_a = 0  # Starting values on
    start_b = 1  # the Fibonacci sequence

    square_a = start_a
    square_b = start_b
    spiral_a = start_a
    spiral_b = start_b

    # Drawing the first square
    for i in range(6):
        t.forward(square_b * scale)
        t.left(90)

    for i in range(1, n):
        # Next numbers on the sequence
        square_a, square_b = square_b, square_a + square_b

        # Drawing the following squares
        t.right(90)
        for j in range(6):
            t.forward(square_b * scale)
            t.left(90)

    # Returning the turtle to the starting point for the spiral
    t.penup()
    t.setposition(0, 0)
    t.seth(0)
    t.pendown()

    t.pencolor("red")

    t.speed(10)

    # Fibonacci spiral
    for i in range(n):
        fwd = math.pi * spiral_b * scale / 180
        for j in range(90):
            t.forward(fwd)
            t.left(1)
        spiral_a, spiral_b = spiral_b, spiral_a + spiral_b


scale = 4

iterations = int(input("Enter the number of iterations (greater than 1): "))
t = turtle.Turtle()
t.speed(10)
draw_squares(iterations)
turtle.done()
