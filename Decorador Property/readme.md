## Decorador @property em Python

O decorador **`@property`** em Python é uma ferramenta poderosa que permite criar propriedades gerenciadas em suas classes. 
Essas propriedades se comportam como atributos normais, mas oferecem controle e flexibilidade adicionais sobre como os dados 
são acessados e modificados.

## Como funciona

* **`@property`** (Getter): Transforma um método em um "getter", permitindo acessar o valor do atributo
  como se fosse um atributo normal (pessoa.nome).

* **`@nome.setter`** (Setter): Define um método "setter", que é chamado quando tentamos atribuir
  um novo valor ao atributo (**`pessoa.nome = "Novo Nome"`**). Aqui, podemos adicionar validações e lógica
  personalizada antes de modificar o valor.

* **`@nome.deleter`** (Deleter): Define um método "deleter", que é chamado quando usamos o operador del
  para tentar apagar o atributo (del pessoa.nome).

## Vantagens de usar @property

* Encapsulamento: Permite esconder a implementação interna dos atributos, expondo apenas uma interface limpa e controlada.
* Validação de dados: Podemos adicionar regras nos setters para garantir que os atributos recebam valores válidos.
* Flexibilidade: Podemos adicionar lógica personalizada nos getters e setters, como cálculos ou formatação de dados.
* Código mais legível: Acessar um atributo usando **`@property`** é tão simples quanto acessar um atributo normal,
  tornando o código mais intuitivo.

## Exemplo:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome não pode ser vazio")
        self._nome = nome

pessoa = Pessoa("Maria")
print(pessoa.nome)  # Acessa o getter
pessoa.nome = "José"  # Acessa o setter
print(pessoa.nome)
del pessoa.nome # Acessa o deleter (se definido)
```
# Resumo

O decorador **`@property`** em Python é uma ferramenta essencial para criar atributos gerenciados, oferecendo mais controle e 
flexibilidade do que os atributos normais. Com ele, você pode adicionar validação, lógica personalizada e encapsulamento 
aos seus atributos, tornando seu código mais robusto e fácil de manter.
