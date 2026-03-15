print("Responda com 'S' para sim e 'N' para não:")
p1 = input("1. Telefonou para a vítima? ").upper()
p2 = input("2. Esteve no local do crime? ").upper()
p3 = input("3. Mora perto da vítima? ").upper()
p4 = input("4. Devia para a vítima? ").upper()
p5 = input("5. Já trabalhou com a vítima? ").upper()

respostas_positivas = [p1, p2, p3, p4, p5].count('S')

if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")