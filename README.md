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

Se você quiser, posso agora escrever uma versão ainda mais enxuta e visualmente limpa, perfeita para GitHub, que destaca funcionalidades e uso sem poluir o README. Quer que eu faça isso?

agora eu quero subir esse cod no github, mas eu nao tenho repositorio criado 

Beleza! Vou te guiar passo a passo para criar um repositório no GitHub e subir seu código, mesmo que você nunca tenha feito isso antes.

1️⃣ Criar um repositório no GitHub

Acesse: https://github.com

Faça login na sua conta (ou crie uma gratuita).

No canto superior direito, clique em “+” → New repository.

Preencha:

Repository name: chatbot-estudo (ou outro nome que preferir)

Description: Chatbot de estudo com IA usando Groq

Visibility: escolha Public se quiser compartilhar, ou Private se for só para você

Marque a opção “Add a README file” se quiser já criar um README inicial (opcional, você pode substituir depois).

Clique em Create repository

Agora você tem um repositório vazio no GitHub.

2️⃣ Preparar seu projeto localmente

No seu computador, na pasta do projeto (chatbot-estudo), abra o terminal e execute:

git init


Isso inicializa o Git na pasta.

Adicionar arquivos e commit inicial
git add .
git commit -m "Primeiro commit - chatbot de estudo"


git add . → adiciona todos os arquivos do projeto

git commit -m "mensagem" → cria um snapshot do projeto

3️⃣ Conectar com o repositório do GitHub

No GitHub, na página do seu repositório, você verá instruções parecidas com estas:

git remote add origin https://github.com/seu-usuario/chatbot-estudo.git
git branch -M main
git push -u origin main


git remote add origin ... → conecta seu projeto local ao repositório no GitHub

git branch -M main → define a branch principal como main

git push -u origin main → envia todos os arquivos para o GitHub

4️⃣ Confirmar que deu certo

Vá para o seu repositório no GitHub

Atualize a página

Você verá todos os arquivos do seu projeto lá (chatbot.py, README.md, etc.)
