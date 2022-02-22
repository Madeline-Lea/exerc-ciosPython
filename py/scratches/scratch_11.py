salarioFixo = float(input("Digite o seu salário: \n " ))
numeroDeCarrVendidos = int(input("Digite o números de carro vendidos: \n"))
vlrCarrVendidos = float(input("Digite o valor de carros vendidos: \n"))

carroVendido = numeroDeCarrVendidos * 0.02 + vlrCarrVendidos * 0.5

print(f"A comissão do carro será: {carroVendido}")