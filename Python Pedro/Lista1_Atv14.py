peso = float(input("Digite o peso total dos peixes (kg): "))
limite = 50.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00
    print(f"Houve um excesso de {excesso:.2f} kg.")
    print(f"O valor da multa a pagar é de R$ {multa:.2f}.")
else:
    print("Peso dentro do limite. Nenhuma multa será aplicada.")