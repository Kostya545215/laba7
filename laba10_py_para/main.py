from recognition import Recognizer
from voice import voice
import time
from commands import Command

rec = Recognizer()
text_gen = rec.listen()
rec.stream.stop_stream()
voice.text_to_speech('Привет! Я голосовой ассистент!')
time.sleep(0.5)
rec.stream.start_stream()

for text in text_gen:
    print(text)

    rec.stream.stop_stream()
    Command(text)
    time.sleep(0.5)
    rec.stream.start_stream()