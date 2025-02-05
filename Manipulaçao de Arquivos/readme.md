## Manipulações de arquivos TXT, CSV e JSON em Python

Python oferece diversas ferramentas e módulos para manipular arquivos de diferentes formatos, incluindo TXT, CSV e JSON.

## Arquivos TXT

* Leitura: Utilize a função **`open()`** com o modo **`"r"`** para abrir o arquivo e os métodos **`read()`**, **`readline()`** ou **`readlines()`** para ler o conteúdo.
* Escrita: Utilize a função **`open()`** com o modo **`"w"`** para criar um novo arquivo ou **`"a"`** para adicionar conteúdo a um arquivo existente.
  Utilize o método **`write()`** para escrever o conteúdo.

## Arquivos CSV

* Leitura: Utilize o módulo csv com a função **`reader()`** para ler o arquivo linha por linha.
* Escrita: Utilize o módulo csv com a função **`writer()`** para escrever os dados no arquivo.

Arquivos JSON:

* Leitura: Utilize o módulo json com a função **`load()`** para carregar o arquivo JSON como um objeto Python.
* Escrita: Utilize o módulo json com a função **`dump()`** para escrever um objeto Python em um arquivo JSON.

## Dicas

* Utilize o gerenciador de contexto with open(...) para garantir que o arquivo seja fechado automaticamente após o uso.
* Especifique a codificação do arquivo (ex: UTF-8) ao abrir para evitar erros de caracteres.
* Utilize bibliotecas como pandas para realizar operações mais complexas em arquivos CSV e JSON.
