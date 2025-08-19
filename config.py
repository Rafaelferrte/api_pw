import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
