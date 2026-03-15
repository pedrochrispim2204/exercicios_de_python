tamanho_arquivo = float(input("Tamanho do arquivo em MB: "))
velocidade_internet = float(input("Velocidade do link de internet em Mbps: "))

# Converte Mbps (Megabits) para MB/s (Megabytes) dividindo por 8
velocidade_mbs = velocidade_internet / 8
tempo_segundos = tamanho_arquivo / velocidade_mbs
tempo_minutos = tempo_segundos / 60

print(f"O tempo aproximado de download será de {tempo_minutos:.2f} minutos.")