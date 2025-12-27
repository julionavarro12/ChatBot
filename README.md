Chatbot de Estudo com IA (Groq + Python)

Este projeto é um chatbot de estudo desenvolvido em Python utilizando a API do Groq e um modelo LLM gratuito.
O chatbot fornece explicações claras, organizadas e didáticas sobre diferentes matérias e temas de estudo.

Funcionalidades

Explica qualquer tema ou pergunta de estudo

Gera respostas claras e estruturadas

Mantém o contexto da conversa

Funciona via terminal (CLI)

Utiliza apenas modelos gratuitos do Groq

Exemplo de uso

Pergunta:
Explique como funciona a fila em estrutura de dados

Resposta (exemplo):
Uma fila é uma estrutura de dados linear que segue o princípio FIFO (First In, First Out).

Principais operações:

Enqueue (inserir)

Dequeue (remover)

Peek (visualizar o primeiro elemento)

Tecnologias utilizadas

Python 3.10+

Groq API

Modelo LLM: llama-3.1-8b-instant

Estrutura de chatbot com contexto em memória

Instalação

Para instalar o projeto, primeiro clone o repositório do GitHub e entre na pasta do projeto.
Depois, instale as dependências groq e python-dotenv usando o pip.

Configuração da API Key

Crie um arquivo chamado .env na raiz do projeto e adicione a sua API Key do Groq na variável GROQ_API_KEY.

No código do chatbot, use a biblioteca dotenv para ler a variável de ambiente e inicializar o cliente Groq com a chave.

Não publique a API Key no GitHub e adicione o arquivo .env ao .gitignore.

Como executar

No terminal, dentro da pasta do projeto, execute o script chatbot.py.
Digite o tema ou pergunta para receber a explicação.
Para encerrar, digite sair.

Estrutura do projeto

O projeto possui a seguinte estrutura:

chatbot.py

.gitignore

README.md

Objetivo do projeto

Criar uma ferramenta prática de estudo, aplicando Python e IA generativa, capaz de fornecer explicações organizadas e compreensíveis para qualquer assunto.
