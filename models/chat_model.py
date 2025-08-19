from groq import Groq
from config import GROQ_API_KEY

# Modelo = comunicação com a API da Groq
class ChatModel:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def get_response(self, user_input):
        response = self.client.chat.completions.create(
            model="llama3-8b-8192",  # você pode trocar para "llama3-70b-8192"
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
