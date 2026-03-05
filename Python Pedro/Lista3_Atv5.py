n1 = int (input("Digite a 1ª nota: "))
n2 = int (input("Digite a 2ª nota: "))

if (n1+n2)/2 >= 10:
    print("Aprovado com Distinção!")
elif (n1+n2)/2 < 7:
    print ("Reprovado!")
else:
    print ("Aprovado")