# api_pw

# ChatGPT Flask com Groq

Este é um projeto simples usando **Flask** e a **API da Groq** para integrar uma IA em um site.

## 🚀 Como rodar

1. Clone o repositório, crie um ambiente virtual, instale as dependências, configure a chave da Groq e rode o projeto:

```bash
git clone https://github.com/Rafaelferrte/api_pw.git
cd api_pw
python -m venv venv
source venv/bin/activate   # no Windows use: venv\Scripts\activate
pip install -r requirements.txt
echo "GROQ_API_KEY=sua_chave_aqui" > .env
python run.py

📂 Estrutura do projeto

app/
 ├── controllers/
 ├── models/
 ├── templates/
 ├── __init__.py
 └── routes.py
run.py
requirements.txt
config.py

🛠️ Tecnologias

Python + Flask
Groq API
HTML + CSS
