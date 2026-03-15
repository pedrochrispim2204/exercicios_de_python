tipo_carne = input("Tipo de carne (F-File Duplo, A-Alcatra, P-Picanha): ").upper()
kg = float(input("Quantidade (Kg): "))
cartao = input("Pagamento com cartão Tabajara? (S/N): ").upper()

if tipo_carne == 'F':
    nome = "Filé Duplo"
    preco_kg = 4.90 if kg <= 5 else 5.80
elif tipo_carne == 'A':
    nome = "Alcatra"
    preco_kg = 5.90 if kg <= 5 else 6.80
elif tipo_carne == 'P':
    nome = "Picanha"
    preco_kg = 6.90 if kg <= 5 else 7.80
else:
    nome = "Inválido"
    preco_kg = 0

if nome != "Inválido":
    preco_total = kg * preco_kg
    desconto = preco_total * 0.05 if cartao == 'S' else 0
    valor_pagar = preco_total - desconto

    print("\n--- CUPOM FISCAL ---")
    print(f"Carne: {nome}")
    print(f"Quantidade: {kg} Kg")
    print(f"Preço total: R$ {preco_total:.2f}")
    print(f"Tipo de pagamento: {'Cartão Tabajara' if cartao == 'S' else 'Outro'}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_pagar:.2f}")
else:
    print("Opção de carne inválida.")