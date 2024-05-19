# python -m venv ./venv
# source venv/bin/activate
#pip install playsound

from vosk_tts import Model, Synth
from playsound import playsound

class Voice:
    def __init__(self):
        model = Model(model_name="vosk-model-tts-ru-0.6-multi")
        self.synth = Synth(model)
        self.speaker = 4

    def text_to_speech(self, text = 'Добрый день!'):
        self.synth.synth(text, 
                         "out.wav", #формат для звукового файла. был mp3
                         speaker_id = self.speaker)
        playsound('out.wav')

    def set_voice(self, speaker):
        self.speaker = speaker  # поле экземпляра класса 

voice = Voice()

if __name__ == '__main__':
    voice = Voice()
    voice.text_to_speech()
    