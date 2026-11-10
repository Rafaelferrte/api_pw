# Chat com IA — Flask e Groq

Projeto acadêmico que integra uma aplicação web desenvolvida com Flask à API da Groq para experimentar a comunicação com modelos de inteligência artificial.

## Tecnologias

- Python
- Flask
- Groq API
- python-dotenv
- HTML e CSS

## Estrutura

```text
.
├── app/
│   ├── controllers/
│   ├── models/
│   ├── templates/
│   ├── __init__.py
│   └── routes.py
├── config.py
├── requirements.txt
└── run.py
```

## Pré-requisitos

- Python instalado.
- Uma chave de API da Groq, disponível no site oficial da [Groq](https://groq.com/).

## Como executar

Clone o repositório:

```bash
git clone https://github.com/Rafaelferrte/api_pw.git
cd api_pw
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e adicione sua chave:

```env
GROQ_API_KEY=sua_chave_aqui
```

Inicie a aplicação:

```bash
python run.py
```

## Segurança

Não compartilhe sua chave de API nem envie o arquivo `.env` para o GitHub. Utilize variáveis de ambiente para manter credenciais fora do código-fonte.

## Objetivo acadêmico

Praticar integração entre aplicações Python, frameworks web e serviços de IA por meio de uma API externa.
