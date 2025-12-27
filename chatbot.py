from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

contexto = [
    {
        "role": "system",
        "content": "Você é um assistente de estudo que explica qualquer assunto com clareza e organização."
    }
]

def gerar_resposta(pergunta):
    contexto.append({"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=contexto
    )

    texto = resposta.choices[0].message.content
    contexto.append({"role": "assistant", "content": texto})

    return texto

if __name__ == "__main__":
    while True:
        pergunta = input("Digite o tema ou pergunta (ou 'sair'): ")

        if pergunta.lower() == "sair":
            print("Até mais! Bons estudos!")
            break

        resposta = gerar_resposta(pergunta)

        print("\n--- Resposta do ChatBot ---\n")
        print(resposta)
        print("\n---------------------------\n")
