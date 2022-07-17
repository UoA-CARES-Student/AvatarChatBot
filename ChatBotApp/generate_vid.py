import chat_api.chatbot_api as convo
import generator.inference as generator
import tts.tts as tts



def generate_video(message):
    face_path = "./faces/input_videoKennedy.mp4"
    input_audio = "./audio/input_audio.wav"
    weights = "./generator/weights/checkpoint_step000363000.pth"

    response = convo.chat(message)

    tts.generate_audio(response)

    generator.generate(face_path, input_audio, weights)
    

if __name__ == '__main__':
	generate_video("what's your favourite animal?")



