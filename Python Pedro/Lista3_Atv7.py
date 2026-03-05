n1 = input("Digite o 1º número: ")
n2 = input("Digite o 2º número: ")
n3 = input("Digite o 3º número: ")

if n1 > n2 and n1 > n3:
    print(f"Maior: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"Maior: {n2}")
else:
    print(f"Maior: {n3}")



if n1 < n2 and n1 < n3:
    print (f"Menor: {n1}")
elif n2 < n1 and n2 < n3:
    print (f"Menor: {n2}")
else: print (f"Menor: {n3}")