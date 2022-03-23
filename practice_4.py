'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.'''

from sys import argv

work_time, rate, bonus = map(int, argv[1:])
sal = (work_time * rate) + bonus
print(f'Result = {sal}')

'''2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
которых больше предыдущего элемента.'''

from random import randint

i = 0
ran_list = []
while i < 10:
    ran_list.append(randint(1, 100))
    i += 1
print(f'Random list: {ran_list}')
new_list = [ran_list[j] for j in range(1, len(ran_list)) if ran_list[j - 1] < ran_list[j]]
print(f'New list: {new_list}')

'''3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну
строку.'''

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

'''4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в
порядке их следования в исходном списке. Для выполнения задания обязательно используйте
генератор.'''

my_list = [1, 2, 5, 5, 8, 8, 1, 11, 9, 12, 3, 3, 3, 4]
new_list = [my_list[i] for i in range(len(my_list)) if my_list.count(my_list[i]) == 1]
print(f'New list:{new_list}')

'''5. Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
результат вычисления произведения всех элементов списка.'''

from functools import reduce


def multi(a, b):
    return a * b


new_list = [i for i in range(100, 1001) if i % 2 == 0]
print(f'New_list:{new_list}')
print(f'Result = {reduce(multi, new_list)}')

'''6. Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее.'''

from  itertools import count, cycle
import time

my_num = int(input('Write an integer number:'))
for el in count(my_num):
    if time.process_time() > 5:
        break
    print(el)

for i in cycle('background'):
    if time.process_time() > 10:
        break
    print(i)

'''7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
нужно выводить только первые n чисел, начиная с 1! и до n!.'''

from functools import reduce


def multi(a, b):
    return a * b


def fact(n):
    for el in (i for i in range(0, n)):
        yield el


for ele in fact(int(input('Write an integer number:'))):
    if ele == 0:
        print(f'{ele}! = 1')
    else:
        my_list = [j for j in range(1, ele + 2)]
        print(f'{ele}! = {reduce(multi, my_list)}')
