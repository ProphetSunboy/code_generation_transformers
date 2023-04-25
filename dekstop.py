from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import filedialog as fd
from tkinter import ttk

import numpy as np
import pandas as pd

def analyze_sentences():
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


def analyze_csv():
    pass
    # file_name = fd.askopenfilename(filetypes=(('CSV files', '*.csv'),))

    # df = pd.read_csv(file_name, names=['text'], skiprows=1)
    # text_list = df['text'].to_list()

    # if model_type.get() == 0:
    #     predictions = model_ru.predict(np.array(text_list))
    # else:
    #     predictions = model.predict(np.array(text_list))

    # sentiment_df = pd.DataFrame(
    #     [[text_list[i], predictions[i][0]] for i in range(len(text_list))],
    #     columns=['text', 'sentiment'],
    # )

    # sentiment_df.to_csv(file_name, index=False)

    # messagebox.showinfo('Результат', 'Успешно')

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


number_of_tokens_label = Label(
    text="Количество токенов:        ", # Длина генерируемой последовательности в символах
    font= ('Arial', 12),
    background='white',
    highlightbackground="black",
    highlightcolor='black',
    highlightthickness=1,
)
number_of_tokens_label.pack(side=LEFT, anchor=NW, padx=4, pady=10)

number_of_tokens_entry = Entry(
    font= ('Arial', 12),
    width=3,
)
number_of_tokens_entry.pack(side=LEFT,anchor=N, padx=4, pady=10)

temperature_label = Label(
    text="Температура генерации: ",
    font= ('Arial', 10),
    background='white',
    highlightbackground="black",
    highlightcolor='black',
    highlightthickness=1,
)
temperature_label.pack(side=LEFT,anchor=N, padx=4, pady=10)

temperature_entry = Entry(
    font= ('Arial', 10),
    width=4,
)
temperature_entry.pack(side=LEFT, anchor=N, padx=4, pady=10)

python = IntVar()
js = IntVar()
c_2plus = IntVar()
c_lang = IntVar()
go_lang = IntVar()
java = IntVar()

python_checkbutton = ttk.Checkbutton(text='Python', variable=python)
python_checkbutton.pack(side=LEFT, anchor=N, padx=4, pady=10)
lbl = ttk.Label(textvariable=python)
lbl.pack(side=BOTTOM)

js_checkbutton = ttk.Checkbutton(text='JavaScript', variable=js)
js_checkbutton.pack(side=LEFT, anchor=N, padx=4, pady=10)

c_2plus_checkbutton = ttk.Checkbutton(text='C++', variable=c_2plus)
c_2plus_checkbutton.pack(side=LEFT, anchor=N, padx=4, pady=10)

c_lang_checkbutton = ttk.Checkbutton(text='C', variable=c_lang)
c_lang_checkbutton.pack(side=LEFT, anchor=N, padx=4, pady=10)

go_lang_checkbutton = ttk.Checkbutton(text='Go', variable=go_lang)
go_lang_checkbutton.pack(side=LEFT, anchor=N, padx=4, pady=10)

java_checkbutton = ttk.Checkbutton(text='Java', variable=java)
java_checkbutton.pack(side=LEFT, anchor=N, padx=4, pady=10)

cb_frame = Frame(root, bg='white', bd=2)

lbl = Label(cb_frame, text='Py',background='white',)




# number_of_tokens_label.grid(row=0, column=0)
# number_of_tokens_entry.grid(row=0, column=1)

# temperature_label.grid(row=1, column=0)
# temperature_entry.grid(row=1, column=1)

# cb_frame.grid(row=0, column=2)
# lbl.pack(anchor=NW)

#number_of_tokens_lbl.pack(anchor=NW, padx=8, pady=8)
#number_of_tokens_entry.pack(anchor=NW, padx=200, pady=8)

sentences_lb = Label(
    text="Введите текст дла анализа\n"
        "(следующий элемент начинать c новой строки)",
    font=20,
)

predictions_lb = Label(
    text="Результаты анализа",
    font=20,
)

sentences_tf = Text(
    width=80,
    height=16,
)

predictions_tf = Text(
    width=16,
    height=16,
)

analyze_btn = Button(
    text='Анализировать',
    font=20,
    command=analyze_sentences,
)

model_type = IntVar()
model_type.set(0)

output_type = BooleanVar()
output_type.set(0)


help_btn = Button(
    text='Помощь',
    width=8,
    height=2,
    command=show_help
)

scroll_sentences = Scrollbar(command=sentences_tf.yview)
sentences_tf.config(yscrollcommand=scroll_sentences.set)

scroll_pred = Scrollbar(command=sentences_tf.yview)
sentences_tf.config(yscrollcommand=scroll_pred.set)

root.mainloop()