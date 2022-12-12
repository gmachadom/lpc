import turtle
from random import choice


def race():
    # Posicionando ambos os jogadores
    player_one.penup()
    player_two.penup()
    player_one.goto(-200, 100)
    player_two.goto(-200, -100)

    # Posicionando as linhas de chegadas
    finish_line_one.penup()
    finish_line_two.penup()
    finish_line_one.goto(200, 100)
    finish_line_two.goto(200, -100)

    rounds = 0

    while player_one.xcor() < 200 and player_two.xcor() < 200:
        player_one_dist = 200 - player_one.xcor()
        player_two_dist = 200 - player_two.xcor()

        # Decidindo o turno de cada jogador
        if rounds % 2 == 0:
            roll_die = input("Jogador Um, aperte Enter para rodar o dado")
            outcome = choice(die)
            steps = outcome * 10
            print(f"O resultado dos dados foi {outcome}\n")

            if player_one_dist < steps:
                player_one.forward(player_one_dist)
            else:
                player_one.forward(steps)

        else:
            roll_die = input("Jogador Dois, aperte Enter para rodar o dado")
            outcome = choice(die)
            steps = outcome * 10
            print(f"O resultado dos dados foi {outcome}\n")

            if player_two_dist < steps:
                player_two.forward(player_two_dist)
            else:
                player_two.forward(steps)

        rounds += 1

    if player_one.xcor() >= 200:
        print("O JOGADOR UM VENCEU!")

    elif player_two.xcor() >= 200:
        print("O JOGADOR DOIS VENCEU!")


# Criando o primeiro jogador
player_one = turtle.Turtle()
player_one.shape("turtle")
player_one.color("red")

# Criando o segundo jogador
player_two = turtle.Turtle()
player_two.shape("turtle")
player_two.color("blue")

# Criando as linhas de chegadas de cada jogador
finish_line_one = turtle.Turtle()
finish_line_one.shape("circle")
finish_line_one.color("pink")
finish_line_one.shapesize(2)
finish_line_two = turtle.Turtle()
finish_line_two.shape("circle")
finish_line_two.color("cyan")
finish_line_two.shapesize(2)

die = [1, 2, 3, 4, 5, 6]

race()
turtle.done()
