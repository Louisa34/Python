'''1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.'''


class Matrix:
    def __init__(self):
        self.mt_1 = [[2, 5, 8], [7, 25, -3], [6, 0, 10]]
        self.mt_2 = [[62, 45, 11], [-9, 30, -7], [34, 52, 12]]

    def __str__(self):
        new_list = [self.mt_1, self.mt_2]
        for n in range(0, 2):
            print(f'Matrix {n + 1}')
            for j in range(0, 3):
                print(f'{new_list[n][j][0]} -- {new_list[n][j][1]} -- {new_list[n][j][2]}')

    def __add__(self):
        new_mt = []
        print(f'Matrix - Sum')
        n = 0
        for i in range(0, 3):
            for j in range(0, 3):
                new_str = self.mt_1[i][j] + self.mt_2[i][j]
                new_mt.append(new_str)
            print(f'{new_mt[i + n]} -- {new_mt[i + n + 1]} -- {new_mt[i + n + 2]}')
            n += 2


my_max = Matrix()
my_max.__str__()
my_max.__add__()

'''2) Реализовать проект расчета суммарного расхода ткани на производство одежды.'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    @ abstractmethod
    def clo_fem(self):
        return 'This clothes for women.'


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @ property
    def size(self):
        return self.__size

    @ size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 48:
            self.__size = 48
        else:
            self.__size = size

    @ size.getter
    def get_coat_size(self):
        return f'The coat size is {str(self.__size)}'

    def clo_fem(self):
        return 'This clothes for women.'

    def coat_1(self):
        coat_text = self.size / 6.5 + 0.5
        return round(coat_text, 2),\
               f'The textile for coat: {round(coat_text, 2)}.'


class Costume(Clothes):
    def __init__(self, height):
        self.h = height

    def clo_fem(self):
        return 'This clothes for women.'

    def costume_1(self):
        cos_text = 2 * self.h + 0.3
        return cos_text, \
               f'The textile for costume: {round(cos_text, 2)}.'


my_cloths_1 = Coat(46)
my_cloths_2 = Costume(120)
print(my_cloths_1.coat_1()[1])
print(my_cloths_1.get_coat_size)
print(my_cloths_2.costume_1()[1])
print(f'The total textile : {round((my_cloths_1.coat_1()[0] + my_cloths_2.costume_1()[0]), 2)}')

'''3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка.'''


class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __add__(self, other):
        return f'The sum of two cells: {self.num_cell + other.num_cell}.'

    def __sub__(self, other):
        if (self.num_cell - other.num_cell) > 0:
            return f'The difference of two cells: {self.num_cell - other.num_cell}.'
        else:
            return f'The difference of two cells less then 0.'

    def __mul__(self, other):
        return f'The multiplication of two cells: {self.num_cell * other.num_cell}.'

    def __truediv__(self, other):
        return f'The division of two cells: {self.num_cell // other.num_cell}.'

    def make_order(self, num_cell, num_row):
        new_str = '*' * num_row + '\n'
        if num_cell // num_row == 0:
            new_line = new_str * (num_cell // num_row)
            return f'{new_line}'
        else:
            new_line = new_str * (num_cell // num_row) + '*' * (num_cell - num_cell // num_row * num_row)
            return f'{new_line}'


cell_1 = Cell(5)
cell_2 = Cell(3)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(20, 8))
