str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

print(f"String 1: '{str1}' - Tamanho: {len(str1)}")
print(f"String 2: '{str2}' - Tamanho: {len(str2)}")

if len(str1) == len(str2):
    print("As duas strings têm o mesmo tamanho.")
else:
    print("As duas strings têm tamanhos diferentes.")

if str1 == str2:
    print("As duas strings possuem conteúdos iguais.")
else:
    print("As duas strings possuem conteúdos diferentes.")