import random

palavras = ["teclado", "mouse", "monitor", "python", "sistema"]
palavra_secreta = random.choice(palavras).upper()

# Embaralha as letras
letras = list(palavra_secreta)
random.shuffle(letras)
palavra_embaralhada = "".join(letras)

print(f"Adivinhe a palavra: {palavra_embaralhada}")

tentativas = 5
while tentativas > 0:
    palpite = input("Seu palpite: ").upper()
    if palpite == palavra_secreta:
        print("Parabéns, você acertou!")
        break
    else:
        tentativas -= 1
        print(f"Errado! Você tem {tentativas} tentativa(s) restante(s).")

if tentativas == 0:
    print(f"Fim de jogo! A palavra era: {palavra_secreta}")