"""
Programa de IMC
Autor: Leonardo Miguel
Data: 07/02/2022
Descrição:
    Um programa feito para calcular pesos e averiguar se tal
    pessoa está em cima da média.
"""

"""
Declaração de variáveis;
a variável peso se encarrega do peso da pessoa.
a variável altura se encarrega da altura da pessoa.
a váriavel calculo se encarrega de calcular a fórmula IMC.
"""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
calculo = float(peso / altura ** 2)

"""
Começo da jogada de condições
Aqui será feito o processo e avaliações das pesagens.

Exemplo: 
Abaixo do peso: 18,5
Peso Normal: 18,5 a 24,9
Sobrepeso: 25 a 29,9 
Obesidade Grau 1: 30 a 34 
Obesidade Grau II: 35 a 39
Obesidade Grau III ou Morbida: maior que 40
"""

if calculo < 18.5:
    print("Você está abaixo do peso." + str(calculo))
elif calculo <= 24.9:
    print("Você está estável. " + str(calculo))
elif calculo <= 29.9:
    print("Você tem de emagrecer. " + str(calculo))
elif calculo <= 34.9:
    print("Você tem de emagrecer muito. " + str(calculo))
elif calculo <= 39.9:
    print("Você tem de emagracer bastante " + str(calculo))
else:
    print("Digite os valores certos")

# Fim do programa
