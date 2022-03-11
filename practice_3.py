''' 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.'''


def f_div(d1 = input('Write number d1 = :'), d2 = input('Write number d2 = :')):
    try:
        d1_n, d2_n = float(d1), float(d2)
        div_r = round(d1_n / d2_n, 4)
        print(f'Result = {div_r}')
    except ZeroDivisionError:
        print('Division by zero!')
    except ValueError:
        print('Only digits!')



f_div()

'''2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.'''


def user_inf(las_name = input('Last Name:'), name = input('Name:'), year_bi = input('Year of birth:'),
              city = input('City:'), pho=input('Phone:'), ema = input('Email:') ):
    print(f'Name - {name}, Last Name - {las_name}, '
          f'Year of birth - {year_bi}, City - {city}, '
          f'Email - {ema}, Phone - {pho}')


user_inf()

'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.'''


def my_func(d1 = input('Write number d1 = :'), d2 = input('Write number d2 = :'), d3 = input('Write number d3 = :')):
    try:
        my_list = [d1, d2, d3]
        new_list = map(float, my_list)
        sort = sorted(new_list)
        m1 = max(sort)
        m2 = max(sort[0], sort[1])
        my_sum = float(m1 + m2)
        return my_sum
    except ValueError:
        print('Only digits!')


print(f'Sum = {my_func()}')

'''4. Программа принимает действительное положительное число x и целое отрицательное число
y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
числа в степень.'''

# with operator **
def my_func(x = float(input('Write a positive number x = :')), y = int(input('Write a negative integer number y = :'))):
    expo = round(x ** y, 4)
    return expo


print(f'Result = {my_func()}')

# with cycle
def my_func(x = float(input('Write a positive number x = :')), y = int(input('Write a negative integer number y = :'))):
    temp = 1
    for i in range(1, (abs(y) + 1)):
        expo = round((1 / x) * temp, 4)
        temp = expo
    return expo


print(f'Result = {my_func()}')

'''5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.'''


def my_func():
    temp = 0
    while True:
        num = input('Write a numbers with separator-space:').split(' ')
        for el in range(0, len(num)):
            if num[el] == 'stop':
                for i in range(0, el):
                    print(f'Sum = {my_sum}')
                    return
            else:
                my_sum = float(num[el]) + temp
                temp = my_sum
        my_sum = temp
        print(f'Sum = {my_sum}')


my_func()

'''6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой.
В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию int_func().'''

def int_func(my_word):
        cap_word = my_word.capitalize()
        return cap_word


word = input('Write a words:').split(' ')
new_word = list(map(int_func, word))
print(f'New list of words: {new_word}')
