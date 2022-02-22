# Declarações
nome = input("Digite o nome do funcionario: ")
salarioAtual = float(input("Digite o salario atual do funcionario: "))


# A condição para fazer a porcentagem do salário
if salarioAtual <= 5000:
  print("Ira receber 20% do seu salario atual")
else:
  print("Ira receber 10% do seu salario atual")

# Demonstração de ambos do salários em 10% e 20%
print("Nome do funcionario: " + nome )
print("Salario atual do funcionario: " + str (salarioAtual))

print("Salario com aumento de 20% : ")
print(float(salarioAtual * 1.2))

print("salario com aumento de 10% : ")
print(float(salarioAtual * 1.1))


# Fim do Programa