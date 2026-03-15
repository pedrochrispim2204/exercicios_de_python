kg_morango = float(input("Kg de Morangos: "))
kg_maca = float(input("Kg de Maçãs: "))

preco_morango = 2.50 if kg_morango <= 5 else 2.20
preco_maca = 1.80 if kg_maca <= 5 else 1.50

total_kg = kg_morango + kg_maca
valor_total = (kg_morango * preco_morango) + (kg_maca * preco_maca)

if total_kg > 8 or valor_total > 25.00:
    valor_total *= 0.90  # Desconto de 10%

print(f"Valor a pagar: R$ {valor_total:.2f}")