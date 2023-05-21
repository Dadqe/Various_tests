# 2022.09.01 16:00

import tkinter as tk
from typing import Union
import random

# random.seed(1)

class Element:
    def __init__(self, number: int, color: str = '') -> None:
        self.number = number
        self.color = color
    
    def __repr__(self) -> str:
        return str(self.number)
    
    @property
    def number(self) -> int:
        return self.__number
    
    @number.setter
    def number(self, num: int):
        self.__number = num
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color: str = ''):
        self.__color = color

class Results:
    def __init__(self) -> None:
        self.list_results = []
    
    @property
    def save(self):
        return self.list_results
    
    @save.setter
    def save(self, array):
        if len(self.list_results) == 3:
            self.list_results.pop(0)
            self.list_results.append(array)
        else:
            self.list_results.append(array)
    
    def __bool__(self):
        return bool(self.save)
    
    def __getitem__(self, indx):
        return self.save[indx]
    
    # Через объект-свойство property def save() запуливать в список полученный результат, если список уже будет заполнен тремя элементами, то тогда надо будет pop(0) and append(array) и всё
    # Объект класса Results надо будет глобально объявлять... либо в первом окне, пока надо поразмыслить. Что б был к нему доступ из окна с результатами и можно было бы потом хоть в какое окно добавить кнопку по работе с результатами, показать "результат 1", "результат 2" и т.д.

# Объявление всех моих функций для работы с массивом данных
def set_array_size():
    '''Устанавливаю количество строк и столбцов в массиве. В данном случае надо создать окошко с inputom, куда запишется два числа: строка и столбец. Получу текст и просплитую через пробел и назначу нужным переменным, необходимые значения. При передаче данных лэйбл скроется. Или через spinbox это вроде к label или отдельно'''
    print('Хотят выбрать размер массива данных')

# Трансформация матрицы, если есть повторяющиеся символы
def transform_array(A):
    A_prev = A
    A_prev_T = [list(row) for row in zip(*A_prev)]
    A_out = []
    
    for i_s, s in enumerate(A_prev): # s-stroka (string)
        stroka = []
        
        for i_c, n in enumerate(s):     # c-column (столбец) Тут я получаю каждое число в строке и буду сравнивать, есть ли такое же в строке и в столбце. n - число в каждой колонке
            count = 0
            el_in_cls = Element(n)
            instring = check_in_string(s, n)
            incolumn = check_in_column(A_prev_T[i_c], n)
            
            if instring-1:
                count += instring
                el_in_cls.color = '#FFFF00'
            if incolumn-1:
                count += incolumn
                el_in_cls.color = '#00FF00'
            if instring-1 and incolumn-1:
                el_in_cls.color = '#00bfff'
            
            el_in_cls.number = n * count if count else n
            stroka.append(el_in_cls)    # Тут я добавляю элемент класса.... Выглядит он всё равно так же. Это просто для того, что б притащить с собой цвет ячейки, где находится это число до момента формирования выходных таблиц
        A_out.append(stroka)    # Добавляю трансформированную строку в выходной массив
    
    return A_out
    

def check_in_string(string: list, num: int) -> int:
    '''Считает количество повторений в строке. Передать надо строку и число, которое проверяю. Может вернуть 0, считается как False, значит не встречается'''
    return string.count(num)    # Отнимаю единицу, потому что там всегда будет 1, само проверяемое число


def check_in_column(column: list, num: int) -> int:
    '''Считает количество повторений в столбце. Передать надо столбец и число, которое проверяю. Может вернуть 0, считается как False, значит не встречается'''
    return column.count(num)

# def prev_and_past(array: list[list[int]]):
#     source_array(array)
#     resulting_array(array)

# def source_array(array: list[list[int]]):
#     print("Исходный массив:")
#     [print(*l) for l in array]
#     return array

def resulting_array(array: list[list[int]]):
    # print("Результат вычислений")
    res = transform_array(array)
    # [print(*l) for l in res]
    return res

# def return_number_of_all_num(array: list[list[int]]) -> int:
#     rows = len(array)         # Определю сколько строк (количество вложенных списков)
#     columns = len(array[0])   # Определю сколько колонок (т.к. прямоугольные массивы, то в каждой строке будет одинковое кол-во столбцов и можно по первому взять определить)
#     number_of_all_nums = rows * columns
#     return number_of_all_nums

def build_first_win():
    global results_t, btn_3,  btn_4, btn_5  # Эти всякие виджеты и экземпляры класса должны появляться/"регистрироваться" в первом окошке и я как-то должен иметь к ним доступ из вне этого окна
    results_t = Results()
    
    # Создание окна и его настройки
    win = tk.Tk()
    win.title("Тест")
    win.geometry("600x600+660+240")     # Сначала размеры окна (горизонталь вертикаль, потом отступы от верхнего левого угла, по горизонту и вертикали)
    # win.resizable(False, False)         # Что б "запретить" растягивать экран

    # Label для текстовой информации
    label_1 = tk.Label(win, text='''Привет! Выбери действие:''', font=('Arial', 14))

    # Создание кнопок
    btn_1 = tk.Button(win, text='Выбрать размер\nмассива данных', command=set_size_array, font=('Arial', 14))
    btn_2 = tk.Button(win, text='Вывести рандомный\nрезультирующий массив', command=get_random_transform_array, font=('Arial', 14))
    btn_3 = tk.Button(win, text='Показать сохр.\nмассив №1', command=show_saved_one, font=('Arial', 14))
    btn_4 = tk.Button(win, text='Показать сохр.\nмассив №2', command=show_saved_second, font=('Arial', 14))
    btn_5 = tk.Button(win, text='Показать сохр.\nмассив №3', command=show_saved_third, font=('Arial', 14))
    btn_6 = tk.Button(win, text='Результат работы\nна тестовом массиве', command=test_array, font=('Arial', 14))

    # Настраиваю конфигурацию колонок для отображения виджетов через метод grid:
    win.grid_columnconfigure(0, minsize=100)        # Для 1й колонки. Индексация так же с нуля
    win.grid_columnconfigure(1, minsize=100)        # Для 2й колонки. Индексация так же с нуля


    # Здесь у меня будет "загрузка" виджетов в окна
    label_1.grid(row=0, column=0, columnspan=2)

    btn_1.grid(row=1, column=0)
    btn_2.grid(row=1, column=1)
    btn_6.grid(row=1, column=2)
    
    win.mainloop()

def build_second_win() -> tk.Tk:
    '''Создание второго окна, на котором будет изображаться "Исходный массив" и "Результирующий" Общее окно, в него потом по надобности всякие виджеты закидывать'''
    win2 = tk.Tk()
    win2.title('Вывод результата')
    win2.geometry("600x600+660+240")
    
    # Создание виджетов общих
    
    # Загрузка виджетов в окно
    # label1_1.grid(row=0, column=0, columnspan=2)
    
    return win2

def build_second_win1():
    '''Создание второго окна, где предстоит выбирать размер массива данных'''
    rows, columns = 0, 0
    
    def save_choice():
        nonlocal rows, columns
        rows, columns = int(spinbox1_1.get()), int(spinbox1_2.get())
        if check_valid_size():
            forget_widgets(spinbox1_1, spinbox1_2, btn1_1, label1_1, label1_3, label1_2, label1_5)
            label1_1['text'] = 'Выбраны следующие характеристики массива:'
            label1_2['text'] = f'Количество строк: {rows}  Количество колонок: {columns}'
            label1_1.grid(row=0, column=0, columnspan=2)
            label1_2.grid(row=1, column=0, columnspan=2)
            label1_4.grid(row=2, column=0, columnspan=2)
            btn1_3.grid(row=3, column=0)
            btn1_4.grid(row=3, column=1)
        else:
            label1_5.grid(column=0, columnspan=2)
    
    def check_valid_size():
        '''Проверка на правильность ввода данный ячеек массива данных. Если вернётся False, следующий шаг не откроется'''
        print(f"Строк: {rows}, Надо не более: {spinbox1_1['to']}")
        print(f"Колонок: {columns}, Надо не более: {spinbox1_2['to']}")
        if rows > int(spinbox1_1['to']) or columns > int(spinbox1_2['to']):
            print("Всё плохо. Где-то ввели число, не входящее в заданные границы")
            return False
        else:
            return True
            
    
    def manual_input():
        forget_widgets(label1_1, label1_2, label1_4, btn1_3, btn1_4)
        label1_4['text'] = 'Выбран метод ручного ввода массива данных\nВарианты чисел от 0 до 30 включительно'
        label1_1.grid(row=0, column=0, columnspan=columns)
        label1_2.grid(row=1, column=0, columnspan=columns)
        label1_4.grid(row=2, column=0, columnspan=columns)
        need_spinboxes = tuple()
        
        def get_array():
            nums_in_array = tuple([int(spin.get()) for spin in need_spinboxes])    # Создам список из всех чисел по порядку спинбоксов, как они создавались и значит задавались числа. В общем, всё как надо.
            # for spin in need_spinboxes:
            #     nums_in_array.append(int(spin.get()))
            
            # check_list = [True if 0 <= el <= int(need_spinboxes[0]['to']) else False for el in nums_in_array]     # Для проверки
            check_values = all([True if 0 <= el <= int(need_spinboxes[0]['to']) else False for el in nums_in_array])    # Проверяю, все ли значения в списке подходят под заданный диапазон
            # print(check_values)     # Для проверки функционала
            # Если не проходит проверку, нужно снова сформировать уведомление и не пустить дальше
            if check_values:
                chunked_array = tuple([tuple(nums_in_array[i:i+columns]) for i in range(0, len(nums_in_array), columns)])     # Тут происходит split этого списка, что б были вложенные и получился массив. Мб tuple хранить проще и "дешевле"?) хотя всё равно работает list comprehenshion
                return chunked_array
            else:
                label1_5.grid(column=0, columnspan=columns)
                return False
            # print(nums_in_array) # Для проверки
            # print(chunked_array) # Для проверки
        
        def transform_it_and_show():
            '''Преобразовываю указанный массив данных. Открываю окно и показываю результаты преобразования'''
            some_array = get_array()
            if not some_array == False:
                build_second_win2(some_array)  # type: ignore
            # print(some_array)
        
        for r in range(rows):
            for c in range(columns):
                link = tk.Spinbox(win2_1, from_=0, to=50, font=('Arial', 12), justify='center', width=5)
                link.grid(row=4+r, column=c)    # Сделал подобным образом, что б можно было потом значения вытащить, как иначе сделать, пока не увидел
                need_spinboxes = need_spinboxes + (link, )  # Добавляю спинбоксы в память, что б по ним потом пройтись и применить метод get и вытащить оттуда числа заданные
        # Если я просто расположу окно с вводом значений для каждой ячейки через пробел, например, то надо будет ещё кучу проверок делать. Сплитить, проверять количество значений, проверить все значения на то, что они int, потом это обработать всё...
        
        # btn1_5 = tk.Button(win2_1, text='Сохранить данный массив', command=save_it, font=('Arial', 14)) # Но вроде не надо просто сохранять массив. Мне ведь надо "Сохранять результат".
        btn1_5 = tk.Button(win2_1, text='Преобразовать данный массив\nИ показать результат', command=transform_it_and_show, font=('Arial', 14))
        
        btn1_5.grid(column=0, columnspan=columns)
        
    
    def automatic_input():
        forget_widgets(label1_1, label1_2, label1_4, btn1_3, btn1_4)
        label1_4['text'] = 'Выбран метод автоматического формирования\nмассива данных по заданным параметрам\nВарианты чисел от 0 до 30 включительно'
        label1_1.grid(row=0, column=0, columnspan=columns)
        label1_2.grid(row=1, column=0, columnspan=columns)
        label1_4.grid(row=2, column=0, columnspan=columns)
        btn1_5.grid(columnspan=columns)
        rand_array = [[random.randint(0, 30) for _ in range(columns)] for _ in range(rows)]
        return rand_array
    
    def automatic_show():
        build_second_win2(automatic_input())
    
    def forget_widgets(*args):
        '''Чтобы не плодить кучу строк виджетов с методом скрывания, я буду в эту функцию передавать необходимые методы и в цикле их прятать'''
        for widget in args:
            widget.grid_forget()
    
    # def check_choice():
    #     print(rows, columns)
    
    win2_1 = build_second_win()
    
    label1_1 = tk.Label(win2_1, text='Выберите размеры массива данных.\nМожно выбрать максимум 10 ячеек в каждом сечении', font=('Arial', 14))
    label1_2 = tk.Label(win2_1, text='Количество строк:', font=('Arial', 14))
    label1_3 = tk.Label(win2_1, text='Количество колонок:', font=('Arial', 14))
    label1_4 = tk.Label(win2_1, text='Желаете вручную ввести массив\nданных или автоматически?', font=('Arial', 14))
    # label1_4 = tk.Label(win2_1, text='Введите массив данных вручную', font=('Arial', 14))
    label1_5 = tk.Label(win2_1, text='Вы умудрились выйти за заданные границы\nПожалуйста следуйте требованиям,\nНаписанным выше👆', font=('Arial', 14))
    spinbox1_1 = tk.Spinbox(win2_1, from_=1, to=10, font=('Arial', 12), justify='center')     # Для указания строк
    spinbox1_2 = tk.Spinbox(win2_1, from_=1, to=10, font=('Arial', 12), justify='center')     # Для указания колонок
    btn1_1 = tk.Button(win2_1, text='Подтвердить выбор', command=save_choice, font=('Arial', 14))
    # btn1_2 = tk.Button(win2_1, text='Проверить выбор', command=check_choice, font=('Arial', 14))  # На всякий случай чисто служебная кнопка была, для проверки функционала записи вводимых строк и колонок
    btn1_3 = tk.Button(win2_1, text='Вручную', command=manual_input, font=('Arial', 14))
    btn1_4 = tk.Button(win2_1, text='Автоматически', command=automatic_input, font=('Arial', 14))
    btn1_5 = tk.Button(win2_1, text='Показать результат вычислений', command=automatic_show, font=('Arial', 14))
    
    
    label1_1.grid(row=0, column=0, columnspan=2)
    label1_2.grid(row=1, column=0)
    label1_3.grid(row=1, column=1)
    spinbox1_1.grid(row=2, column=0)
    spinbox1_2.grid(row=2, column=1)
    btn1_1.grid(row=3, column=0, columnspan=2)
    # btn1_2.grid(row=4, column=0, columnspan=2)
    
    # Настройка ширины столбцов. В цикле, потому что надо для всех колонок настроить
    for c in range(columns):
        win2_1.grid_columnconfigure(c, minsize=50)

def build_second_win2(array: Union[list[list[int]], tuple[tuple[int]]]):
    '''Эта функция именно под тестовый массив из ТЗ напрямую array вызываю'''
    
    
    def save_result():
        results_t.save = res
        print(results_t.list_results)
        if len(results_t.save) == 1:
            btn_3.grid()
        elif len(results_t.save) == 2:
            btn_4.grid()
        elif len(results_t.save) == 3:
            btn_5.grid()
    
    win2_2 = build_second_win()     # Даю ссылку на второе окно, что б туда виджеты подгружать
    
    # prev = source_array(array)      # Похоже, что не надо, т.к. я в эту функцию уже передаю array изначальный, что б запустить его в цикле переработки
    res = resulting_array(array)  # type: ignore
    rows, сolumns = len(array), len(array[0])       # Определяю количество символов в строке и столбцах, т.к. часто дальше по коду буду использовать, что б постоянно не вызывать len
    
    # Создание виджетов
    label2_1 = tk.Label(win2_2, text='''Исходный массив:''', font=('Arial', 14))
    label2_2 = tk.Label(win2_2, text='''Результирующий массив:''', font=('Arial', 14))
    
    # btn2_1 = tk.Button(win2_2, text="I'm HERE!", font=('Arial', 14), command=second_hello)
    btn2_1 = tk.Button(win2_2, text='Сохранить результирующий массив', font=('Arial', 14), command=save_result)
    
    # Сначала создам столько виджетов, сколько надо под каждое число и заполню ноликами для наглядности. Всё в цикле, естественно, количество labels зависит от того, сколько всего чисел в массиве
    # Загрузка виджетов в окно
    label2_1.grid(row=0, column=0, columnspan=сolumns)            # "Исходный массив"
    for r in range(rows):           # тут перебираются вложенные списки == строки
        for c in range(сolumns):    # тут перебираются элементы вложенного первого списка == колонки
            tk.Label(win2_2, text=array[r][c]).grid(row=r+1, column=c)    # +1 потому что у меня в первой строке label "Исходный массив:"
    label2_2.grid(row=rows+2, column=0, columnspan=сolumns)       # "Результирующий массив" +2 что б отступить от всех строк и первого label, т.к. строки типа с 0 будут вести подсчёт
    
    for r in range(rows):           # тут перебираются вложенные списки == строки
        for c in range(сolumns):    # тут перебираются элементы вложенного первого списка == колонки
            if res[r][c].color:
                tk.Label(win2_2, text=res[r][c], background=res[r][c].color, font=('Arial', 10)).grid(row=rows+3+r, column=c)
            else:
                tk.Label(win2_2, text=res[r][c]).grid(row=rows+3+r, column=c)    # +3 надо отступить две строки текста и ещё 1, т.к. индексация строк начинается с 0 и надо отступить вниз
    
    btn2_1.grid(row=rows*2+3, column=0, columnspan=сolumns)
    
    # Настройка ширины столбцов. В цикле, потому что надо для всех колонок настроить
    for c in range(сolumns):
        win2_2.grid_columnconfigure(c, minsize=50)      # Думаю, такой ширины достаточно для отображения 6 значных чисел и даже с расстоянием между ними. Построчно и так неплохой формат
    
    # Надо будет где-то формировать отдельный массив и тогда начинать передавать его по цепочке, а то с тестовым то щас просто всё....
    
def build_third_win(win_num):
    '''Создание окошка для отображения сохранённых результатов раннее'''
    win3 = build_second_win()
    win3.title(f'Вывод сохр. рез. №{win_num}')
    
    array = results_t[win_num-1]
    rows, сolumns = len(array), len(array[0])
    
    for r in range(rows):
        for c in range(сolumns):
            tk.Label(win3, text=array[r][c]).grid(row=r, column=c)
    
    for c in range(сolumns):
        win3.grid_columnconfigure(c, minsize=50)

# Функции для кнопок первого окна --------------------------------------------------------------------------------------------
def get_random_transform_array():
    print('Тыкнули на кнопку рандомного результирующего массива')
    rand_rows = random.randint(2, 10)
    rand_columns = random.randint(2, 10)
    rand_array = [[random.randint(0, 20) for _ in range(rand_columns)] for _ in range(rand_rows)]
    # r_arr = [[random.randint(0, 20) for _ in range(random.randint(2, 10))] for _ in range(random.randint(2, 10))] # Так не вышло, потому что внутренние списки формировались как попало, а не с одним количеством элементов (колонок)
    # print(rand_array)     # Проверка служебная
    build_second_win2(rand_array)     # По нажатию на кнопку я тут сразу передаю нужный массив, в зависимости от кнопки. В каждой кнопке будет заложен свой массив.

def set_size_array():
    print('Тыкнули на первую кнопку. Хотят выбрать размер массива данных')
    build_second_win1()

def secondс_hello():
    print("Привет из второго окна")

def test_array():
    print('Проверка на тестовом массиве данных из Задания')
    test_array = [[0, 2, 3, 9, 7], [6, 2, 4, 5, 8], [8, 9, 1, 2, 8], [6, 5, 4, 3, 0], [9, 7, 6, 2, 1]]
    build_second_win2(test_array)

def show_saved_one():
    print("Хотят посмотреть на первый результат")
    build_third_win(1)

def show_saved_second():
    print("Хотят посмотреть на второй результат")
    build_third_win(2)

def show_saved_third():
    print("Хотят посмотреть на третий результат")
    build_third_win(3)

# array = [[0, 2, 3, 9, 7], [6, 2, 4, 5, 8], [8, 9, 1, 2, 8], [6, 5, 4, 3, 0], [9, 7, 6, 2, 1]]    # Тестовый массив из примера
# random_array = [[random.randint(0, 20)] for _ in range(random.randint(2, 10))]

def main():
    build_first_win()

if __name__ == '__main__':
    main()
    


# Можно атвоматически (построчно) создавать Лэйблы, что б туда выводилась построчно информация о строках в массиве
# Можно попробовать созавать label в него передавать многострочную строку, которая будет сама проставлять отступы, подумать, как можно сделать

# Остаётся вопрос о закрашивании всего этого дела.... Только если через grid добавлять labels и закрашивать их фон..

# Для вывода думаю, стоит создать отдельное окно, которое будет вызываться и там буду все эти labels расположены в нужном порядке и подкрашены как надо
# В этом окне создать кнопки (Закрыть, Сохранить) и буду сохранять в последнюю ячейку списка, видимо, удаляя первую, что-то типа объекта класса сделать, там будет проверка, есть ли у этого объекта в локальном аттрибуте чкакой-то объект на 0 индексе, если список будет заполнен, тип Len == 3, то тогда надо будет удалять первый элемент, добавлять 3й... под капотом будет формироваться массив, по которому будет итерироваться функция, создавать окошки и выводить результаты + как-то красить🥲 
# возможно из-за этих "сохранёнок, надо будет обновлять главное окно и создавать кнопку типа показать 1й итоговый результат, 2й итоговый и т.д."
# Сначала задумки отработаю с одной функцией, которая берёт тестовый вариант массива и покажет его без закрашиваний хотя б....

# Указание количества строк и столбцов можно реализовать через spinbox, вроде норм тема, избавляю себя от проверки правильно вводимых данных... Но ограничиться мб в 10х10? что б не жирно было

# Посчитал, что можно попробовать создать класс для отображения значения в массиве, отображаться оно так и будет цифрой, наверное, ну или строкой, просто так можно будет сразу вычислять и записывать, в какой цвет надо будет закрасить label и тащить это вместе с объектом класса
# Принты в консоль чисто для дополнительного контроля действий и типа логирования

# Надо углубиться и научиться формировать весь tkinter через классы, что б можно было заголовки передавать, копки там или ещё что-нибудь, ну и что б по-человечески выглядело. А то всё через костылики какие-то