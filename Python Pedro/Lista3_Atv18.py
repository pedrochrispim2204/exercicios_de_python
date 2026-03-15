data = input("Digite uma data (dd/mm/aaaa): ")
try:
    dia, mes, ano = map(int, data.split('/'))
    valida = True
    
    if mes < 1 or mes > 12:
        valida = False
    elif mes in [1, 3, 5, 7, 8, 10, 12] and (dia < 1 or dia > 31):
        valida = False
    elif mes in [4, 6, 9, 11] and (dia < 1 or dia > 30):
        valida = False
    elif mes == 2:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        if bissexto and (dia < 1 or dia > 29):
            valida = False
        elif not bissexto and (dia < 1 or dia > 28):
            valida = False
            
    if valida:
        print("Data válida!")
    else:
        print("Data inválida!")
except:
    print("Formato inválido. Use dd/mm/aaaa.")