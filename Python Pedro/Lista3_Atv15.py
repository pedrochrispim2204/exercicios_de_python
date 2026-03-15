l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Os valores formam um triângulo.")
    if l1 == l2 == l3:
        print("Tipo: Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")
else:
    print("Os valores não podem formar um triângulo.")