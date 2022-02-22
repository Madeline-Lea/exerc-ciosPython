def somar(num1, num2):
	resultado = num1 + num2
	return resultado

def digitar(numero):
	res = input(f"Digite o {numero}º número: ")
	return res

num1 = int(digitar(1))
num2 = int(digitar(2))

resultado = somar(num1, num2)



print(resultado)
