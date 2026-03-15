numeros = []
for i in range(3):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros.sort(reverse=True)
print(f"Os números em ordem decrescente são: {numeros}")