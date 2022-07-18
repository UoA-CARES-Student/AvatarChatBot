from flask import Blueprint, render_template, jsonify, request, send_file

from os import getcwd
from bot_api.generate_vid import generate_video

def create_chatbot_blueprint():
  
  chatbot = Blueprint(name='chatbot',import_name=__name__, static_folder='templates')
    
  @chatbot.route('/home',methods=['GET'])
  def home():
    return "Hello"


  @chatbot.route('/message',methods=['POST'])
  def message():
    try:
      message = request.form['message']
    except Exception as error:
      print(error)

    output_file_path = generate_video(message)
    
    return jsonify({
      "message": message,
      "video_path": output_file_path,
    }), 200

  return chatbot


