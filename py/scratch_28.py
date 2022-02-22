positivo = open("resultadoPositivo.txt", "r+")
negativo = open("resultadoNegativo.txt", "r+")

numeroUm = int(input("Digite um número para calcular: "))
numeroDois = int(input("Digite outro número para calcular: "))

soma = numeroUm + numeroDois
menos = numeroUm - numeroDois

if numeroUm + numeroDois:
	positivo.write(f"O resultado foi: {soma} \n")
elif numeroUm - numeroDois:
	negativo.write(f"O resultado foi: {menos}\n")

positivo.close()
negativo.close()