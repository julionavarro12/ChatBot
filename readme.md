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

Uma fila é uma estrutura de dados linear que segue o princípio FIFO
(First In, First Out).

Principais operações:
- Enqueue (inserir)
- Dequeue (remover)
- Peek (visualizar o primeiro elemento)

Tecnologias utilizadas

Python 3.10+

Groq API

Modelo LLM: llama-3.1-8b-instant

Estrutura de chatbot com contexto em memória

Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


Instale a dependência:

pip install groq

Configuração da API Key

Crie uma conta gratuita em:
https://console.groq.com

Gere sua API Key e configure no código:

client = Groq(api_key="SUA_API_KEY_AQUI")


Não publique sua API key no GitHub.

Como executar

No terminal, dentro da pasta do projeto:

python chatbot.py


Digite o tema ou pergunta e o chatbot responderá com uma explicação detalhada.
Para encerrar, digite:

sair

Estrutura do projeto
chatbot-estudo
 ├─ chatbot.py
 └─ README.md

Objetivo do projeto

Criar uma ferramenta prática de estudo, aplicando Python e IA generativa, capaz de fornecer explicações organizadas e compreensíveis para qualquer assunto.

Próximas melhorias

Interface web com Streamlit

Exportação das respostas para PDF

Modo quiz e exercícios

Salvamento de histórico

Deploy online