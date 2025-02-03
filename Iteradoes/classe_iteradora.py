"""
Exemplo Simples de Classe Iteradora em Python:

Em Python, um iterador é um objeto que permite percorrer uma sequência de elementos, como uma lista ou tupla. 
Para criar um iterador personalizado, você precisa definir uma classe que implemente os métodos __iter__() e __next__().

O método __iter__() retorna o próprio objeto iterador. Ele é chamado no início da iteração,
quando você usa um loop for ou a função iter().

O método __next__() retorna o próximo elemento da sequência. Ele é chamado a cada iteração do loop. 
Quando não há mais elementos, ele deve lançar uma exceção StopIteration.
"""

class Numeros:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

# Cria um objeto iterador
numeros = Numeros()

# Percorre os números usando um loop for
for x in numeros:
  print(x)

"""
Explicação:

A classe Numeros possui um atributo a que armazena o número atual.
O método __iter__() inicializa o atributo a com o valor 1 e retorna o próprio objeto iterador.
O método __next__() retorna o valor atual de a e o incrementa em 1. Se a for maior que 5, ele lança uma exceção StopIteration.
O loop for itera sobre o objeto numeros, chamando o método __next__() a cada iteração e imprimindo o valor retornado.
"""