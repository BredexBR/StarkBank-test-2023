# StarkBank-test-2023

## Introdução
O projeto proposto foi um desafio da Starkbank que consiste em um programa que vai enviar de 8 a 12 faturas, a cada 3 horas, para pessoas aleatórias durante 24 horas. Posteriormente, receber os créditos da fatura e enviar para uma conta por uma transferência. Disponibilizando um ambiente sandbox para o consumo de sua API.

A proposta foi realizada com o [Visual Studio Code](https://code.visualstudio.com/download) e, para organização das pastas e códigos, foi utilizada a [Arquitetura Hexagonal](https://engsoftmoderna.info/artigos/arquitetura-hexagonal.html#:~:text=Os%20objetivos%20de%20uma%20Arquitetura,mais%20f%C3%A1ceis%20de%20serem%20testados.). 

## Bibliotecas/Ferramentas
Foi necessário baixar a ferramenta [ngrok](https://ngrok.com/).

A biblioteca flask:
> $ pip install flask

E também a biblioteca psycopg2:
> $ pip install psycopg2

## Configurações
Seguindo o caminho /src/Infrastructure/server.py 
Existe uma variável que deve ser armazenada a chave privada. A API fornece algumas soluções. [Clique aqui](https://starkbank.com/faq/how-to-create-ecdsa-keys) caso tenha curiosidade.
> private_key_content = """ Informação da chave privada """

Precisara do id do projeto criado dentro do ambiente sandbox
> id="id do ambiente sandbox"

Seguindo o caminho /src/Application/checkWebHook.py
Precisara do id do webhook criado dentro do ambiente sandbox
> webHookSandbox = "id do webhook sandbox"

Seguindo o caminho /src/Infrastructure/conDatabase.py sera necessário configurar as informações para conexão em seu banco de dados(postgres). No projeto para a criação da tabela sql foi utilizado o [railway](https://railway.app/)(banco de dados na nuvem e muitas outras coisas). [clique aqui](https://docs.railway.app/) caso tenha interesse em ler a documentação deles.

Criar uma tabela(table) chamada people com 3 colunas id(int), name(text), cpf(text) e adicionar 12 linhas(rows). OBS: precisam ser cpf's validos.

Entretanto caso não queira utilizar um banco de dados existe outra opção:
primeiramente em /src/Adapters/invoiceController.py retire as seguintes linhas de código:
> conn = conDatabase.conDatabase()

> if conn != "erro":

> conDatabase.closeDatabase(conn)

> else:

> print("Não foi possível realizar a conexão com o banco de dados")

Após entrar em /src/Application/addInvoice.py trocar linha de código:
> people = addPeopleDatabase.addPeopleDatabase(conn, numberRandom)

Por
> people = addPeople.addPeople(numberRandom)

## Executando o projeto
Inicie o ngrok dentro de sua respectiva pasta
> $ ngrok/ngrok.exe http 5000

Execute o projeto entrando na pasta src. Basta inserir no terminal:
> $ cd .\src\
> $ python main.py
