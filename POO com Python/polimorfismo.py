"""
O código demonstra o conceito de polimorfismo em Python através de classes e um método. Vamos analisar:

Classes:

Passaro: Classe base com o método voar() que retorna "Voando ...".
Pardal: Herda de Passaro e sobrescreve o método voar() para retornar o mesmo que a classe mãe, usando super().voar().
Avestruz: Herda de Passaro e sobrescreve o método voar() para retornar "Avestruz não pode voar".

Método:

plano_voo(obj): Aceita um objeto como argumento e chama o método voar() desse objeto.

Instâncias:

p1: Instância da classe Pardal.
p2: Instância da classe Avestruz.

Execução:

plano_voo(p1): Chama o método voar() do objeto p1 (Pardal), que retorna "Voando ...".
plano_voo(p2): Chama o método voar() do objeto p2 (Avestruz), que retorna "Avestruz não pode voar".

Polimorfismo em ação:

O polimorfismo permite que o método plano_voo() funcione com diferentes tipos de objetos (Pardal e Avestruz), 
sem precisar verificar o tipo específico. Cada objeto responde ao método voar() de sua maneira específica,
demonstrando o conceito de "muitas formas" do polimorfismo.

Em resumo, o polimorfismo torna o código mais flexível e reutilizável, 
permitindo que objetos de diferentes classes sejam tratados de forma uniforme através de interfaces comuns
"""

# Classes 

class Passaro:
    def voar(self):
        return "Voando ..."
    
class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        return "Avestruz não pode voar"
    

# Método - Exemplo de polimorfismo

def plano_voo(obj):
    return obj.voar()


# Instâncias

p1 = Pardal()
p2 = Avestruz()


# Execução

print(plano_voo(p1))
print(plano_voo(p2))

