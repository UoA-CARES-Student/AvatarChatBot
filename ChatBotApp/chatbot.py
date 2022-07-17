from flask import Blueprint, send_from_directory

from os import getcwd

def chatbot():
  
  chatbot = Blueprint(name='chatbot',import_name=__name__, static_folder='templates')
  
  path_to_home_page = 'templates/home.html'
  
  @chatbot.route('/home',methods=['GET'])
  def home():
    print(getcwd())
    return send_from_directory(chatbot.static_folder, 'home.html')

  return chatbot
