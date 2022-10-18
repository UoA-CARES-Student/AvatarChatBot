from flask import Blueprint, render_template, jsonify, request, send_file, Response
from os import getcwd
import os, re

from .generate_vid import generate_video
from .generator.hparams import hparams as hp


def chatbot():

  speaker_emotion_face = {
    "obama-happy": "ChatBotApp/resources/face/obama/obama_happy.png",
    "obama-neutral": "ChatBotApp/resources/face/obama/obama_neutral.png",
    "obama-sad": "ChatBotApp/resources/face/obama/obama_sad.png"
  }

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

    weight_path = "ChatBotApp/generator/weights/wav2lip_spt_weights.pth"

    response, vid_name = generate_video(message,face_path, audio_path ,weight_path)
    print(response)
    print(response.__class__)
    print("Finihsed processing => ")
    return jsonify({
      "message": response,
      "video_path": vid_name
    }), 200

  @chatbot.route('/message_img2vid',methods=['POST'])
  def message_img2vid():
    try:
      message = request.form['message']
      target_speaker = request.form['speaker']
      emotion = request.form['emotion']

    except Exception as e:
      print(e)

    audio_path = "ChatBotApp/resources/audio/input_audio.wav"

    face_path = speaker_emotion_face[target_speaker+"-"+emotion]

    weight_path = "ChatBotApp/generator/weights/wav2lip_spt_weights.pth"

    response, vid_name = generate_video(message,face_path, audio_path ,weight_path)
    print(response)
    print(response.__class__)
    print("Finihsed processing => ")
    return jsonify({
      "message": response,
      "video_path": vid_name
    }), 200


  @chatbot.after_request
  def after_request(response):
      response.headers.add('Accept-Ranges', 'bytes')
      return response


  def get_chunk(filename, byte1=None, byte2=None):
      full_path = "ChatBotApp/results/" + filename
      file_size = os.stat(full_path).st_size
      start = 0
      
      if byte1 < file_size:
          start = byte1
      if byte2:
          length = byte2 + 1 - byte1
      else:
          length = file_size - start

      with open(full_path, 'rb') as f:
          f.seek(start)
          chunk = f.read(length)
      return chunk, start, length, file_size


  @chatbot.route('/video/<filename>')
  def get_file(filename):
      range_header = request.headers.get('Range', None)
      byte1, byte2 = 0, None
      if range_header:
          match = re.search(r'(\d+)-(\d*)', range_header)
          groups = match.groups()

          if groups[0]:
              byte1 = int(groups[0])
          if groups[1]:
              byte2 = int(groups[1])
        
      chunk, start, length, file_size = get_chunk(filename, byte1, byte2)
      resp = Response(chunk, 206, mimetype='video/mp4',
                        content_type='video/mp4', direct_passthrough=True)
      resp.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))
      return resp


  return chatbot
