## Programação orientada a objetos com Python

A Programação Orientada a Objetos (POO) é um paradigma de programação que permite organizar o código em torno de "objetos", 
que combinam dados e funcionalidades. Em Python, a POO é amplamente utilizada devido à sua flexibilidade e escalabilidade.

### Principais conceitos da POO em Python

1.  **Classes:** São moldes para criar objetos. Definem os atributos (dados) e métodos (funções) que os objetos terão.
2.  **Objetos:** São instâncias de classes. Cada objeto tem seus próprios valores para os atributos e pode executar os métodos definidos na classe.
3.  **Atributos:** São variáveis que armazenam os dados de um objeto.
4.  **Métodos:** São funções que definem o comportamento de um objeto.
5.  **Encapsulamento:** Agrupa os dados e métodos relacionados em um objeto, protegendo os dados de acesso externo e permitindo o controle sobre sua manipulação.
6.  **Herança:** Permite que classes herdem atributos e métodos de outras classes, promovendo a reutilização de código e a organização hierárquica das classes.
7.  **Polimorfismo:** Permite que objetos de diferentes classes sejam tratados de forma uniforme através de uma interface comum.

### Exemplo de POO em Python

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_informacoes()
