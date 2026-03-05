n1 = input("Digite o 1º número: ")
n2 = input("Digite o 2º número: ")
n3 = input("Digite o 3º número: ")

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)