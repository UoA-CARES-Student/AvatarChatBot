from cmath import e
from flask import Blueprint, send_from_directory, render_template, jsonify, request

from os import getcwd

def chatbot():

  chatbot = Blueprint(name='chatbot',import_name=__name__, static_folder='templates')
    
  @chatbot.route('/home',methods=['GET'])
  def home():
    return "Hello"


  @chatbot.route('/message',methods=['POST'])
  def message():
    try:
      message = request.form['message']
    except Exception as e:
      print(e)

    return jsonify({
      'video_path' : "/Users/takahiroi/Desktop/AvatarChatBot/ChatBotApp/media/input_videoKennedy.mp4",
      'message' : message,
    }), 200


  return chatbot
