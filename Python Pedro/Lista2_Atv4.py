nome = input("Digite o seu nome: ").upper()
for i in range(1, len(nome) + 1):
    print(nome[:i])