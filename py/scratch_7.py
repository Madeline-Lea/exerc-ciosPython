
"""
Programa para média ponderada
Autor: Leonardo Miguel
Data: 09/02/2022
Descrição:
Programa feito para calcular a média ponderada de um
aluno. 
"""
"""
Declarações e Uso do Programa:
/////////////////////////////////////////////////////////////////
Às variaveis nota... e peso... servem para que o usuário insira 
às notas dos alunos, e essas notas serão avaliadas 
pelo o peso que ira multiplicar pelo o tanto de notas e depois 
uma soma ocorrerá com os pesos e logo uma divisão será
efeituada assim dando a média ao usuário.			 
/////////////////////////////////////////////////////////////////
"""
notaUm = float(input("Insira à primeira nota: "))
pesoUm = 1

notaDois = float(input("Insira à segunda nota: "))
pesoDois = 2

notaTres = float(input("Insira à terceira nota: "))
pesoTres = 3

notaQuatro = float(input("Insira à quarta nota: "))
pesoQuatro = 4

alunoMedia = (notaUm * pesoUm + notaDois * pesoDois + notaTres * pesoTres + notaQuatro * pesoQuatro) / (pesoUm + pesoDois + pesoTres + pesoQuatro)

print(f"A média do aluno é: {alunoMedia}")

# Fim do programa