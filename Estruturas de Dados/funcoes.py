"""
Neste exemplo, definimos três funções simples em Python:

1 - dobrar_numero: Esta função recebe um número como entrada e retorna o dobro desse número.
2 - imprimir_mensagem: Esta função recebe um nome e uma saudação (opcional) como entrada e imprime uma mensagem personalizada.
3 - somar_numeros: Esta função recebe um número variável de argumentos e retorna a soma deles.
    Em seguida, chamamos essas funções com diferentes valores e imprimimos os resultados.

Este é apenas um exemplo básico de como usar funções em Python. 
As funções são uma ferramenta poderosa que permite modularizar seu código, tornando-o mais organizado, 
reutilizável e fácil de manter.

Com funções, você pode dividir seu programa em partes menores e mais gerenciáveis, o que facilita o desenvolvimento, 
teste e depuração do seu código. Além disso, as funções podem ser reutilizadas em diferentes partes do seu programa 
ou em outros programas, o que economiza tempo e esforço.
"""

# Definindo uma função simples que retorna o dobro de um número
def dobrar_numero(numero):
  """
  Esta função recebe um número como entrada e retorna o dobro desse número.
  """
  return numero * 2

# Chamando a função com diferentes valores
resultado1 = dobrar_numero(5)
resultado2 = dobrar_numero(10)
resultado3 = dobrar_numero(15)

# Imprimindo os resultados
print("O dobro de 5 é:", resultado1)  # Saída: O dobro de 5 é: 10
print("O dobro de 10 é:", resultado2) # Saída: O dobro de 10 é: 20
print("O dobro de 15 é:", resultado3) # Saída: O dobro de 15 é: 30

# Definindo uma função que imprime uma mensagem personalizada
def imprimir_mensagem(nome, saudacao="Olá"):
  """
  Esta função recebe um nome e uma saudação (opcional) como entrada e imprime uma mensagem personalizada.
  """
  print(f"{saudacao}, {nome}!")

# Chamando a função com diferentes valores
imprimir_mensagem("João")           # Saída: Olá, João!
imprimir_mensagem("Maria", "Bom dia") # Saída: Bom dia, Maria!

# Definindo uma função com parâmetros variáveis
def somar_numeros(*args):
  """
  Esta função recebe um número variável de argumentos e retorna a soma deles.
  """
  soma = 0
  for numero in args:
    soma += numero
  return soma

# Chamando a função com diferentes números de argumentos
resultado4 = somar_numeros(1, 2, 3)
resultado5 = somar_numeros(4, 5, 6, 7)

# Imprimindo os resultados
print("A soma de 1, 2 e 3 é:", resultado4)    # Saída: A soma de 1, 2 e 3 é: 6
print("A soma de 4, 5, 6 e 7 é:", resultado5) # Saída: A soma de 4, 5, 6 e 7 é: 22