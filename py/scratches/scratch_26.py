"""import random

def lines():
print("-" * 140)

lista = []
lista2 = []
for k in range(1, 61):
lista.append(k)



#lines()

for m in range(6):
numeros_sorteados = random.choice(lista)
lista2.append(numeros_sorteados)
lista.remove(numeros_sorteados)


for c in range(len(lista2)):
for b in range(len(lista2)-1):
    if lista2[b] > lista2[b+1]:
        aux = lista2[b]
        lista2[b] = lista2[b+1]
        lista2[b+1] = aux
print(lista2)"""


"""vetor = [2,4,1,5,7,1,4]
v_rem = set(vetor)
vetor = list(v_rem)
print(vetor)
"""

dicionario = {
    "nome": "Elizabeth Madeline",
    "idade": "28",
    "genero": "Feminino",
    "classe": "Bruxa"
}

print(dicionario["nome"])
