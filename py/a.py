"""
Programa de Criação de Tabuada
Autor: Leonardo Miguel
Data 07/02/2022
Descrição:
Um programa feito para calcular uma tabuada, mas com o while.
"""

"""
Declarações e uso do programa

A variável valor é o display para o usuário digitar um número desejado
assim exibindo o resultado.
A variável aux tem a definição de ser o auxiliar na hora de fazer o 
nosso looping introduzindo elas ao lado da variável valor x "aux" = valor 
no caso nosso incrementador.
 Assim com o meu spoiler o loop é o nosso while que tem a condição de 
"""
valor = int(input('Entre com um número para saber a tabuada: '))
aux = 0
print('Tabuada de {}'.format(valor))
while aux <= 10:
    print('{} X {} = {}'.format(aux, valor, (aux * valor)))
    aux = aux + 1

# Fim do programa
