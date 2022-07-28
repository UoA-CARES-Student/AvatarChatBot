import chatbot_server.chat_api.chatbot_api as convo
import chatbot_server.generator.inference as generator
import chatbot_server.tts.tts as tts



def generate_video(message, face_path, input_audio, weights):
    # face_path = "./faces/input_videoKennedy.mp4"
    # input_audio = "./audio/input_audio.wav"
    # weights = "./generator/weights/checkpoint_step000363000.pth"

    response = convo.chat(message)

    tts.generate_audio(response)

    vid_name = generator.generate(face_path, input_audio, weights)


    return response, vid_name
