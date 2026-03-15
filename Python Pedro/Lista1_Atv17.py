import math

area = float(input("Digite o tamanho da área a ser pintada (m²): "))
area_com_folga = area * 1.1
litros_necessarios = area_com_folga / 6

# Opção 1: Apenas latas de 18L
latas_apenas = math.ceil(litros_necessarios / 18)
preco_latas = latas_apenas * 80.00

# Opção 2: Apenas galões de 3,6L
galoes_apenas = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes_apenas * 25.00

# Opção 3: Misturar latas e galões (para menor desperdício)
latas_mistas = int(litros_necessarios // 18)
litros_restantes = litros_necessarios % 18
galoes_mistos = math.ceil(litros_restantes / 3.6)
preco_misto = (latas_mistas * 80.00) + (galoes_mistos * 25.00)

print("\n--- Opções de Compra ---")
print(f"1. Apenas latas (18L): {latas_apenas} lata(s) por R$ {preco_latas:.2f}")
print(f"2. Apenas galões (3,6L): {galoes_apenas} galão(ões) por R$ {preco_galoes:.2f}")
print(f"3. Misto (melhor preço): {latas_mistas} lata(s) e {galoes_mistos} galão(ões) por R$ {preco_misto:.2f}")