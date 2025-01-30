"""
Neste exemplo, demonstramos como criar um conjunto, adicionar e remover elementos, 
verificar se um elemento pertence ao conjunto e realizar operações básicas como união, interseção e diferença.
Lembre-se de que os conjuntos em Python são estruturas de dados que não permitem elementos duplicados 
e não possuem uma ordem específica.
"""

# Criando um conjunto
conjunto = {1, 2, 3, 4, 5}

# Imprimindo o conjunto
print(conjunto)  # Saída: {1, 2, 3, 4, 5}

# Adicionando um elemento ao conjunto
conjunto.add(6)

# Imprimindo o conjunto atualizado
print(conjunto)  # Saída: {1, 2, 3, 4, 5, 6}

# Removendo um elemento do conjunto
conjunto.remove(3)

# Imprimindo o conjunto atualizado
print(conjunto)  # Saída: {1, 2, 4, 5, 6}

# Verificando se um elemento pertence ao conjunto
print(2 in conjunto)  # Saída: True
print(3 in conjunto)  # Saída: False

# Operações com conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# União de conjuntos
uniao = conjunto1 | conjunto2
print(uniao)  # Saída: {1, 2, 3, 4, 5}

# Interseção de conjuntos
intersecao = conjunto1 & conjunto2
print(intersecao)  # Saída: {3}

# Diferença de conjuntos
diferenca = conjunto1 - conjunto2
print(diferenca)  # Saída: {1, 2}