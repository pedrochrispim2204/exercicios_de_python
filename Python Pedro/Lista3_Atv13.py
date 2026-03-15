dia = int(input("Digite um número (1-7) para o dia da semana: "))

dias = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 
        5: "Quinta", 6: "Sexta", 7: "Sábado"}

if dia in dias:
    print(dias[dia])
else:
    print("Valor inválido.")