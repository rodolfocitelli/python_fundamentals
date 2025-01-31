"""
Exemplo Simples de Classes em Python
Em Python, uma classe é como um modelo para criar objetos. Pense em uma classe como uma forma de bolo: você pode usar essa forma para criar vários bolos diferentes (objetos), cada um com suas próprias características (atributos) e comportamentos (métodos).

Vamos criar uma classe chamada Carro que terá os atributos marca, modelo e ano, e o método ligar().
"""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("O carro está ligado!")

"""
class Carro: Define a classe chamada Carro.

def __init__(self, marca, modelo, ano): Este é o método construtor da classe. 
Ele é chamado automaticamente quando um novo objeto Carro é criado. 
O self se refere ao objeto que está sendo criado. 
Os parâmetros marca, modelo e ano são usados para inicializar os atributos do objeto.
self.marca = marca: Atribui o valor do parâmetro marca ao atributo marca do objeto. O mesmo é feito para modelo e ano.

def ligar(self): Define o método ligar(). Este método imprime a mensagem "O carro está ligado!" quando é chamado.

Agora, vamos criar um objeto Carro:
"""

meu_carro = Carro("Toyota", "Corolla", 2020)

"""
meu_carro = Carro("Toyota", "Corolla", 2020): Cria um novo objeto Carro chamado meu_carro. 
Os valores "Toyota", "Corolla" e 2020 são passados para o método construtor para inicializar os atributos do objeto.
"""

# Podemos acessar os atributos do objeto:
print(meu_carro.marca)  # Saída: Toyota
print(meu_carro.modelo)  # Saída: Corolla
print(meu_carro.ano)  # Saída: 2020

# Chamando o metodo ligar():
meu_carro.ligar()  # Saída: O carro está ligado!