import random

# declarações


nomes = []
sorteados = []

participante = ''

while participante != "f":
    participante = input("Digite o nome dos participantes: ")
    if participante != "f":
        nomes.append(participante)

print(nomes)

# sortear o participante

for i in range(4):
    nome_sorteado = random.choice(nomes)
    nomes.remove(nome_sorteado)
    sorteados.append(nome_sorteado)


print(sorteados)
