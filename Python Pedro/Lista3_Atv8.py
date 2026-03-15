p1 = float(input("Digite o preço do 1º produto: R$ "))
p2 = float(input("Digite o preço do 2º produto: R$ "))
p3 = float(input("Digite o preço do 3º produto: R$ "))

if p1 < p2 and p1 < p3:
    print("Você deve comprar o 1º produto.")
elif p2 < p1 and p2 < p3:
    print("Você deve comprar o 2º produto.")
else:
    print("Você deve comprar o 3º produto.")