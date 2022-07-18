import bot_api.chat_api.chatbot_api as convo
import bot_api.video_generator.inference as generator
import bot_api.tts.tts as tts


def generate_video(message):
    face_path = "/Users/Goyard/Desktop/python-ws/AvatarChatBot/bot_api/resources/face/input_videoKennedy.mp4"
    input_audio = "bot_api/resources/audio/input_audio.wav"
    weights = "./video_generator/weights/checkpoint_step000363000.pth"
    
    output_file_path = "w"

    response = convo.chat(message)

    tts.generate_audio(response)

    generator.generate(face_path, input_audio, weights)
    return 'results/result_voice_2.mp4'


