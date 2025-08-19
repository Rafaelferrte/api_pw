from flask import Flask
from controllers.chat_controller import index
import os

# Dizendo onde está a pasta de templates
app = Flask(__name__, template_folder=os.path.join("views", "templates"))

# Rotas
app.add_url_rule("/", view_func=index, methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True)
