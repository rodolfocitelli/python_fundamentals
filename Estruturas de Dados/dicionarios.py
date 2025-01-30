"""
Um dicionário Python é uma estrutura de dados que armazena pares chave-valor. 
Cada chave é única e usada para acessar seu valor correspondente.

Neste exemplo, criamos um dicionário chamado pessoa com informações sobre uma pessoa. 
Usamos chaves como "nome", "idade" e "cidade" para acessar os valores correspondentes.

Adicionamos um novo par chave-valor para a profissão da pessoa e alteramos sua idade. 
Em seguida, removemos o par chave-valor da cidade.

Usamos o operador in para verificar se uma chave existe no dicionário.
Iteramos sobre as chaves, valores e pares chave-valor do dicionário usando loops for.
"""

# Criando um dicionário
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Acessando valores
print(pessoa["nome"])  # Saída: João
print(pessoa["idade"]) # Saída: 30

# Adicionando novos pares chave-valor
pessoa["profissão"] = "Engenheiro"
print(pessoa)  # Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# Alterando valores
pessoa["idade"] = 35
print(pessoa)  # Saída: {'nome': 'João', 'idade': 35, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# Removendo pares chave-valor
del pessoa["cidade"]
print(pessoa)  # Saída: {'nome': 'João', 'idade': 35, 'profissão': 'Engenheiro'}

# Verificando se uma chave existe
print("nome" in pessoa)  # Saída: True
print("cidade" in pessoa)  # Saída: False

# Iterando sobre as chaves
for chave in pessoa:
    print(chave)

# Iterando sobre os valores
for valor in pessoa.values():
    print(valor)

# Iterando sobre os pares chave-valor
for chave, valor in pessoa.items():
    print(chave, valor)