a = float(input("Digite o número do primeiro lado: "))
b = float(input("Digite o número do segundo lado: "))
c = float(input("Digite o número do terceiro lado: "))

if a < b + c and a < c + b and b < c + a:
    print("É possível formar um triangulo.")
else:
    print("É impossível fazer um triângulo")

"""
for i in range(10):
    if i == 5 or i == 8
        print(i)

    if i == 8:
        print(i)
        break
"""