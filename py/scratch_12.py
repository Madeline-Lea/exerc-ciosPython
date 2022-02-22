nomeVendedor = input("Digite o nome do vendedor: ")
salarioFixo = float(input("Digite o salário do vendedor: R$ "))
vendasDiversas = float(input("Digite o valor de vendas R$ "))
qntCarros = int(input("Digite o valor de carros: "))

for i in range(1, qntCarros + 1, 1 ):
    valorCarros = float(input("Digite o valor do carro: R$"))

comissao = (qntCarros * 0.02 + vendasDiversas * 0.05)

print(f"O salário total do vendedor {comissao} é: {comissao + salarioFixo}")
