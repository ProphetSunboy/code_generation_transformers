from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import filedialog as fd
from tkinter import ttk

import numpy as np
import pandas as pd

from codegen import generate_code

def generate():
    correct_inputs = True
    try:
        max_tokens = int(number_of_tokens_entry.get().strip())
        temperature = float(temperature_entry.get().strip())
    except ValueError:
        messagebox.showinfo('Некорректные данные',
            'Количество токенов и температура генерации должны быть числовыми')
        correct_inputs = False

    input_seq = input_txt.get().strip()
    if len(input_seq) == 0:
        messagebox.showinfo('Пустой ввод',
                            'Пожалуйста введите сигнатуру функции')
        correct_inputs = False

    if correct_inputs:
        output_txt.delete('1.0', END)
        splitted_input = input_seq.split(' ', maxsplit=1)

        if python.get() == 1:
            output_txt.insert(END, '\n\nPython:\n')
            generate_code(,max_tokens, temperature)

        if js.get() == 1:
            output_txt.insert(END, '\n\JavaScript:\n')
            generate_code(,max_tokens, temperature)

        if c_2plus.get() == 1:
            output_txt.insert(END, '\n\C++:\n')
            generate_code(,max_tokens, temperature)

        if c_lang.get() == 1:
            output_txt.insert(END, '\n\C:\n')
            generate_code(,max_tokens, temperature)

        if go_lang.get() == 1:
            output_txt.insert(END, '\n\Go:\n')
            generate_code(,max_tokens, temperature)

        if java.get() == 1:
            output_txt.insert(END, '\n\Java:\n')
            generate_code(,max_tokens, temperature)

        generate_code(input_seq, max_tokens, temperature)
    pass
    # predictions_tf.delete(1.0, END)
    # sentences = sentences_tf.get(1.0, END).split('\n')

    # sentences_correctness = []
    # for i in range(len(sentences) - 1):
    #     iscorrect = bool(sentences[i].strip())
    #     sentences_correctness.append(iscorrect)
    #     if not iscorrect:
    #         messagebox.showinfo('Некорректное предложение',
    #             f'Предложение {i+1} введено некорректно')

    # if not all(sentences_correctness):
    #     messagebox.showinfo('Ошибка анализа',
    #         'Введите корректный текст для анализа')
    # else:
    #     if model_type.get() == 0:
    #         predictions = model_ru.predict(np.array(sentences[:-1]))
    #     else:
    #         predictions = model.predict(np.array(sentences[:-1]))

    #     if output_type.get() == 0:
    #         for x in range(0, len(predictions)):
    #             predictions_tf.insert(float(x+1), str(predictions[x]) + '\n') 

    #         messagebox.showinfo('Среднее',
    #             str(sum(predictions) / len(predictions)))

    #     else:
    #         for x in range(0, len(predictions)):
    #             if predictions[x] < -0.1:
    #                 predictions_tf.insert(float(x+1), 'Негативный' + '\n')
    #             elif predictions[x] > 0.1:
    #                 predictions_tf.insert(float(x+1), 'Положительный' + '\n')
    #             else:
    #                 predictions_tf.insert(float(x+1), 'Нейтральный' + '\n')
    #         pred_avg = sum(predictions) / len(predictions)
    #         if pred_avg < -0.1:
    #             messagebox.showinfo('Среднее', 'Негативно')
    #         elif pred_avg > 0.1:
    #             messagebox.showinfo('Среднее', 'Положительно')
    #         else:
    #             messagebox.showinfo('Среднее', 'Нейтрально')


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
    command=analyze_sentences,
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