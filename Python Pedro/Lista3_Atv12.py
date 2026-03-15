valor_hora = float(input("Digite o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    perc_ir = 0
elif salario_bruto <= 1500:
    perc_ir = 5
elif salario_bruto <= 2500:
    perc_ir = 10
else:
    perc_ir = 20

ir = salario_bruto * (perc_ir / 100)
inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.03 # Conforme enunciado
fgts = salario_bruto * 0.11
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({perc_ir}%) : R$ {ir:.2f}")
print(f"(-) INSS (10%) : R$ {inss:.2f}")
print(f"(-) Sindicato (3%) : R$ {sindicato:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de descontos : R$ {total_descontos:.2f}")
print(f"Salário Liquido : R$ {salario_liquido:.2f}")