from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from codegen import generate_code

def remove_datatypes(str):
    '''
    remove_datatypes(str)
        Return str without datatypes.
    '''
    data_types = ['string', 'int', 'bool', 'char', 'float', 'double']
    return ', '.join([word for word in ''.join(str.split(',')).split() if word.lower() not in data_types])

def split_outputs():
    '''
    Function to separate outputs.
    '''
    return '\n\n_______________________________\n\n'

def format_f_name(f_name, lang='not py'):
    '''
    format_f_name(f_name, lang='not py')
        Function returns a properly formatted function name,
        depending on the lang.
    '''
    if lang == 'py':
        if '_' in f_name:
            return f_name
        # 'greetUser' -> 'greet_user'
        return ''.join([f_name[i].lower() if f_name[i+1].islower() else f_name[i].lower() + '_' for i in range(len(f_name)-1)]) + f_name[-1]
    else:
        if '_' not in f_name:
            return f_name
        # 'greet_user' -> 'greetUser'
        return ''.join([word[0].upper() + word[1:] if i != 0 else word for i, word in enumerate(f_name.split('_'))])

def parse_input(text):
    '''
    parse_input(text)
        return properly parsed input sequence for different programming
        languages i.e. parse_input('def greet_user(username):') ->
        -> {'Py': 'def greet_user(username):',
            'JS': 'function greetUser(username){',
            ...
            }
    '''
    function_name, params = text.split(':')[0].split('{')[0].split('(')
    function_name = function_name.split(' ')[-1]
    params = params.split(')')[0]
    formatted_params = remove_datatypes(params)

    python = f'def {format_f_name(function_name, lang="py")}({formatted_params}):'
    js = f'function {format_f_name(function_name)}({formatted_params})' + '{'
    c_2plus = f'void {format_f_name(function_name)}({params})' + '{'
    c_lang = f'#include <stdio.h>\nvoid {format_f_name(function_name)}({params})' + '{'
    go_lang = f'func {format_f_name(function_name)}({params})' + ' {'
    java = f'public void {format_f_name(function_name)}({params})' + '{'

    signatures = {'Py': python, 'JS': js, 'C++': c_2plus,
                  'C': c_lang, 'Go': go_lang, 'Java': java}
    
    return signatures

def generate():
    '''
    Function check inputs for correctness and perform
    code generation in selected programming languages.
    '''
    correct_inputs = True

    try:
        # slicing [:3] needed to limit input n_tokens
        n_tokens = int(number_of_tokens_entry.get().strip()[:3])
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

    try:    
        signatures = parse_input(input_seq)
    except ValueError:
        messagebox.showerror('Ошибка ввода', 'Введённая функция некорректна')
        correct_inputs = False

    if correct_inputs:
        output_txt.delete('1.0', END)
        
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
    '''
    Show info about program in messagebox
    '''
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
root.title("Генерация кода")
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
text_boxes.pack()

input_frame = Frame(text_boxes)
output_frame = Frame(text_boxes)

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