import turtle


def draw_tree(branches, distance):
    if branches > 0:
        # Definindo as cores das folhas
        red = 255 // branches
        green = 100 // branches
        blue = 200 // branches

        t.pendown()
        t.color(red, green, blue)
        t.forward(distance)

        # Ramificações à direita
        t.right(angle)
        draw_tree(branches - 1, distance * 0.8)

        # Ramificações à esquerda
        t.left(angle * 2)
        draw_tree(branches - 1, distance * 0.8)

        # Retornando para a cor inicial
        t.color(red, green, blue)

        # Retornando para a posição anterior
        t.right(angle)
        t.backward(distance)

# Ângulo de cada ramo
angle = 30

t = turtle.Turtle()
turtle.colormode(255)
t.speed("fastest")
t.penup()

# Posicionando a tartaruga
t.seth(90)
t.goto(0, -200)

draw_tree(10, 80)

# Manter a tela final
turtle.done()
