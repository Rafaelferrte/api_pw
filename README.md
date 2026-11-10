# Chat com IA — Flask e Groq

Aplicação web acadêmica que integra Flask à API da Groq para enviar perguntas a um modelo de linguagem e exibir as respostas em uma interface de chat.

## Funcionalidades

- Interface web para enviar perguntas.
- Processamento das mensagens por uma aplicação Flask.
- Integração com a API da Groq.
- Exibição da resposta gerada pelo modelo na página.

## Tecnologias

- Python
- Flask
- Groq Python SDK
- python-dotenv
- HTML e Tailwind CSS

## Estrutura do projeto

```text
.
├── controllers/
│   └── chat_controller.py
├── models/
│   └── chat_model.py
├── views/
│   └── templates/
│       └── index.html
├── app.py
├── config.py
└── requirements.txt
```

## Pré-requisitos

- Python 3 instalado.
- Uma chave de API da Groq, disponível em [console.groq.com](https://console.groq.com/).

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

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

Inicie a aplicação:

```bash
python app.py
```

Abra o endereço local exibido pelo Flask no terminal.

## Segurança

- Não compartilhe sua chave de API nem envie o arquivo `.env` ao GitHub.
- O modo de depuração do Flask está habilitado no código atual para desenvolvimento. Não utilize essa configuração em produção.
- Para aplicações reais, trate erros da API e valide os dados recebidos do formulário.

## Objetivo acadêmico

Praticar a integração de uma aplicação Python com um serviço de IA, utilizando organização em camadas simples (controllers e models) e renderização de templates.
