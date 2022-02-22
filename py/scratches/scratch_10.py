num = int(input("Digite o número para verificação"))
cont = 0

for n in range(2, num):
    if num % n == 0:
        cont += 1

if cont == 2:
    print("É primo.")
else:
    print("Não é primo")

