unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

num = int(input("Digite um número entre 0 e 99: "))

if 0 <= num < 20:
    print(unidades[num])
elif 20 <= num <= 99:
    dezena = num // 10
    unidade = num % 10
    if unidade == 0:
        print(dezenas[dezena])
    else:
        print(f"{dezenas[dezena]} e {unidades[unidade]}")
else:
    print("Número fora do intervalo.")