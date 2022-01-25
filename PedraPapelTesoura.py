import random
ciclo = 1
while ciclo == 1:
    jogador = input("Escolha (pedra, papel, tesoura): ")
    acoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(acoes)
    print ("Você escolheu: " + jogador)
    print ("Computador escolheu: " + computador)

    if jogador == computador:
        print("Empate!")
    elif jogador == "pedra":
        if computador == "tesoura":
            print("Pedra esmaga a Tesoura! Ganhaste!")
        else:
            print("Papel cobre a Pedra! Perdeste!")
    elif jogador == "papel":
        if computador == "pedra":
            print("Papel cobre a Pedra! Ganhaste!")
        else:
            print("Tesoura corta o Papel! Perdeste!")
    elif jogador == "tesoura":
        if computador == "papel":
            print("Tesoura corta o Papel! Ganhaste!")
        else:
            print("Pedra esmaga a Tesoura! Perdeste!")

    print()
    jogarDnv = input("Jogar outra vez? (s/n): ")
    if jogarDnv.lower() != "s":
        break