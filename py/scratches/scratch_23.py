"""
Software of media calculate
Author: Leonardo Miguel
Date: 14/02/2022
Description:
    This app has the proposal to make a calculation of
a student media, and says if he's, or she's are approved.
"""


# Function

def lines():
    print("-" * 30)


def digitar_nota(indice):
    return float(input(f"Digite a primeira nota {indice}ª:"))


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f"O aluno está aprovado!  Com à média: {media}")
    else:
        print(f"O aluno está reprovado! Com à média: {media}")

print("Programa de calculo de médias")
lines()
num1 = digitar_nota(1)
lines()
num2 = digitar_nota(2)
lines()
calcular_media(num1, num2)
lines()
input("Aperte enter para fechar o programa...")
lines()