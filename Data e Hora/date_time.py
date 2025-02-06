from datetime import datetime
import pytz

# Obter a data e hora atual no fuso horário local
data_hora_atual = datetime.now()
print(f"Data e hora atual (local): {data_hora_atual}")

# Obter a data e hora atual em UTC
data_hora_utc = datetime.utcnow()
print(f"Data e hora atual (UTC): {data_hora_utc}")

# Converter para um fuso horário específico (ex: São Paulo)
fuso_sp = pytz.timezone("America/Sao_Paulo")
data_hora_sp = data_hora_utc.astimezone(fuso_sp)
print(f"Data e hora em São Paulo: {data_hora_sp}")

# Formatar a data e hora
formato = "%d/%m/%Y %H:%M:%S"
data_hora_formatada = data_hora_sp.strftime(formato)
print(f"Data e hora formatada: {data_hora_formatada}")

# Criar um objeto datetime a partir de uma string
data_hora_string = "25/12/2023 10:30:00"
data_hora_obj = datetime.strptime(data_hora_string, formato)
print(f"Objeto datetime a partir da string: {data_hora_obj}")

# Realizar operações com datas e horas
diferenca = data_hora_sp - data_hora_obj
print(f"Diferença entre as datas: {diferenca}")