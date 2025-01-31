"""
Explicação do código:

1 - Classe abstrata Forma:

    Define os métodos abstratos calcular_area e calcular_perimetro.
    Esses métodos não têm implementação, servindo como um contrato para as subclasses.

2 - Classes concretas Retangulo e Circulo:

    Herdam da classe abstrata Forma.
    Implementam os métodos abstratos calcular_area e calcular_perimetro, 
    fornecendo a lógica específica para cada forma geométrica.

3 - Exemplo de uso:

    Cria instâncias das classes concretas Retangulo e Circulo.
    Chama os métodos calcular_area e calcular_perimetro para calcular e exibir 
    a área e o perímetro de cada forma.

4 - Conceito de classes abstratas:

Classes abstratas não podem ser instanciadas diretamente.
Servem como modelos para outras classes (subclasses).
Garantem que as subclasses implementem determinados métodos (contrato).
Promovem a reutilização de código e a consistência na hierarquia de classes.
"""

from abc import ABC, abstractmethod

# Classe abstrata
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

# Classes concretas que herdam da classe abstrata
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio**2

    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio

# Exemplo de uso
retangulo = Retangulo(5, 10)
print(f"Área do retângulo: {retangulo.calcular_area()}")
print(f"Perímetro do retângulo: {retangulo.calcular_perimetro()}")

circulo = Circulo(7)
print(f"Área do círculo: {circulo.calcular_area()}")
print(f"Perímetro do círculo: {circulo.calcular_perimetro()}")