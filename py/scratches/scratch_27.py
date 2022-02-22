

funcionarios = [
     {
        "nome": "Larissa Silva",
        "cargo": "Dev. Pleno",
        "idade": 22,
        "projetos": ["Projeto Docs", "Projeto Dev"],
        "bloqueado": False
    },
    {
        "nome": "Joao Silva",
        "cargo": "Dev. Jr",
        "idade": 18,
        "projetos": ["Projeto Docs", "Projeto Query"],
        "bloqueado": False
    },
    {
        "nome": "Henrique Silvano",
        "cargo": "Dev. Senior",
        "idade": 25,
        "projetos": ["Projeto Query", "Projeto Prata"],
        "bloqueado": True
    },
    {
        "nome": "Ryan Oliveira",
        "cargo": "Dev. Jr",
        "idade": 19,
        "projetos": ["Projeto Prata"],
        "bloqueado": False
    },
    {
        "nome": "Wagner Silva",
        "cargo": "Dev. Pleno",
        "idade": 24,
        "projetos": ["Projeto Ouro"],
        "bloqueado": True
     }
    ]


def lines():
    print ("-" * 50)

lines()

print(f"            Cliqx Dev - Desafios - 2           ")
print()
print(f"Professores: Guilherme Parnaiba e Wagner Barth")

lines()

print()

lines()
print("        Média Aritimética Simples            ")

lines()

print()

soma = 0


for funcionarios in funcionarios:
    media = funcionarios["idade"]
    soma += media / 5




print(f" Média dos funcionários são:     {soma}       ")


print()

lines()

print("           Verificação no Array           ")

lines()

print()

flag = False

nome = input("Digite o nome do funcionário: ")

for i in range(len(funcionarios)):
    if funcionarios[i]["nome"] == nome:
        print(f"{funcionarios[i]['nome']}")
        flag = True

if not flag:
    print("Esse funcionário não existe")

print()
lines()


