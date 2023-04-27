from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import filedialog as fd
from tkinter import ttk

import numpy as np
import pandas as pd

from codegen import generate_code

def replace_datatypes(str):
    data_types = ['string', 'int', 'bool', 'char', 'float', 'double']
    return ', '.join([word for word in str.split() if word.lower() not in data_types])

def parse_input(text):

    function_name, params = text.split(':')[0].split('{')[0].split('(')
    function_name = function_name.split(' ')[1]
    params = params.split(')')[0]
    formatted_params = replace_datatypes(params)

    python = replace_datatypes(f'def {function_name}({formatted_params}):')
    js = replace_datatypes(f'function {function_name}({formatted_params})' + '{')
    c_2plus = f'void {function_name}({params})' + '{' 
    c_lang = f'#include <stdio.h>\nvoid {function_name}({params})' + '{'
    go_lang = f'func {function_name}({params})' + '{'
    java = f'public void {function_name}({params})' + '{'

    signatures = {'Py': python, 'JS': js, 'C++': c_2plus,
                  'C': c_lang, 'Go': go_lang, 'Java': java}
    
    return signatures

def generate():
    correct_inputs = True
    try:
        max_tokens = int(number_of_tokens_entry.get().strip())
        temperature = round(float(temperature_entry.get().strip()), 2)
    except ValueError:
        messagebox.showinfo('Некорректные данные',
            'Количество токенов и температура генерации должны быть числовыми')
        correct_inputs = False

    input_seq = input_txt.get('1.0', END).strip()
    if len(input_seq) == 0:
        messagebox.showinfo('Пустой ввод',
                            'Пожалуйста введите сигнатуру функции')
        correct_inputs = False

    if correct_inputs:
        output_txt.delete('1.0', END)
        signatures = parse_input(input_seq)

        if python.get() == 1:
            output_txt.insert(END, '\n\nPython:\n')
            output_txt.insert(END, generate_code(signatures.get('Py'), max_tokens, temperature))

        if js.get() == 1:
            output_txt.insert(END, '\n\nJavaScript:\n')
            output_txt.insert(END, generate_code(signatures.get('JS'), max_tokens, temperature))

        if c_2plus.get() == 1:
            output_txt.insert(END, '\n\nC++:\n')
            output_txt.insert(END, generate_code(signatures.get('C++'), max_tokens, temperature))

        if c_lang.get() == 1:
            output_txt.insert(END, '\n\nC:\n')
            output_txt.insert(generate_code(signatures.get('C'), max_tokens, temperature))

        if go_lang.get() == 1:
            output_txt.insert(END, '\n\nGo:\n')
            output_txt.insert(generate_code(signatures.get('Go'), max_tokens, temperature))

        if java.get() == 1:
            output_txt.insert(END, '\n\nJava:\n')
            output_txt.insert(generate_code(signatures.get('Java'), max_tokens, temperature))

def show_help():
    messagebox.showinfo('Помощь', 'Язык анализа следует выбирать исходя '
        'из языка анализируемого текста.\n'
        'Формат вывода определяет в каком виде будет '
        'показан результат: числовом или словесном.\n'
        'Для получения результата необходимо в поле '
        'анализа ввести текст и нажать на кнопку "Анализировать".\n'
        'При выборе ".csv" файла результат, после анализа, '
        'автоматически запишется в этот файл.\n'
        'Файл должен содержать единственный столбец с анализируемым текстом.\n'
        'После анализа, в тот же файл, добавится второй '
        'столбец с результатами.\n'
        'При работе с ".csv" файлом всегда используется формат вывода "Точный"'
    )

root = Tk()
root.geometry('900x450')
root.title("AIcGEN")
root.iconbitmap(default="icons/main_logo.ico")
# root.config(background='lightgray')

parameters = Frame(root)
parameters.pack(expand=1, fill=X, padx=(0, 0), pady=(0, 20))

number_of_tokens_label = Label(
    parameters,
    text="Количество токенов:        ", # Длина генерируемой последовательности в символах
    font= ('Arial', 11),
    background='white',
    highlightbackground="black",
    highlightcolor='black',
    highlightthickness=1,
)
number_of_tokens_label.pack(side=LEFT, anchor=NW, padx=(20, 1))

number_of_tokens_entry = Entry(
    parameters,
    font= ('Arial', 11),
    width=3,
)
number_of_tokens_entry.pack(side=LEFT,anchor=N, padx=0, pady=(1, 0))

temperature_label = Label(
    parameters,
    text="Температура генерации: ",
    font= ('Arial', 11),
    background='white',
    highlightbackground="black",
    highlightcolor='black',
    highlightthickness=1,
)
temperature_label.pack(side=LEFT,anchor=N, padx=(10, 1))

temperature_entry = Entry(
    parameters,
    font= ('Arial', 11),
    width=4,
)
temperature_entry.pack(side=LEFT, anchor=N, padx=0, pady=(1, 0))

python = IntVar()
js = IntVar()
c_2plus = IntVar()
c_lang = IntVar()
go_lang = IntVar()
java = IntVar()

python_checkbutton = ttk.Checkbutton(parameters,text='Python', variable=python)
python_checkbutton.pack(side=LEFT, anchor=N, padx=(80, 4))

js_checkbutton = ttk.Checkbutton(parameters,text='JavaScript', variable=js)
js_checkbutton.pack(side=LEFT, anchor=N, padx=4)

c_2plus_checkbutton = ttk.Checkbutton(parameters,text='C++', variable=c_2plus)
c_2plus_checkbutton.pack(side=LEFT, anchor=N, padx=4)

c_lang_checkbutton = ttk.Checkbutton(parameters,text='C', variable=c_lang)
c_lang_checkbutton.pack(side=LEFT, anchor=N, padx=4)

go_lang_checkbutton = ttk.Checkbutton(parameters,text='Go', variable=go_lang)
go_lang_checkbutton.pack(side=LEFT, anchor=N, padx=4)

java_checkbutton = ttk.Checkbutton(parameters,text='Java', variable=java)
java_checkbutton.pack(side=LEFT, anchor=N, padx=4)

text_boxes = Frame(root)

input_frame = Frame(text_boxes)
output_frame = Frame(text_boxes)
text_boxes.pack()
input_frame.pack(side=LEFT)
output_frame.pack(side=LEFT)

input_label = Label(
    input_frame,
    text="Введите функцию: ",
    font= ('Arial', 11),
)
input_label.pack(anchor=NW, padx=(20, 0), pady=(0, 0))

output_label = Label(
    output_frame,
    text="Результат генерации: ",
    font= ('Arial', 11),
)
output_label.pack(anchor=NE, padx=(0, 235), pady=(0, 0))

input_txt = Text(input_frame, width=46, height=14, wrap=NONE)
input_txt.pack(side=LEFT,anchor=NW, padx=(20, 0), pady=(0, 0))

output_txt = Text(output_frame, width=46, height=14, wrap=NONE)
output_txt.pack(anchor=NE, padx=20, pady=(0, 0))

generate_button = Button(
    root,
    text='Сгенерировать код',
    width=20,
    height=2,
    command=generate,
)
generate_button.pack(anchor=S, padx=(0, 0), pady=(10, 0))

help_button = Button(
    root, 
    text='Помощь',
    width=8,
    height=2,
    command=show_help
)
help_button.pack(anchor=SE, padx=(0, 8), pady=(0, 8))

scroll_input_y = Scrollbar(command=input_txt.yview)
scroll_input_x = Scrollbar(command=input_txt.xview)
input_txt.config(yscrollcommand=scroll_input_y.set, xscrollcommand=scroll_input_x)

scroll_output_y = Scrollbar(command=input_txt.yview)
scroll_output_x = Scrollbar(command=input_txt.xview)
input_txt.config(yscrollcommand=scroll_output_y.set, xscrollcommand=scroll_output_x)

root.mainloop()