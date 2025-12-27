# Chatbot de Estudo com IA (Groq + Python)

Este projeto é um chatbot de estudo desenvolvido em Python utilizando a API do Groq e um modelo LLM gratuito.  
O chatbot fornece explicações claras, organizadas e didáticas sobre diferentes matérias e temas de estudo.

---

## Funcionalidades

- Explica qualquer tema ou pergunta de estudo  
- Gera respostas claras e estruturadas  
- Mantém o contexto da conversa  
- Funciona via terminal (CLI)  
- Utiliza apenas modelos gratuitos do Groq  

---

## Exemplo de uso

**Pergunta:**  
Explique como funciona a fila em estrutura de dados

**Resposta (exemplo):**  
Uma fila é uma estrutura de dados linear que segue o princípio FIFO (First In, First Out).

Principais operações:

- Enqueue (inserir)  
- Dequeue (remover)  
- Peek (visualizar o primeiro elemento)  

---

## Tecnologias utilizadas

- Python 3.10+  
- Groq API  
- Modelo LLM: llama-3.1-8b-instant  
- Estrutura de chatbot com contexto em memória  

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instale as dependências:


pip install groq python-dotenv
Configuração da API Key
Crie um arquivo .env na raiz do projeto:


GROQ_API_KEY=SUA_API_KEY_AQUI
No seu código (chatbot.py), use:

python
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
Não publique sua API key no GitHub. Adicione .env ao .gitignore:


.env
Como executar
No terminal, dentro da pasta do projeto:

bash
python chatbot.py
Digite o tema ou pergunta e o chatbot responderá com uma explicação detalhada.
Para encerrar, digite:



Estrutura do projeto
Copiar código
chatbot-estudo
 ├─ chatbot.py
 ├─ .gitignore
 └─ README.md
Objetivo do projeto
Criar uma ferramenta prática de estudo, aplicando Python e IA generativa, capaz de fornecer explicações organizadas e compreensíveis para qualquer assunto.
