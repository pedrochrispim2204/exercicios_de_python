int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

calc_a = (2 * int1) * (int2 / 2)
calc_b = (3 * int1) + real
calc_c = real ** 3

print(f"Produto do dobro do primeiro com metade do segundo: {calc_a}")
print(f"Soma do triplo do primeiro com o terceiro: {calc_b}")
print(f"Terceiro elevado ao cubo: {calc_c:.2f}")