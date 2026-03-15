import math

area = float(input("Digite o tamanho da área a ser pintada (m²): "))
litros_necessarios = area / 3
latas = math.ceil(litros_necessarios / 18)
preco_total = latas * 80.00

print(f"Você precisará de {latas} lata(s) de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")