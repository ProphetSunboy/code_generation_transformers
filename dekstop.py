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

def split_outputs():
    return '\n\n_______________________________'

def parse_input(text):
    function_name, params = text.split(':')[0].split('{')[0].split('(')
    function_name = function_name.split(' ')[-1]
    params = params.split(')')[0]
    formatted_params = replace_datatypes(params)

    python = f'def {function_name}({formatted_params}):'
    js = f'function {function_name}({formatted_params})' + '{'
    c_2plus = 'void greetUser(username){'#f'void {function_name}({params})' + '{'
    c_lang = f'#include <stdio.h>\nvoid {function_name}({params})' + '{'
    go_lang = f'func {function_name}({params})' + '{'
    java = f'public void {function_name}({params})' + '{'

    signatures = {'Py': python, 'JS': js, 'C++': c_2plus,
                  'C': c_lang, 'Go': go_lang, 'Java': java}
    
    return signatures

def generate():
    correct_inputs = True

    try:
        n_tokens = int(number_of_tokens_entry.get().strip())
        temperature_inp = round(float(temperature_entry.get().strip()), 2)
    except ValueError:
        messagebox.showwarning('Некорректные данные',
            'Количество токенов и температура генерации должны\nбыть числовыми')
        correct_inputs = False

    input_seq = input_txt.get('1.0', END).strip()
    if len(input_seq) == 0:
        messagebox.showwarning('Пустой ввод',
                            'Пожалуйста введите сигнатуру функции')
        correct_inputs = False

    if correct_inputs:
        output_txt.delete('1.0', END)
        signatures = parse_input(input_seq)

        if python.get() == 1:
            output_txt.insert(END, 'Python:\n')
            output_txt.insert(END, generate_code(signatures.get('Py'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if js.get() == 1:
            output_txt.insert(END, 'JavaScript:\n')
            output_txt.insert(END, generate_code(signatures.get('JS'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if c_2plus.get() == 1:
            output_txt.insert(END, 'C++:\n')
            output_txt.insert(END, generate_code(signatures.get('C++'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if c_lang.get() == 1:
            output_txt.insert(END, 'C:\n')
            output_txt.insert(END, generate_code(signatures.get('C'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if go_lang.get() == 1:
            output_txt.insert(END, 'Go:\n')
            output_txt.insert(END, generate_code(signatures.get('Go'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if java.get() == 1:
            output_txt.insert(END, 'Java:\n')
            output_txt.insert(END, generate_code(signatures.get('Java'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

def show_help():
    messagebox.showinfo('Помощь',
                'Количество токенов это длина генерируемой\n'
                'последовательности в символах\n'
                'Температура генерации это коэффициент случайности\n'
                'генерации (меньшие значения соответствуют более\n'
                'стабильной генерации).\n'
                'Код выбранных языков программирования в процессе\n'
                'генерации будет появляться в поле "Результат генерации"\n'
                'Для получения результата генерации необходимо в поле\n'
                '"Введите функцию" ввести сигнатуру функции и нажать\n'
                'на кнопку "Сгенерировать код".'
    )

root = Tk()
root.geometry('900x450')
root.title("AIcGEN")
root.iconbitmap(default="icons/main_logo.ico")

parameters = Frame(root)
parameters.pack(expand=1, fill=X, padx=(0, 0), pady=(0, 20))

number_of_tokens_label = Label(
    parameters,
    text="Количество токенов:        ",
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