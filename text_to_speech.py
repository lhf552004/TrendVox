from gtts import gTTS

def text_to_speech(text, fileName, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save(f"{fileName}.mp3")