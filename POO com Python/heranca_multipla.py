"""
O código demonstra o conceito de herança múltipla em Python, 
onde uma classe pode herdar atributos e métodos de múltiplas classes pai.

Classes:

Animal: Classe base com atributo nro_patas.
Mamifero (Animal): Herda de Animal e adiciona cor_pelo.
Ave (Animal): Herda de Animal e adiciona cor_bico.
Cachorro (Mamifero): Herda de Mamifero e adiciona porte.
Passaro (Ave): Herda de Ave e adiciona cor_pena.
Ornitorrinco (Mamifero, Ave): Exemplo de herança múltipla, herdando de Mamifero e Ave, adicionando filhote.
Herança Múltipla:

A classe Ornitorrinco herda características de Mamifero (cor do pelo) e Ave (cor do bico). 
Isso permite que instâncias de Ornitorrinco possuam atributos e comportamentos de ambas as classes pai.

Vantagens:

Reutilização de código de diferentes classes.
Modelagem de entidades com múltiplas naturezas.

Desafios:

Conflitos de nomes de atributos/métodos (resolvidos com super() e ordem de herança).
Complexidade na hierarquia de classes.

Código:

O código cria instâncias de diferentes classes, demonstrando a herança de atributos 
e como a herança múltipla permite que Ornitorrinco possua características de mamífero e ave.

Observação: A ordem de herança na definição de Ornitorrinco (Mamifero, Ave) é importante para a resolução de conflitos.
"""

# Criando classes
class Animal:
    def __init__(self, nro_patas):

        self.nro_patas = nro_patas

    def __repr__(self):

        return f"{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **Kw):

        super().__init__(**Kw)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **Kw):

        super().__init__(**Kw)
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    def __init__(self, porte, **Kw):

        super().__init__(**Kw)
        self.porte = porte


class Passaro(Ave):
    def __init__(self, cor_pena, **Kw):

        super().__init__(**Kw)
        self.cor_pena = cor_pena


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, filhote=False, **Kw):

        super().__init__(**Kw)
        self.filhote = filhote


# Instancias
golden = Cachorro(nro_patas=4, cor_pelo="gold", porte="Grande")
print(golden)

corvo = Passaro(nro_patas=2, cor_bico="preto", cor_pena="Preto")
print(corvo)

ornitorrinco = Ornitorrinco(
    nro_patas=4, cor_pelo="Marrom", cor_bico="preto", filhote=True
)
print(ornitorrinco)
