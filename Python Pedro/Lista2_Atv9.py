def valida_cpf(cpf):
    # Extrai apenas os números
    numeros = [int(digito) for digito in cpf if digito.isdigit()]
    
    # Verifica se tem 11 dígitos ou se são todos iguais (ex: 111.111.111-11)
    if len(numeros) != 11 or len(set(numeros)) == 1:
        return False
        
    # Cálculo do primeiro dígito verificador
    soma = sum(n * peso for n, peso in zip(numeros[:9], range(10, 1, -1)))
    d1 = 11 - (soma % 11)
    d1 = 0 if d1 >= 10 else d1
    
    # Cálculo do segundo dígito verificador
    soma = sum(n * peso for n, peso in zip(numeros[:10], range(11, 1, -1)))
    d2 = 11 - (soma % 11)
    d2 = 0 if d2 >= 10 else d2
    
    return numeros[9] == d1 and numeros[10] == d2

cpf_input = input("Digite o CPF (xxx.xxx.xxx-xx): ")
if valida_cpf(cpf_input):
    print("CPF Válido!")
else:
    print("CPF Inválido!")