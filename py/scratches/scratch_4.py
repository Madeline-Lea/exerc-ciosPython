"""
Declarações e uso do programa

A variável valor tem o input que o usuário irá digitar
A variav
"""
"""
Programa de Cálculo de média 
Autor: Leonardo Miguel 
Data: 08/02/2022
Descrição:
    Esse programa tem à função de fazer um calculo de média
    após o usuário teclar um número negativo.
"""



valor = float(input("Digite um número: "))
soma = 0

contagem = 0

while valor > 0:

    valor = float(input("Digite o próximo valor: "))
    soma = (valor + soma)
    contagem = contagem + 1

    if valor <= 0:
        input("O número inserido foi negativo, ou seja o programa será encerrado, aperte qualquer tecla.")
        media = soma / contagem
        print("A média dos números teclados: " + str(media))

