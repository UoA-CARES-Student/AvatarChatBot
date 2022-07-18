from google.cloud import texttospeech


def generate_audio(speech_text, lang_code = "en-US", voice_name = 'en-US-Wavenet-D'):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text = speech_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    #voice = texttospeech.VoiceSelectionParams(
    #   language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
    #)

    voice = texttospeech.VoiceSelectionParams(
        language_code= lang_code, 
        name= voice_name
    )
    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    import os
    print(os.getcwd())
    with open("bot_api/resources/audio/input_audio.wav", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "input_audio.wav"')