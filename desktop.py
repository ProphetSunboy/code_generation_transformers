from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

from codegen import generate_code

def remove_datatypes(str):
    '''
    remove_datatypes(str)
        Return str without datatypes.
    '''
    data_types = ['string', 'int', 'bool', 'char', 'float', 'double', 'integer']
    return ', '.join([word for word in ''.join(str.split(',')).split() if word.lower() not in data_types])

def split_outputs():
    '''
    Function to separate outputs.
    '''
    return f'\n\n{"_"*97}\n\n'

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
    comments = (text.split('\n', maxsplit=1) + [''])[1].strip().replace('"""', '').replace('//', '').replace('\t', '').split('\n')
    py_comments = '\n    '.join(comments)
    other_comments = '\n    '.join('// ' + line for line in comments if line)
    function_name = function_name.split(' ')[-1]
    params = params.split(')')[0]
    formatted_params = remove_datatypes(params)

    python = f'def {format_f_name(function_name, lang="py")}({formatted_params}):' + f'\n    """{py_comments}"""' * (len(py_comments) != 0)
    js = f'function {format_f_name(function_name)}({formatted_params})' + '{' + f'\n    {other_comments}' * (len(other_comments) != 0)
    c_2plus = f'void {format_f_name(function_name)}({params})' + '{' + f'\n    {other_comments}' * (len(other_comments) != 0)
    c_lang = f'#include <stdio.h>\nvoid {format_f_name(function_name)}({params})' + '{' + f'\n    {other_comments}' * (len(other_comments) != 0)
    go_lang = f'func {format_f_name(function_name)}({params})' + ' {' + f'\n    {other_comments}' * (len(other_comments) != 0)
    java = f'public void {format_f_name(function_name)}({params})' + '{' + f'\n    {other_comments}' * (len(other_comments) != 0)

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
            'Значения полей "Количество токенов" и "Температура генерации"\n должны быть числовыми')
        correct_inputs = False

    if n_tokens <= 0 or temperature_inp <= 0:
        messagebox.showwarning('Некорректные данные',
            'Значения полей "Количество токенов" и "Температура генерации"\n должны быть больше 0')
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
            output_txt.insert(END, 'Python:\n\n')
            output_txt.insert(END, generate_code(signatures.get('Py'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if js.get() == 1:
            output_txt.insert(END, 'JavaScript:\n\n')
            output_txt.insert(END, generate_code(signatures.get('JS'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if c_2plus.get() == 1:
            output_txt.insert(END, 'C++:\n\n')
            output_txt.insert(END, generate_code(signatures.get('C++'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if c_lang.get() == 1:
            output_txt.insert(END, 'C:\n\n')
            output_txt.insert(END, generate_code(signatures.get('C'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if go_lang.get() == 1:
            output_txt.insert(END, 'Go:\n\n')
            output_txt.insert(END, generate_code(signatures.get('Go'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

        if java.get() == 1:
            output_txt.insert(END, 'Java:\n\n')
            output_txt.insert(END, generate_code(signatures.get('Java'), max_tokens=n_tokens, temperature=temperature_inp) + split_outputs())

def show_help():
    '''
    Show info about program in messagebox
    '''
    messagebox.showinfo('Помощь',
                'Количество токенов это максимальное\n'
                'количество токенов (ограничено 999 токенами)\n'
                'Температура генерации это коэффициент вероятностного\n'
                'распределения генерации (меньшие значения увеличивают\n'
                'шанс зацикливания генерации).\n'
                'Код выбранных языков программирования в процессе\n'
                'генерации будет появляться в поле "Результат генерации"\n'
                'Для получения результата генерации необходимо в поле\n'
                '"Введите функцию" ввести сигнатуру функции и нажать\n'
                'на кнопку "Сгенерировать код".'
    )

root = ctk.CTk()
root_width, root_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{root_width}x{root_height}')
root.title("Генерация кода")
root.state('zoomed')
root.minsize(1350, 700)
root.iconbitmap(default="icons/main_logo.ico")

# background_image = PhotoImage('icons/background.png')
# background_label = Label(root, image=background_image)
# background_label.place(x=0, y=0, relheight=1, relwidth=1)

# background_image = ctk.CTkImage(Image.open(fp='icons/background.png'))
# background_label = ctk.CTkLabel(master=root, image=background_image)
# background_label.place(x=0, y=0, relheight=1, relwidth=1)

parameters = ctk.CTkFrame(root)
parameters.pack(fill=X, side=TOP)

number_of_tokens_label = ctk.CTkLabel(
    parameters,
    text="Количество токенов: ",
    font=('Roboto', 16),
)
number_of_tokens_label.pack(side=LEFT, anchor=NW, padx=(60, 0), pady=(10,10))

number_of_tokens_entry = ctk.CTkEntry(
    parameters,
    font=('Roboto', 16),
    width=40,
)
number_of_tokens_entry.pack(side=LEFT,anchor=N, padx=0, pady=(10,10))

temperature_label = ctk.CTkLabel(
    parameters,
    text="Температура генерации: ",
    font=('Roboto', 16),
)
temperature_label.pack(side=LEFT,anchor=N, padx=(10, 0), pady=(10,10))

temperature_entry = ctk.CTkEntry(
    parameters,
    font=('Roboto', 16),
    width=46,
)
temperature_entry.pack(side=LEFT, anchor=N, padx=0, pady=(10,10))

python = IntVar()
js = IntVar()
c_2plus = IntVar()
c_lang = IntVar()
go_lang = IntVar()
java = IntVar()

java_checkbutton = ctk.CTkCheckBox(parameters, text='Java', font=('Roboto', 16), variable=java)
java_checkbutton.pack(side=RIGHT, anchor=N, padx=(0, 60), pady=(10,10))

go_lang_checkbutton = ctk.CTkCheckBox(parameters, text='Go', font=('Roboto', 16), variable=go_lang)
go_lang_checkbutton.pack(side=RIGHT, anchor=N, padx=0, pady=(10,10))

c_lang_checkbutton = ctk.CTkCheckBox(parameters, text='C', font=('Roboto', 16), variable=c_lang)
c_lang_checkbutton.pack(side=RIGHT, anchor=N, padx=0, pady=(10,10))

c_2plus_checkbutton = ctk.CTkCheckBox(parameters, text='C++', font=('Roboto', 16), variable=c_2plus)
c_2plus_checkbutton.pack(side=RIGHT, anchor=N, padx=0, pady=(10,10))

js_checkbutton = ctk.CTkCheckBox(parameters, text='JavaScript', font=('Roboto', 16), variable=js)
js_checkbutton.pack(side=RIGHT, anchor=N, padx=(0, 30), pady=(10,10))

python_checkbutton = ctk.CTkCheckBox(parameters, text='Python', font=('Roboto', 16), variable=python)
python_checkbutton.pack(side=RIGHT, anchor=N, padx=(0, 10), pady=(10,10))

text_boxes = ctk.CTkFrame(root)
text_boxes.pack(anchor=CENTER, pady=(80,0))

input_frame = ctk.CTkFrame(text_boxes)
output_frame = ctk.CTkFrame(text_boxes)

input_frame.pack(side=LEFT)
output_frame.pack(side=RIGHT, padx=(1, 0))

input_label = ctk.CTkLabel(
    input_frame,
    text="Введите функцию: ",
    font=('Roboto', 18),
)
input_label.pack(anchor=NW, padx=(20, 0), pady=(10, 0))

output_label = ctk.CTkLabel(
    output_frame,
    text="Результат генерации: ",
    font=('Roboto', 18),
)
output_label.pack(anchor=NW, padx=(16, 0), pady=(10, 0))

input_txt = ctk.CTkTextbox(input_frame, font=('Roboto', 14), width=640, height=400, wrap=NONE)
input_txt.pack(side=LEFT,anchor=NW, padx=(20, 10), pady=(0, 20))

output_txt = ctk.CTkTextbox(output_frame, font=('Roboto', 14), width=640, height=400, wrap=NONE)
output_txt.pack(side=LEFT, anchor=NW, padx=(10, 20), pady=(0, 20))

generate_button = ctk.CTkButton(
    root,
    text='Сгенерировать код',
    font=('Roboto', 20),
    width=120,
    height=48,
    corner_radius=45,
    command=generate,
)
generate_button.pack(anchor=S, padx=(0, 0), pady=(10, 0))

help_button = ctk.CTkButton(
    root, 
    text='Помощь',
    font=('Roboto', 16),
    width=32,
    height=24,
    corner_radius=45,
    command=show_help,
)
help_button.pack(side=BOTTOM, anchor=SE, padx=(0, 10), pady=(0, 10))

root.mainloop()