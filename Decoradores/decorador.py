"""
Neste exemplo:

* meu_decorador é o decorador. Ele recebe uma função como argumento (funcao) e define 
  uma nova função (funcao_modificada) que envolve a função original.

* funcao_modificada imprime uma mensagem antes e depois de chamar a função original.

* @meu_decorador é a sintaxe para aplicar o decorador meu_decorador à função minha_funcao. 

* Isso é equivalente a fazer minha_funcao = meu_decorador(minha_funcao).
  Quando você chama minha_funcao(), o decorador é executado, e você vê a seguinte saída:

"Antes da execução da função original."
"Executando minha função."
"Depois da execução da função original."
"""

def meu_decorador(funcao):
    def funcao_modificada():
        print("Antes da execução da função original.")
        funcao()
        print("Depois da execução da função original.")
    return funcao_modificada

@meu_decorador
def minha_funcao():
    print("Executando minha função.")

minha_funcao()

"""
COMO FUNCIONA:

1 - Definição do decorador: O decorador é uma função que aceita outra função como argumento e retorna uma nova função.
2 - Aplicação do decorador: A sintaxe @nome_do_decorador acima de uma função aplica o decorador a essa função.
3 - Execução da função decorada: Quando a função decorada é chamada, o decorador é executado, 
    e a nova função (retornada pelo decorador) é quem realmente é executada.
"""
