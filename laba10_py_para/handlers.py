import random
import webbrowser
import pyautogui
from num2words import num2words as nw

from recognition import Recognizer
from voice import voice
from weather import weather_check

def options(list_of_options):
    sel = random.choice(list_of_options)
    voice.text_to_speech(sel)

def thanks(text):
    options(['Было несложно', 'Пожалуйста', 'Обращайтесь'])

def view(text):
    voice.text_to_speech('Наслаждайтесь!')
    webbrowser.open('https://yandex.ru/images/search?from=tabbar&text=красивые%20вид')

def favorite_city(text):
    voice.text_to_speech('Спасибо, что спросили. Мой любимый город это')
    options(['Москва', 'Рим', 'Токио', 'Париж', 
                            'Лондон', 'Нью-Йорк', 'Стамбул', 'Барселона', 'Пекин', 'Дубай', 'Дели', 
                            'Рио-де-Жанейро', 'Кейптаун', 'Сидней', 'Буэнос-Айрес']) 
    voice.text_to_speech('А моя любимая страна это ')
    options(['Россия', 'Италия', 'Япония', 'Франция', 'Великобритания', 'США', 'Турция', 'Испания',
            'Китай', 'Объединённые Арабские Эмираты', 'Индия', 'Бразилия', 'ЮАР', 'Австралия', 'Аргентина'])

def weather(text):
    rec = Recognizer()
    text_gen = rec.listen()
    time, precipitation, weather, wind_speed = weather_check(text.split()[-1] + 'погода')
    voice.text_to_speech(f'Время в {text.split()[-1]}, осадки, температура или скорость ветра?')
    Flag = True
    while Flag:
        for text in text_gen:
            print(text)
            if text == 'время':
                print(time)
                voice.text_to_speech(f'В этом городе сейчас {nw(int(time.split()[1][:2]), lang='ru')} ноль ноль')
                Flag = False
                break
            elif text == 'температура':
                voice.text_to_speech(f'Температура воздуха {nw(int(weather), lang='ru')} градусов')
                Flag = False
                break
            elif text == 'осадки':
                voice.text_to_speech(f'Сейчас {precipitation}')
                Flag = False
                break
            elif text == 'скорость ветра':
                voice.text_to_speech(f'Cкорость ветра: {nw(int(wind_speed[:2]), lang='ru')} метров в секунду')
                Flag = False
                break

def activities(text):
    voice.text_to_speech('Вот десять активностей для улицы')
    webbrowser.open('https://rutube.ru/video/768fb0e5866ee27ed1f72d5ba8472b6d/?t=7')

def close(text):
    options(['Жаль', 'Хорошо', 'как скажете', 'уже закрываю'])
    pyautogui.hotkey('ctrl', 'w')

def back(text):
    options(['как вы непостоянны', 'открываю', 'что-то забыли посмотреть?', 'вот прошлая страница'])
    pyautogui.hotkey('ctrl', 'shift', 't')
