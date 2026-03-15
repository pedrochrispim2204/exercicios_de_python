numero = int(input("Digite um número menor que 1000: "))

if 0 <= numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    
    partes = []
    if centenas > 0:
        partes.append(f"{centenas} centena{'s' if centenas > 1 else ''}")
    if dezenas > 0:
        partes.append(f"{dezenas} dezena{'s' if dezenas > 1 else ''}")
    if unidades > 0:
        partes.append(f"{unidades} unidade{'s' if unidades > 1 else ''}")
        
    if len(partes) == 3:
        resultado = f"{partes[0]}, {partes[1]} e {partes[2]}"
    elif len(partes) == 2:
        resultado = f"{partes[0]} e {partes[1]}"
    elif len(partes) == 1:
        resultado = partes[0]
    else:
        resultado = "0 unidades"
        
    print(resultado)
else:
    print("Número fora do intervalo permitido.")