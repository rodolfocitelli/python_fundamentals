"""
O código Python demonstra como criar e ler um arquivo CSV:

Função: O código cria um arquivo CSV chamado "usuarios.csv" na mesma pasta do script, 
escreve dados de usuários (id e nome) e, em seguida, lê e imprime o conteúdo deste arquivo.

Passos:

1 - Importação de módulos:

    * csv: Para trabalhar com arquivos CSV.
    * pathlib: Para lidar com caminhos de arquivos de forma mais robusta.

2 - Definição do caminho:

    * ROOT_PATH: Define o caminho para a pasta onde o script está localizado.

3 - Escrita do arquivo CSV:

    * Abre o arquivo "usuarios.csv" em modo de escrita ("w"). Se o arquivo não existir, 
      ele será criado. Se existir, o conteúdo anterior será apagado.
    * Cria um objeto escritor do tipo csv.writer para escrever no arquivo.
    * Escreve a linha de cabeçalho ("id", "nome") e três linhas de dados de usuários.
    * Em caso de erro (IOError), imprime uma mensagem de erro.

4 - Leitura do arquivo CSV:

    * Abre o mesmo arquivo "usuarios.csv" em modo de leitura ("r").
    * Cria um objeto leitor do tipo csv.reader para ler o arquivo.
    * Itera sobre cada linha do arquivo, e imprime cada linha.
    * Em caso de erro (IOError), imprime uma mensagem de erro.

Saída:

O código irá imprimir no console:

['id', 'nome']
['1', 'Rodolfo']
['2', 'Tatiane']
['3', 'Lorena']

Observações:

O código usa tratamento de exceções (try...except) para lidar com possíveis erros de 
leitura ou escrita de arquivos.
A codificação UTF-8 (encoding="utf-8") é especificada para garantir a correta 
leitura e escrita de caracteres especiais, como acentos.
O código é um exemplo básico de como criar e ler arquivos CSV em Python. 
Em situações reais, você pode querer adicionar mais funcionalidades, como validação de dados, 
tratamento de diferentes delimitadores, etc.

"""

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# write ==============================================================================================
try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Rodolfo"])
        escritor.writerow(["2", "Tatiane"])
        escritor.writerow(["3", "Lorena"])

except IOError as exc:
    print(f"Erro ao criar o arquivo {exc}") 

# read ==============================================================================================
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:

        leitor = csv.reader(arquivo)

        for row in leitor:
            print(row)
       
except IOError as exc:
    print(f"Erro ao ler o arquivo {exc}") 

    