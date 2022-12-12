import turtle
import math


def draw_squares(n):
    start_a = 0  # Valores iniciais de Fibonacci
    start_b = 1  # que serão guardados

    square_a = start_a
    square_b = start_b
    spiral_a = start_a
    spiral_b = start_b

    # Desenhando o primeiro quadrado
    for i in range(6):
        t.forward(square_b * scale)
        t.left(90)

    for i in range(1, n):
        # Novos valores da sequência
        square_a, square_b = square_b, square_a + square_b

        # Desenhando os próximos quadrados
        t.right(90)
        for j in range(6):
            t.forward(square_b * scale)
            t.left(90)

    # Retornando a tartaruga para a posição inicial da espiral
    t.penup()
    t.setposition(0, 0)
    t.seth(0)
    t.pendown()

    t.pencolor("red")

    t.speed(10)

    # Espiral de Fibonacci
    for i in range(n):
        fwd = math.pi * spiral_b * scale / 180
        for j in range(90):
            t.forward(fwd)
            t.left(1)
        spiral_a, spiral_b = spiral_b, spiral_a + spiral_b


scale = 4

iterations = int(input("Insira o número de iterações (maior que 1): "))
t = turtle.Turtle()
t.speed(10)
draw_squares(iterations)
turtle.done()
