## Código Python para Manipulação de Data, Hora e Fuso Horário

O arquivo date_time.py demonstra como realizar operações básicas com datas, 
horas e fusos horários em Python, utilizando o módulo `datetime` e a biblioteca `pytz`.

## Importação de módulos

* `datetime`: módulo para trabalhar com datas e horas.
* `pytz`: biblioteca para lidar com fusos horários.
  
## Obtenção da data e hora atual

* `datetime.now()`: retorna a data e hora atual no fuso horário local.
* `datetime.utcnow()`: retorna a data e hora atual em UTC (Tempo Universal Coordenado).

## Conversão para fuso horário específico

* `pytz.timezone("America/Sao_Paulo")`: define o fuso horário de São Paulo.
* `astimezone(fuso_sp)`: converte o objeto datetime para o fuso horário especificado.
  
## Formatação da data e hora

* `strftime(formato)`: formata o objeto datetime de acordo com o formato especificado.
* `%d`: dia do mês (01 a 31)
* `%m`: mês (01 a 12)
* `%Y`: ano com quatro dígitos
* `%H`: hora (00 a 23)
* `%M`: minutos (00 a 59)
* `%S`: segundos (00 a 59)
  
## Criação de objeto datetime a partir de string

* `datetime.strptime(data_hora_string, formato)`: converte uma string em um objeto datetime, de acordo com o formato especificado.

## Operações com datas e horas

* É possível realizar diversas operações com objetos datetime, como calcular diferenças, adicionar ou subtrair dias, horas, etc.
  
## Observações

* Para instalar a biblioteca `pytz`, execute o comando `pip install pytz` no seu terminal.
* A lista de fusos horários disponíveis pode ser obtida `com pytz.all_timezones`.
* Este código é apenas um exemplo básico. A manipulação de datas, horas e fusos horários pode ser muito mais complexa,
  dependendo da sua necessidade.
