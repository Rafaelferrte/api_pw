from flask import render_template, request
from models.chat_model import ChatModel

chat_model = ChatModel()

def index():
    response = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            response = chat_model.get_response(user_input)
    return render_template("index.html", response=response)
