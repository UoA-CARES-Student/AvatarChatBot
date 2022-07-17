from cmath import e
from flask import Blueprint, render_template, jsonify, request, send_file

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
      "message": message,
      "video_path": "/videos/input_videoKennedy.mp4"
    }), 200

  return chatbot
