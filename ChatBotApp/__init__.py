import os

from flask import Flask
from ChatBotApp.chatbot import chatbot

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    app.register_blueprint(chatbot(), url_prefix='/v1/chatbot')
    
    return app
