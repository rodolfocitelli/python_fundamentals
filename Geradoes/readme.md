## Entendendo Geradores em Python
Geradores em Python são como funções especiais que retornam uma sequência de valores, um de cada vez, 
em vez de calcular todos os valores de uma vez e armazená-los na memória. 
Isso os torna muito eficientes para trabalhar com grandes conjuntos de dados, 
pois economizam memória e podem ser interrompidos e retomados a qualquer momento.

## Benefícios de usar geradores
* Economia de memória: Geradores produzem valores sob demanda, evitando carregar todos os dados na memória de uma vez.
* Eficiência: O processamento é feito em partes, o que pode ser mais rápido para grandes conjuntos de dados.
* Flexibilidade: Geradores podem ser interrompidos e retomados, permitindo o processamento parcial dos dados.

## Quando usar geradores
* Trabalhar com arquivos muito grandes que não cabem na memória.
* Processar dados em streaming, onde os dados chegam um de cada vez.
* Implementar algoritmos que precisam gerar uma sequência infinita de valores.
