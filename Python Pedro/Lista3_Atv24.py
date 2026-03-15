num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+': res = num1 + num2
elif operacao == '-': res = num1 - num2
elif operacao == '*': res = num1 * num2
elif operacao == '/': res = num1 / num2
else: 
    print("Operação inválida.")
    res = None

if res is not None:
    print(f"Resultado: {res}")
    print("Par" if res % 2 == 0 else "Ímpar")
    print("Positivo" if res > 0 else "Negativo" if res < 0 else "Zero")
    print("Inteiro" if res == round(res) else "Decimal")