"""
Exemplo Simples de Iterações em Python:
Em Python, iterações são formas de repetir um bloco de código várias vezes. 
Isso é útil para percorrer coleções de dados, executar tarefas repetitivas ou criar estruturas de repetição.

Tipos de Iterações:
Existem dois tipos principais de iterações em Python:

for: Usado para iterar sobre uma sequência (como uma lista, tupla, string ou dicionário) ou qualquer outro objeto iterável.
while: Usado para repetir um bloco de código enquanto uma condição for verdadeira.

"""

# Exemplo com for --------------------------------------------

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
  print(f"Eu gosto de {fruta}")

"""
Saída:
Eu gosto de maçã
Eu gosto de banana
Eu gosto de laranja
"""

# Exemplo com while ------------------------------------------

contador = 0

while contador < 5:
  print(f"Contador: {contador}")
  contador += 1

"""
Saída:
Contador: 0
Contador: 1
Contador: 2
Contador: 3
Contador: 4

"""

"""
Observações:

É importante definir uma condição de parada para loops while, caso contrário, 
eles podem se tornar infinitos.

Loops for são geralmente mais adequados para iterar sobre coleções de dados, 
enquanto loops while são mais flexíveis para outros tipos de repetição.

"""