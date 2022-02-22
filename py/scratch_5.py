num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 > num2:
    aux = num2
    num2 = num1
    num1 = aux

print(f" Os números pares são: \n")
for n in range(num1, num2 + 1):
    if n % 2 == 0:
        print(n)

