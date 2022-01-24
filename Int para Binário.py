ciclo = 1
# Criar um ciclo infinito até ser digitado 0 ou qualquer letra do teclado
while ciclo == 1:
    num = int(input('Diga um número inteiro para passarmos para binário:  '))
    if num == 0: quit()
    else:
        binary = ''
        while num != 0:
            # Resto do número atual a dividir por 2.
            # Como o número é sempre dividido por 2 só devolve 0 ou 1
            remainder = num % 2

            # A lista guarda o valor
            binary += str(remainder)

            # O número é dividido por 2 até ser igual a 0
            num = int(num/ 2)
        # Revertemos a Lista para nos devolver o número correto
        valorFinal = binary[::-1]
        print("O número em binário é: " + (str(valorFinal)))
        print()

    print("Vamos converter outro número..")
    print("Para sair escreva 0")

# Exemplo: 10
# 10 % 2 = 0 , 10 / 2 = 5
# 5 % 2 = 1 , 5 / 2 = 2
# 2 % 2 = 0 , 2 / 2 = 1
# 1 % 2 = 1 , 1/2 = 0
# Binary = "0101"
# Se revertermos [-1] , Binary: "1010"
