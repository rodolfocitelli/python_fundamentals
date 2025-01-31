"""
Explicação do código:

A classe Animal é a classe pai, que define o atributo nome e o método falar().
As classes Cachorro e Gato são classes filhas que herdam da classe Animal.
O método super().__init__(nome) dentro das classes filhas chama o construtor da classe pai para inicializar o atributo nome.
Cada classe filha pode ter seus próprios atributos e métodos, como raca para Cachorro e cor para Gato.
O método falar() é sobrescrito nas classes filhas para fornecer um comportamento específico para cada tipo de animal.
Vantagens da herança:

Reutilização de código: Evita a repetição de código comum entre classes relacionadas.
Organização: Organiza as classes em uma hierarquia lógica, facilitando a compreensão e manutenção do código.
Extensibilidade: Permite adicionar novas funcionalidades às classes filhas sem modificar o código da classe pai.
"""

# Classe pai
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som genérico de animal")

# Classe filha que herda de Animal
class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chama o construtor da classe pai para inicializar o atributo nome
        super().__init__(nome)
        self.raca = raca

    def falar(self):
        print("Au au!")

# Classe filha que herda de Animal
class Gato(Animal):
    def __init__(self, nome, cor):
        # Chama o construtor da classe pai para inicializar o atributo nome
        super().__init__(nome)
        self.cor = cor

    def falar(self):
        print("Miau!")

# Criando objetos
animal = Animal("Genérico")
cachorro = Cachorro("Rex", "Pastor Alemão")
gato = Gato("Mimi", "Siames")

# Chamando métodos
animal.falar()  # Saída: Som genérico de animal
cachorro.falar()  # Saída: Au au!
gato.falar()  # Saída: Miau!

# Acessando atributos
print(cachorro.nome)  # Saída: Rex
print(gato.cor)  # Saída: Siames