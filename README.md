# StarkBank-test-2023

## Introdução
O projeto proposto foi um desafio da Starkbank que consiste em um programa que vai enviar de 8 a 12 faturas, a cada 3 horas, para pessoas aleatórias durante 24 horas. Posteriormente, receber os créditos da fatura e enviar para uma conta por uma transferência. Disponibilizando um ambiente sandbox para o consumo de sua API.

A proposta foi realizada com o [Visual Studio Code](https://code.visualstudio.com/download) e, para organização das pastas e códigos, foi utilizada a [Arquitetura Hexagonal](https://engsoftmoderna.info/artigos/arquitetura-hexagonal.html#:~:text=Os%20objetivos%20de%20uma%20Arquitetura,mais%20f%C3%A1ceis%20de%20serem%20testados.). 

## Bibliotecas/Ferramentas
Foi necessário baixar a ferramenta [ngrok](https://ngrok.com/).

E também a biblioteca flask:
> $ pip install flask

## Configurações
Seguindo o caminho /src/Infrastructure/server.py 
Existe uma variável que deve ser armazenada a chave privada. A API fornece algumas soluções. [Clique aqui](https://starkbank.com/faq/how-to-create-ecdsa-keys) caso tenha curiosidade.
> private_key_content = """ Informação da chave privada """

Precisara do id do projeto criado dentro do ambiente sandbox
> id="id do ambiente sandbox"

Seguindo o caminho /src/Application/checkWebHook.py
Precisara do id do webhook criado dentro do ambiente sandbox
> webHookSandbox = "id do webhook sandbox"

## Executando o projeto
Inicie o ngrok dentro de sua respectiva pasta
> $ ngrok/ngrok.exe http 5000

Execute o projeto entrando na pasta src. Basta inserir no terminal:
> $ cd .\src\
> $ python main.py
