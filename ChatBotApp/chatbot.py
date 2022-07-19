from flask import Blueprint, render_template, jsonify, request, send_file
from os import getcwd

from .generate_vid import generate_video
from .generator.hparams import hparams as hp


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

    audio_path = "ChatBotApp/resources/audio/input_audio.wav"

    face_path = "ChatBotApp/resources/face/input_videoMonaLisa.mp4"

    weight_path = "/home/tish386/EmoFaceGeneration/emofacegeneration/checkpoints/attension_v6_jul_15/checkpoint_step000123367.pth"

    response = generate_video(message,face_path, audio_path ,weight_path)
    print(response)
    print(response.__class__)
    print("Finihsed processing => ")
    return jsonify({
      "message": response
      # "video_path": "/home/tish386/AvatarChatBot/ChatBotApp/results/result_voice.mp4"
    }), 200

  return chatbot
