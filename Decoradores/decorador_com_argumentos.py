"""
Neste exemplo, meu_decorador_com_args aceita dois argumentos e retorna o decorador propriamente dito.
O decorador então é aplicado à função minha_funcao.

"""
def meu_decorador_com_args(arg1, arg2):
    def decorador(funcao):
        def funcao_modificada():
            print(f"Argumentos do decorador: {arg1}, {arg2}")
            funcao()
        return funcao_modificada
    return decorador

@meu_decorador_com_args("Olá", "Mundo")
def minha_funcao():
    print("Executando minha função.")

minha_funcao()