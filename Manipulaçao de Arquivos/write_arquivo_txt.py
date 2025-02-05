"""
O código Python demonstra como escrever em arquivos de texto usando as funções write() e writelines().

Parte 1: Usando write()

1 - Abre o arquivo: arquivo = open("Teste.txt", "w") abre o arquivo "Teste.txt" em modo de escrita ("w"). 
    Se o arquivo não existir, ele será criado. Se já existir, o conteúdo antigo será apagado.

2 - Escreve no arquivo: arquivo.write("Escrevendo dados em um novo arquivo") escreve a string especificada no arquivo.

3 - Fecha o arquivo: arquivo.close() fecha o arquivo, garantindo que os dados sejam gravados e os recursos sejam liberados.

Parte 2: Usando writelines()

1 - Cria uma lista de strings: string = ["Escrevendo ", "um ", "novo", " texto"] 
    cria uma lista de strings que serão escritas no arquivo.

2 - Abre o arquivo (novamente): arquivo = open("Teste.txt", "w") abre o mesmo arquivo "Teste.txt" em modo de escrita. 
    O conteúdo anterior será apagado novamente.

3 - Escreve as strings no arquivo: arquivo.writelines(string) escreve todas as strings da lista no arquivo.
    Fecha o arquivo: arquivo.close() fecha o arquivo.

Resultado:

Após a execução do código, o arquivo "Teste.txt" conterá o seguinte texto: "Escrevendo um novo texto". 
O conteúdo anterior ("Escrevendo dados em um novo arquivo") foi substituído 
quando o arquivo foi aberto novamente em modo de escrita.

"""

# Abrindo um arquivo txt com "write"
arquivo = open("Teste.txt", "w")

# Escrevendo no arquivo
arquivo.write("Escrevendo dados em um novo arquivo")

# Fechando arquivo
arquivo.close()

# ===================================

string = ["Escrevendo ", "um ", "novo", " texto"]

# Abrindo um arquivo txt com "write"
arquivo = open("Teste.txt", "w")

# Escreve uma string por vez no arquivo
arquivo.writelines(string)

# Fechando arquivo
arquivo.close()
