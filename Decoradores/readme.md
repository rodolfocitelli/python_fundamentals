# Decoradores em Python

## O que são decoradores?
Decoradores são uma forma de modificar o comportamento de funções ou métodos sem alterar seu código diretamente. 
Eles são comumente usados para adicionar funcionalidades como logging, controle de acesso, caching, entre outros.

## Como funcionam
* Definição: Um decorador é uma função que recebe outra função como argumento e retorna uma nova função (a função "envolvida").
* Aplicação: O decorador é aplicado à função que se deseja modificar usando o símbolo @ seguido do nome do decorador, 
  logo antes da definição da função.
* Execução: Quando a função decorada é chamada, o decorador é executado, adicionando as funcionalidades 
  extras definidas na função "envolvida".

## Vantagens
* Reutilização de código: Evita a repetição de trechos de código que são usados em várias funções.
* Organização: Mantém o código mais limpo e modular, separando as responsabilidades de cada função.
* Legibilidade: Facilita a compreensão do código, pois as funcionalidades extras ficam separadas da lógica principal da função.

## Exemplos de uso
* Logging: Registrar informações sobre a execução da função, como os argumentos e o tempo de execução.
* Medição de tempo: Calcular o tempo gasto para executar uma função.
* Verificação de acesso: Garantir que apenas usuários autorizados possam executar determinadas funções.
* Tratamento de erros: Lidar com exceções que possam ocorrer durante a execução da função.

## Conclusão
Os decoradores são uma ferramenta poderosa do Python que permitem modificar funções de forma elegante e reutilizável. 
Eles são amplamente usados em frameworks como Flask e Django para manipulação de rotas e permissões, entre outras funcionalidades.
