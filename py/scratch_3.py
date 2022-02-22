"""
Programa - Porcentagem do Salário
Autor e Autora: Leonardo e Nathalia
Data:04/02/2022
Descrição:
Um programa feito para calcular a porcetagem de um salário.
"""

# Declarações
nome = input("Digite o nome do funcionario: ")
salarioAtual = float(input("Digite o salario atual do funcionario: "))
salarioComAumento20 = salarioAtual * 1.2
salarioComAumento10 = salarioAtual * 1.1

# A condição para fazer a porcentagem do salário
if salarioAtual <= 5000:
  print("Ira receber 20% do seu salario atual")
else:
  print("Ira receber 10% do seu salario atual")


# Fim do Programa