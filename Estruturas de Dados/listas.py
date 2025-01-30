# Uma lista de frutas
frutas = ["maçã", "banana", "laranja"]

# Uma lista de números 
numeros = list(range(1,21))


# Imprimindo a lista de frutas
print("Lista de frutas:")
print(frutas)

# Imprimindo a lista de números
print("\nLista de numeros:")
print(numeros)

# Acessando elementos da lista 
print("\nPrimeira fruta:", frutas[0])
print("\nSegundo número:", numeros[1])


# Listas são mutáveis
frutas.append("uva")  # Adiciona "uva" à lista de frutas
numeros.append(21)  # Adiciona 21 à lista de frutas


print("\nLista de frutas após adicionar 'uva':")
print(frutas)

print("\nLista de numeros após adicionar '21':")
print(numeros)