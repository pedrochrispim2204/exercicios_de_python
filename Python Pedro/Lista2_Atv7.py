frase = input("Digite uma frase: ")

espacos = frase.count(' ')
vogais = sum(1 for letra in frase.lower() if letra in 'aeiouáéíóúâêîôûãõ')

print(f"A frase contém {espacos} espaço(s) e {vogais} vogal(is).")