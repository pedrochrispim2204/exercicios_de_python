import random

palavras = ["PYTHON", "PROGRAMACAO", "COMPUTADOR", "ALGORITMO", "DESENVOLVEDOR"]
palavra = random.choice(palavras)
letras_descobertas = ["_"] * len(palavra)
tentativas = 6
letras_erradas = []

print("Bem-vindo ao Jogo da Forca!")

while tentativas > 0 and "_" in letras_descobertas:
    print(f"\nPalavra: {' '.join(letras_descobertas)}")
    print(f"Tentativas restantes: {tentativas}")
    if letras_erradas:
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
    chute = input("Digite uma letra: ").upper()
    
    if chute in palavra:
        for i, letra in enumerate(palavra):
            if letra == chute:
                letras_descobertas[i] = chute
    else:
        if chute not in letras_erradas:
            letras_erradas.append(chute)
            tentativas -= 1
            print("Letra errada!")

if "_" not in letras_descobertas:
    print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
else:
    print(f"\nFim de jogo. A palavra era: {palavra}")