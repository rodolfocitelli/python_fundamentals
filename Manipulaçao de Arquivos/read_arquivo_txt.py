"""
O código demonstra três formas de ler o conteúdo de um arquivo de texto ("Lorem.txt") em Python:

* read(): Lê todo o conteúdo do arquivo de uma vez e o retorna como uma string.

* readline(): Lê apenas a primeira linha do arquivo e a retorna como uma string.

* readlines(): Lê todas as linhas do arquivo e as retorna como uma lista de strings, 
  onde cada string é uma linha do arquivo.

Observações:

As três funções abrem o arquivo em modo de leitura ("r") e o fecham após a leitura.
O arquivo "Lorem.txt" precisa existir no mesmo diretório que o script Python para que o código funcione.

"""

# read() ==================================

# Abrindo um arquivo txt com "read"
arquivo = open("Lorem.txt", "r")

# Imprimindo arquivo
# retorna todo o conteudo do arquivo
print(arquivo.read())

# Fechando arquivo
arquivo.close()

# readline() ===============================

# Abrindo um arquivo txt com "read"
arquivo = open("Lorem.txt", "r")

# Retorna apenas uma linha do arquivo
print(arquivo.readline())

# Fechando arquivo
arquivo.close()

# readlines() ===============================

# Abrindo um arquivo txt com "read"
arquivo = open("Lorem.txt", "r")

# Retorna todas as linhas do arquivo em uma lista
print(arquivo.readlines())

# Fechando arquivo
arquivo.close()

# tips ===============================

# Abrindo um arquivo txt com "read"
arquivo = open("Lorem.txt", "r")

for line in arquivo.readlines():
    print(line)


# Fechando arquivo
arquivo.close()