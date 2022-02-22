soma = 0
somaDepois = 0
cont = 1

while somaDepois < 10000000000:
    print(f"{cont}: {somaDepois} ")
    cont += 1
    somaDepois = somaDepois + soma
    soma = somaDepois - soma
    if somaDepois == 0:
        somaDepois = somaDepois + 1

"""
i = 0
p = 1 

txt = f"{i}, {p}"

for n in range(50)
    
    f = i + 
    if n < 49:
        txt += "{f}, "
    else:
        txt += f"{f} "
    i = p 
    p = f

print(txt)
"""