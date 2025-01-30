# Tupla de números inteiros
numeros = (1, 2, 3, 4, 5)

# Tupla de strings
nomes = ("Alice", "Bob", "Charlie")

# Tupla de tipos diferentes
dados_pessoais = ("Maria", 30, "Rua das Flores, 123")

# Tupla aninhada (uma tupla dentro de outra)
coordenadas = ((10, 20), (30, 40))

# imprimindo as tuplas
print("numeros: ", numeros)
print("nomes: ", nomes)
print("dados_pessoais: ", dados_pessoais)
print("coordenadas: ", coordenadas)

print("\n") # Quebra de linha

# Você pode acessar os elementos de uma tupla utilizando índices, da mesma forma que em listas:
print(numeros[0])  # Saída: 1
print(nomes[1])  # Saída: Bob
print(dados_pessoais[2])  # Saída: Rua das Flores, 123
print(coordenadas[0]) # Saída: (10, 20)

# Tuplas são imutáveis
# nomes.append("Rodolfo") Isso causaria um erro, pois tuplas são imutáveis