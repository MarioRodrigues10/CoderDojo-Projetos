def novo_jogo():
    respostas = []
    respostas_corretas = 0
    numero_questao = 1

    for key in questoes:
        print("-------------------------------")
        print(key)
        for i in opcoes[numero_questao-1]:
            print(i)
        resposta = input("Coloque (A,B,C,D): ")
        resposta = resposta.upper()  
        respostas.append(resposta) 

        respostas_corretas += verificarResposta(questoes.get(key), resposta)
        numero_questao += 1

    mostrarScore(respostas_corretas, respostas)

def verificarResposta(respostaC, tentativa):
    if respostaC == tentativa:
        print("-------------------------------")
        print("Resposta Certa!")
        return 1
    else:
        return 0

def mostrarScore(respostasC, tentativas):
    print("-------------------------------")
    print("Resultados:")
    print("-------------------------------")

    print("Respostas: ", end="")
    for i in questoes:
        print(questoes.get(i), end=" ")
    print()
    
    print("Tentativas: ", end="")
    for i in tentativas:
        print(i, end=" ")
    print()

    score = int((respostasC / len(questoes))*100)
    print("Pontuação final:" + str(score))
def jogarNovamente():
    perguntaFinal = input("Quer Jogar Novamente (S/N):")
    perguntaFinal = perguntaFinal.upper()
        
    if perguntaFinal == "S":
        return True
    else:
        return False
    


questoes={"Quantos anos faz o CoderDojo?": "B",
           "O que ensinamos no CoderDojo?": "C",
           "Quem é o melhor mentor do CoderDojo?": "D",
           "Quantos cinturões existem no Coderdojo?": "A"
        }
 
opcoes=[["A. 8", "B. 9", "C. 10", "D. 11"],
        ["A. Coisas da Vida", "B. Biologia", "C. Programação", "D. Coisas Ilegais"],
        ["A. Mike", "B. Vitor", "C. Rui", "D. Mário"],
        ["A. 8", "B. 9", "C. 6", "D. 7"]]

novo_jogo()

while jogarNovamente():
    novo_jogo()

print ("Adeus!")