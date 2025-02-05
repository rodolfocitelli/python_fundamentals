"""
Em Python, a manipulação de arquivos JSON (JavaScript Object Notation) é facilitada pelo módulo json, 
que permite codificar e decodificar dados nesse formato. JSON é um formato leve de troca de dados, 
amplamente utilizado em APIs web e outras aplicações.

Codificação de dados Python para JSON:

Para transformar dados Python em formato JSON, você pode usar a função json.dumps(). 
Essa função recebe um objeto Python como entrada e retorna uma string JSON.

"""
import json

data = {
    "nome": "Rodolfo",
    "idade": 34,
    "cidade": "Conchal"
}

json_data = json.dumps(data)
print(json_data) # {"nome": "Rodolfo", "idade": 34, "cidade": "Conchal"}

"""
Para realizar o processo inverso e transformar uma string JSON em um objeto Python, 
utilize a função json.loads().
"""

json_data = '{"nome": "Rodolfo", "idade": 34, "cidade": "Conchal"}'

data = json.loads(json_data)
print(data) # {'nome': 'Rodolfo', 'idade': 34, 'cidade': 'Cocnhal'}

"""
Leitura e escrita de arquivos JSON:

Para trabalhar com arquivos JSON, você pode usar as funções json.dump() e json.load(). 
A primeira permite escrever dados Python em um arquivo JSON, enquanto a segunda lê dados de um arquivo JSON 
e os converte em um objeto Python.
"""

with open('dados.json', 'w') as f:
    json.dump(data, f)

# Lendo dados de um arquivo JSON
with open('dados.json', 'r') as f:
    data = json.load(f)

print(data) # {'nome': 'Rodolfo', 'idade': 34, 'cidade': 'Conchal'}

"""
Observações:

* Ao escrever em um arquivo JSON, utilize o modo de abertura 'w' para sobrescrever 
  o conteúdo existente ou criar um novo arquivo.
* Ao ler um arquivo JSON, utilize o modo de abertura 'r'.
* Certifique-se de que os dados Python que você está codificando são serializáveis em JSON. 
  Tipos de dados comuns, como strings, números, listas e dicionários, são compatíveis.
* Em caso de erros durante a leitura ou escrita de arquivos JSON, 
  utilize blocos try...except para lidar com exceções.
  
"""