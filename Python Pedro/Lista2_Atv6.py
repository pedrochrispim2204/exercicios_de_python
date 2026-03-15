data = input("Digite a data (dd/mm/aaaa): ")
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dia, mes, ano = data.split('/')
nome_mes = meses[int(mes) - 1]

print(f"{dia} de {nome_mes} de {ano}")