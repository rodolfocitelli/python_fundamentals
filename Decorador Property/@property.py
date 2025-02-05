"""
Como o código funciona:

A classe Pessoa demonstra o uso do property para os atributos nome e idade. 
Vamos analisar o que acontece em cada parte:

1 - Definindo as propriedades:

* Usamos o decorador @property antes de um método para transformá-lo em um "getter", ou seja, 
  uma forma de acessar o valor do atributo.

* O decorador @nome.setter define um método "setter", que é chamado quando tentamos atribuir um novo valor ao atributo nome. 
  Aqui, podemos adicionar regras para garantir que o nome seja válido (por exemplo, não vazio).

* O decorador @nome.deleter define um método "deleter", que é chamado quando usamos o operador del 
  para tentar apagar o atributo.

2 - Usando as propriedades:

* Quando acessamos pessoa.nome, o método nome() (definido com @property) é chamado e 
  retorna o valor armazenado em self._nome.

* Quando fazemos pessoa.nome = "Lorena", o método nome(self, nome) (definido com @nome.setter) é chamado, 
  permitindo que o novo nome seja validado antes de ser atribuído.

* O mesmo acontece para o atributo idade, que tem um getter que calcula a idade com base no ano de nascimento 
  e um setter que permite modificar o ano de nascimento.
  
"""

class Pessoa:
    def __init__(self, nome = None, ano_nascimento = None):
        
        self._nome = nome
        self._ano_nascimento = ano_nascimento


    # A função @property faz com que o mêtodo vire um atributo
    @property
    def nome(self):
        return self._nome
    
     # A função @setter faz parte de @property
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # A função @deleter faz parte de @property
    @nome.deleter
    def nome(self):
        self._nome = None
    
    # ------------------------------------------------------#

    # A função @property faz com que o mêtodo vire um atributo 
    @property
    def idade(self):

        if self._ano_nascimento:
           ano_atual = 2024
           return ano_atual - self._ano_nascimento
    
    # A função @setter faz parte de @property
    @idade.setter
    def idade(self, ano_nascimeto):
        self._ano_nascimento = ano_nascimeto

    
    # A função @deleter faz parte de @property
    @idade.deleter
    def idade(self):
        self._ano_nascimento = None

# ----------------------------------------------------#

# Instância da classe Pessoa
pessoa = Pessoa("Rodolfo", 1990)

# Chama a função @property
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

# Chama a função @setter
pessoa.nome = "Lorena"
pessoa.idade = 2021

# Chama a função @property
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

# Chama a função @deleter
del pessoa.nome
del pessoa.idade

# Chama a função @property
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

