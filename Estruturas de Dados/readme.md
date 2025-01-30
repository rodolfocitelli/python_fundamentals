# Resumo sobre Estruturas de Dados e Funções em Python

## 1. Listas

* **O que são:** Coleções ordenadas e mutáveis de itens.
* **Como criar:** `minha_lista = [1, 2, "texto", 3.14]`
* **Características:**
    * Itens podem ser de tipos diferentes.
    * A ordem dos itens é preservada.
    * Você pode adicionar, remover ou alterar itens.
* **Exemplo:** `minha_lista.append(5)` adiciona o número 5 ao final da lista.

## 2. Tuplas

* **O que são:** Coleções ordenadas e imutáveis de itens.
* **Como criar:** `minha_tupla = (1, 2, "texto", 3.14)`
* **Características:**
    * Semelhantes às listas, mas não podem ser modificadas após a criação.
    * Úteis para representar dados que não devem ser alterados.
* **Exemplo:** `minha_tupla[0]` acessa o primeiro item da tupla (índice 0).

## 3. Dicionários

* **O que são:** Coleções de pares chave-valor, onde cada chave é única e está associada a um valor.
* **Como criar:** `meu_dicionario = {"nome": "Alice", "idade": 30}`
* **Características:**
    * Os valores são acessados pelas chaves, não por índices.
    * Flexíveis para armazenar dados relacionados.
* **Exemplo:** `meu_dicionario["nome"]` retorna o valor "Alice".

## 4. Conjuntos (Sets)

* **O que são:** Coleções não ordenadas de itens únicos.
* **Como criar:** `meu_conjunto = {1, 2, 3, 3}` (o número 3 repetido será ignorado)
* **Características:**
    * Itens duplicados são removidos automaticamente.
    * Úteis para verificar se um elemento pertence a um grupo.
* **Exemplo:** `2 in meu_conjunto` retorna `True`.

## 5. Funções

* **O que são:** Blocos de código reutilizáveis que executam tarefas específicas.
* **Como definir:**
    ```python
    def minha_funcao(parametro1, parametro2):
        # Código da função
        return resultado
    ```
* **Como usar:** `minha_funcao(valor1, valor2)`
* **Características:**
    * Podem receber parâmetros (entradas) e retornar valores (saídas).
    * Ajudam a organizar o código e evitar repetição.

## Exemplo prático

```python
def calcular_media(lista_numeros):
  total = sum(lista_numeros)
  media = total / len(lista_numeros)
  return media

notas = [8, 7, 9, 6]
media_notas = calcular_media(notas)
print(f"A média das notas é: {media_notas}")
````
## Recursos adicionais
* Se precisar de mais detalhes ou exemplos, consulte a documentação oficial do Python: https://python.org.br/
* Explore tutoriais e cursos online para aprofundar seus conhecimentos.
