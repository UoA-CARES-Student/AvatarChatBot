import os
from dotenv import load_dotenv
from flask import Flask
from chatbot_server.chatbot import chatbot

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    load_dotenv()
    
    app.register_blueprint(chatbot(), url_prefix='/v1/chatbot')
    
    return app
