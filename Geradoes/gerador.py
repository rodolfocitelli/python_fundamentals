"""
Exemplo: meu_gerador()

1 - meu_gerador(numeros): Esta função recebe uma lista de números inteiros (numeros) como entrada.
2 - for num in numeros: O loop for itera sobre cada número na lista numeros.
3 - yield num**2: A palavra-chave yield é o que transforma uma função em um gerador. 
    Em vez de retornar o valor calculado (num**2), yield "produz" esse valor e pausa a execução da função. 
    O valor produzido pode ser acessado através de um iterador.
4 - for i in meu_gerador(...): Este loop for itera sobre os valores gerados por meu_gerador. 
    A cada iteração, meu_gerador é retomado, calcula o próximo valor (num**2) e o produz. O loop for então imprime esse valor.

"""


def meu_gerador(numeros: list[int]):
    for num in numeros:
        yield num**2

for i in meu_gerador(numeros = list(range(1,101))):
    print(i)