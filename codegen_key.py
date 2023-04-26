import keyboard
import pyperclip
import time
import PIL.Image
import pystray
from threading import Thread

from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "Salesforce/codegen-350M-multi"

model = AutoModelForCausalLM.from_pretrained(checkpoint)

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def ctrl_key(key):
    keyboard.press(29)
    time.sleep(0.02)
    keyboard.press(key)
    time.sleep(0.02)
    keyboard.release(29)
    keyboard.release(key)
    time.sleep(0.02)

def on_click(icon, item):
    if str(item) == 'Назначить горячие клавиши':
        print('Ты чё тут делаешь?')
    elif str(item) == 'Exit':
        icon.stop()

tray_main = PIL.Image.open('main_logo.png')
tray_progress = PIL.Image.open('processing.png')

icon = pystray.Icon('AIcGen', tray_main, menu=pystray.Menu(
        pystray.MenuItem('Назначить горячие клавиши', on_click),
        pystray.MenuItem('Exit', on_click)
)) # Program title is under construction

def tray_init():
    icon.run()

def generate_code():
    continue_exe = True
    while continue_exe:
        if keyboard.is_pressed(65):
            icon.icon = tray_progress
            ctrl_key(46)
            text = pyperclip.paste()
            completion = model.generate(**tokenizer(text, return_tensors="pt"), max_new_tokens=50)              
            pyperclip.copy(tokenizer.decode(completion[0]))
            ctrl_key(47)
            icon.icon = tray_main

        if not thread_tray.is_alive():
            continue_exe = False

if __name__ == '__main__':
    thread_generator = Thread(target=generate_code)
    thread_tray = Thread(target=tray_init)

    thread_generator.start()
    thread_tray.start()

# Examples
def fibonacci(n):
    """returns nth number of Fibonacci sequence"""

def is_e_in_L(e, L):
    """return True if e in list L"""

def sum_of_elements_of_L(L):
    pass

def RecursiveFactorial(n):
    pass

# void greetUser(string username) {

"""
                                                                                                                                                 v maxsplit = 1 потому что параметры тоже могут быть с пробелами
Варианты решения: input.split(' ') - слева остаётся синтаксис функции, справа название + параметры: signature = "def is_e_in_L(e, L)".split(' ', maxsplit = 1) -> ['def', 'is_e_il_L(e, L)]
                  Далее подставить синтаксис функции для каждого языка: funcJS = 'function' + signature[1]
                  Проводить генерацию на разных потоках для увеличения скорости генерации.
                  Выводить результаты сразу после генерации, а не в один момент
"""