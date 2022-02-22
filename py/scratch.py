"""
Programa - Pesagem Ideal
Autor e Autora: Leonardo e Nathalia
Data: 04/02/2022
Descrição:
Um programa feito para calcular a altura e a pesagem assim dando o peso ideal.
"""

# Declarações

homem = input("Você é homem?")
mulher = input("Você é mulher?")
altura = float(input("Digite sua altura: "))

# Para calcular a altura do homem

if homem == 'Sim':
    calculo = (72.7 * altura) - 58
    print("Seu peso ideal é :" + str(calculo))

# Para calcular a altura da mulher

if mulher == "Sim":
    calculo = (62.1 * altura) - 44.7
    print("Seu peso ideal é: " + str(calculo))

# Fim do Programa
