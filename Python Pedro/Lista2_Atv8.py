texto = input("Digite uma frase ou palavra: ").lower().replace(" ", "")
# Removendo acentos básicos para garantir a precisão
texto = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")