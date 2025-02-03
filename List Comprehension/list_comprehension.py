"""
Resumo do código e explicação sobre List Comprehension:

O código demonstra o uso de List Comprehension em Python, uma forma concisa de criar listas.

1. Criação da lista original:

* lista = list(range(0, 20)): Cria uma lista com números de 0 a 19.
* print(lista): Imprime a lista criada.

2. List Comprehension:

* lista_quadrado = [x**2 for x in lista]: Cria uma nova lista, onde 
  cada elemento é o quadrado do elemento correspondente na lista original.
* lista_pares = [x for x in lista if x % 2 == 0]: Cria uma lista contendo apenas os números pares da lista original.
* lista_par_impar = [{x:"par"} if x % 2 == 0 else {x:"impar"} for x in lista]: Cria uma lista de dicionários. 
  Para cada número na lista original, o dicionário contém o número como chave e "par" ou "impar" como valor, 
  dependendo se o número é par ou ímpar

"""

# Declaração de uma lista
lista = list(range(0, 20))
print(lista)

# Cria um lista ao quadrado
lista_quadrado = [x**2 for x in lista]
print(f"Lista ao quadrado: {lista_quadrado}")

# Cria uma lista com numeros pares
lista_pares = [x for x in lista if x % 2 == 0]
print(f"Numeros pares: {lista_pares}")

# Cria uma lista com chaves e valor para números pares e ímpares
lista_par_impar = [{x:"par"} if x % 2 == 0 else {x:"impar"} for x in lista]
print(f"Pares e impares na lista: {lista_par_impar}")