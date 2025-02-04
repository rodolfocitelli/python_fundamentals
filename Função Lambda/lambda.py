# Uma função lambda simples que retorna o dobro de um número
dobro = lambda x: x * 2

# Testando a função lambda
print(dobro(5))  # Saída: 10

# Outro exemplo de função lambda que retorna a soma de dois números
soma = lambda a, b: a + b

# Testando a função lambda
print(soma(3, 4))  # Saída: 7

# Uma função lambda que retorna o maior de dois números
maior = lambda x, y: x if x > y else y

# Testando a função lambda
print(maior(10, 5))  # Saída: 10

# Funções lambda podem ser usadas dentro de outras funções
def aplicar_operacao(num, operacao):
  return operacao(num)

# Usando a função lambda 'dobro' dentro de 'aplicar_operacao'
resultado = aplicar_operacao(7, dobro)
print(resultado)  # Saída: 14

# Usando uma função lambda diretamente como argumento
resultado = aplicar_operacao(10, lambda x: x * x)  # Eleva ao quadrado
print(resultado)  # Saída: 100