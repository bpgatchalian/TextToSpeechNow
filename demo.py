import os
from openai import OpenAI 
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class TextToSpeechNow:

    def __init__(
            self, 
            tts_engine="google_tts",
            language="en",
            model="tts-1",
            voice="nova",
            ):
        self.tts = TTSEngine()
        self.tts_engine = tts_engine
        self.language=language
        self.model=model
        self.voice=voice
                
    def synthesize_text(self, text, output_path):
        self.tts.tts(
            tts_engine=self.tts_engine,
            text_to_speak=text, 
            language=self.language,
            model=self.model,
            voice=self.voice,
            output_path=output_path
            )
    
    def speak(self, text):
        output_path = f"speech_{datetime.now():%Y%m%d_%H%M%S}.mp3"
        self.synthesize_text(text=text,output_path=output_path)
        self.play_audio(audio_file=output_path)

    def play_audio(self, audio_file):
        playsound(audio_file)
        os.remove(audio_file)

class TTSEngine:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.openai_api_key)

    def tts(self, tts_engine, text_to_speak, language, model, voice, output_path):
        if tts_engine == 'google_tts':
            self.google_tts(text_to_speak, language, output_path)
        elif tts_engine =='openai_tts':
            self.openai_tts(text_to_speak, model, voice, output_path)

    def google_tts(self, text_to_speak, language, output_path):

        gtts_obj = gTTS(text=text_to_speak, lang=language)

        audio_file = output_path
        gtts_obj.save(audio_file)

    def openai_tts(self, text_to_speak, model, voice, output_path):

        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=text_to_speak
        )
        
        with open(output_path, 'wb') as file:
            file.write(response.content)

if __name__ == '__main__':

    tts_now = TextToSpeechNow()
    tts_now.speak("Hello, welcome to TextToSpeechNow.")