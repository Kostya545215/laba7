from voice import voice
from handlers import thanks, close, back, activities, view, weather, favorite_city

COMMANDS = [
    {'id' : 0, 'text' : 'спасибо', 'handler': thanks},
    {'id' : 1, 'text' : 'погода', 'handler': weather},
    {'id' : 2, 'text' : 'любимый город', 'handler': favorite_city},
    {'id' : 3, 'text' : 'активности', 'handler': activities},
    {'id' : 4, 'text' : 'красивый вид', 'handler': view},
    {'id' : 5, 'text' : 'закрой', 'handler': close},
    {'id' : 6, 'text' : 'верни', 'handler': back}
]

ACTIVATION = 'джек'

class Command:
    def __init__(self, text):
        self.text = text
        self.map()

    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION,"").strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Я не знаю такой команды')
    
    def run(self, cmd):
        handler = cmd['handler']
        handler(self.text)

