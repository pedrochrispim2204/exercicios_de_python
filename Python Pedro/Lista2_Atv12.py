telefone = input("Telefone: ").replace("-", "")

if len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
    telefone_corrigido = "3" + telefone
    print(f"Telefone corrigido sem formatação: {telefone_corrigido}")
    print(f"Telefone corrigido com formatação: {telefone_corrigido[:4]}-{telefone_corrigido[4:]}")
elif len(telefone) == 8:
    print(f"Telefone válido. Com formatação: {telefone[:4]}-{telefone[4:]}")
else:
    print("Tamanho de telefone inválido para este exercício.")