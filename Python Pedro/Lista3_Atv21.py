saque = int(input("Digite o valor para saque (entre 10 e 600): "))

if 10 <= saque <= 600:
    notas_100 = saque // 100
    saque %= 100
    
    notas_50 = saque // 50
    saque %= 50
    
    notas_10 = saque // 10
    saque %= 10
    
    notas_5 = saque // 5
    saque %= 5
    
    notas_1 = saque
    
    print("Notas fornecidas:")
    if notas_100 > 0: print(f"{notas_100} nota(s) de 100")
    if notas_50 > 0: print(f"{notas_50} nota(s) de 50")
    if notas_10 > 0: print(f"{notas_10} nota(s) de 10")
    if notas_5 > 0: print(f"{notas_5} nota(s) de 5")
    if notas_1 > 0: print(f"{notas_1} nota(s) de 1")
else:
    print("Valor fora dos limites permitidos.")