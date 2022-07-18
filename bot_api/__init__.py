import os

from flask import Flask
from bot_api.chatbot_blueprint_gen import create_chatbot_blueprint
from dotenv import load_dotenv


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    load_dotenv()
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    app.register_blueprint(create_chatbot_blueprint(), url_prefix='/v1/chatbot')
    
    return app
