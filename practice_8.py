'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год».'''


class Date:

    def __init__(self):
        global new_date
        self.my_date = input('Write the date in format day-month-year:')
        new_date = self.my_date.split('-')

    @classmethod
    def str_trans(cls):
        day = int(new_date[0])
        month = int(new_date[1])
        year = int(new_date[2])
        return f'Day:{day} \nMonth:{month} \nYear:{year}'

    @staticmethod
    def valid():
        if 1 <= int(new_date[1]) <= 12:
            print('The month is written correctly!')
        else:
            print('The month should be in range 1 to 12!')
        if int(new_date[2]) < 2000:
            print('The year should be more then 2000!')
        else:
            print('The year is written correctly!')


date_1 = Date()
print(Date.str_trans())
Date.valid()

'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.'''


class ZeroDiv(Exception):

    def __init__(self, text):
        self.text = text


nums_str = (input('Write two number with space:')).split()
try:
    if int(nums_str[1]) == 0:
        raise ZeroDiv('Division by zero!')
except ValueError:
    print('Should be a number!')
except ZeroDiv as err:
    print(err)
else:
    print(f'Your numbers: {int(nums_str[0])}, {int(nums_str[1])}')

'''3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел.'''


class OnlyNum(Exception):
    def __init__(self, text):
        self.text = text


num_list = []
zero_nine = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
    n, k = 0, 0
    nums = input('Stop word: stop! Write a number:')
    if nums == 'stop':
        print(f'Your list of numbers:{num_list}')
        break
    try:
        for i in range(0, 10):
            if zero_nine[i] in nums:
                n += 1
            else:
                k += 1
        if n > 0:
            num_list.append(float(nums))
        if k == 10:
            raise OnlyNum('Write only a number!')
    except OnlyNum as err:
        print(err)

'''4. 5. 6. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников.'''

from abc import ABC, abstractmethod


class Cinema:

    def __init__(self):
        global guest_name
        self.gn = input('Write your name:')
        guest_name = self.gn.upper()

    @ staticmethod
    def welcome():
        return f'Dear {guest_name} ! Welcome to the world of cinematography!'


class FilmAwards:

    @ staticmethod
    def f_awads():
        return f'Here you will know all about cinema awards.'


class FilmFestival(ABC):

    @ staticmethod
    def f_festival():
        return f'Here you will know all about film festivals.'

    @abstractmethod
    def history(self):
        pass

    @ abstractmethod
    def best_film(self):
        pass

    @ abstractmethod
    def best_director(self):
        pass

    @ abstractmethod
    def best_screenplay(self):
        pass


class Berlinale(FilmFestival):

    def __init__(self, year):
        global y_year
        self.year = year
        y_year = int(self.year)

    @ staticmethod
    def f_name():
        return 'Berlin International Film Festival'

    def history(self):
        return 'The Berlin International Film Festival, ' \
               'usually called the Berlinale, is a film festival held annually in Berlin, Germany.' \
               ' Founded in West Berlin in 1951, the festival has been held every February since 1978.'

    def best_film(self):
        ber_film = {2016: 'Fire at Sea', 2017: 'On Body and Soul', 2018: 'Touch Me Not',
                    2019: 'Synonyms', 2020: 'There Is No Evil'}
        return f'Berlin International Film Festival - Golden Bear for Best Film {y_year} - {ber_film[y_year]}'

    def best_director(self):
        pass

    def best_screenplay(self):
        pass


class Cannes(FilmFestival):

    @ staticmethod
    def f_name():
        return 'Cannes Film Festival'

    def history(self):
        return 'The Cannes Festival until 2003 called the International Film Festival and ' \
               'known in English as the Cannes Film Festival, is an annual film festival held in Cannes, France, ' \
               'which previews new films of all genres, including documentaries, from all around the world. ' \
               'Founded in 1946.'

    def best_film(self):
        pass

    def best_director(self):
        pass

    def best_screenplay(self):
        pass


class Venice(FilmFestival):

    @ staticmethod
    def f_name():
        return 'Venice Film Festival'

    def history(self):
        return 'The Venice Film Festival or Venice International Film Festival is the worlds oldest film festival. ' \
               'Founded in Venice, Italy in August 1932, the festival is part of the Venice Biennale, ' \
               'exhibitions of art, created by the Venice City Council on 19 April 1893.'

    def best_film(self):
        pass

    def best_director(self):
        pass

    def best_screenplay(self):
        pass


guest_1 = Cinema()
film_1 = Berlinale(2020)
print(guest_1.welcome())
print(FilmAwards.f_awads())
print(FilmFestival.f_festival())
print(film_1.best_film())

'''7. Реализовать проект «Операции с комплексными числами».'''


class Complex:

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_list = [int(self.num_1), int(self.num_2)]

    def __add__(self, other):

        sum_real = self.num_list[0] + other.num_list[0]
        sum_ima = self.num_list[1] + other.num_list[1]
        return f'The sum of two complex number:{sum_real} + {sum_ima}j'

    def __mul__(self, other):
        mul_real = self.num_list[0] * other.num_list[0] - self.num_list[1] * other.num_list[1]
        mul_ima = self.num_list[0] * other.num_list[1] + self.num_list[1] * other.num_list[0]
        return f'Multiplication of two complex number:{mul_real} + {mul_ima}j'


com_num_1 = Complex(3, 5)
com_num_2 = Complex(-8, 7)
print(com_num_1 + com_num_2)
print(com_num_1 * com_num_2)
