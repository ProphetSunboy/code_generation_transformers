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

# remove title bar
root.overrideredirect(True)

def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

# create fake title bar
title_bar = Frame(root, bg='darkgreen')
title_bar.pack(expand=1, fill=X)

# Bind the title bar
title_bar.bind('<B1-Motion>', move_app)

# Create title text
title_label = Label(title_bar, text='   AIcGen', bg='darkgreen', fg='white')
title_label.pack(side=LEFT, pady=4)

# Create close button on titel bar
close_button = Button(title_bar, text='  X  ', command=root.destroy, bg='darkgreen', fg='white')
close_button.pack(side=RIGHT, pady=4)

number_of_tokens_label = Label(
    root,
    text="Количество токенов:        ", # Длина генерируемой последовательности в символах
    font= ('Arial', 12),
    background='white',
    highlightbackground="black",
    highlightcolor='black',
    highlightthickness=1,
)
number_of_tokens_label.pack(side=LEFT, padx=4, pady=(10, 380))

number_of_tokens_entry = Entry(
    root,
    font= ('Arial', 12),
    width=20,
)
number_of_tokens_entry.pack(padx=(0, 680), pady=(10, 380))

temperature_lbl = Label(
    root,
    text="Температура генерации: ",
    font= ('Arial', 12),
    background='white',
    highlightbackground="black",
    highlightcolor='black',
    highlightthickness=1,
)

temperature_entry = Entry(
    root,
    font= ('Arial', 12),
    width=4,
)

cb_frame = Frame(root, bg='white', bd=2)

lbl = Label(cb_frame, text='Py',background='white',)

# scroll_sentences = Scrollbar(command=sentences_tf.yview)
# sentences_tf.config(yscrollcommand=scroll_sentences.set)

# scroll_pred = Scrollbar(command=sentences_tf.yview)
# sentences_tf.config(yscrollcommand=scroll_pred.set)

root.mainloop()