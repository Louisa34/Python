'''1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.'''

my_list = ['Hello', 15, [23, 12, 56], 85.23, ('World', 0, '!'), {'London': 99, 'Rome': 12}]
for el in my_list:
    print(type(el))

'''2. Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().'''

my_list = (input('Write the elements for list:').split())
if (len(my_list) % 2) != 0:
    for el in range(0, (len(my_list) - 2), 2):
        my_list[el], my_list[(el + 1)] = my_list[(el + 1)], my_list[el]
else:
    for el in range(0, len(my_list), 2):
        my_list[el], my_list[(el + 1)] = my_list[(el + 1)], my_list[el]
print(my_list)

'''3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict.'''

# with list
mon_num = int(input('Write the number of month:'))
sea_num = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
sea_name = ['winter', 'spring', 'summer', 'autumn']
for el in range(0, 4):
    if mon_num in sea_num[el]:
        print(f'This month belongs to {sea_name[el]}')

# with dictionary
mon_num = int(input('Write the number of month:'))
sea_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
for el in sea_dict:
    print(el)
    if mon_num in sea_dict[el]:
        print(f'This month belongs to {el}')
        break

'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. 
Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.'''

my_str = (input('Write a few words with separator-space:')).split(' ')
for ind, el in enumerate(my_str, 1):
    print(ind, el[:10]) if len(el) > 10 else print(ind, el)

'''5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. 
У пользователя нужно запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.'''

new_el = int(input('Write new element of rating:'))
my_list = [8, 8, 8, 6, 4, 4, 3, 2, 0]
my_list.reverse()
for el in range(0, len(my_list)):
    if new_el > my_list[len(my_list) - 1]:
        my_list.insert((len(my_list)), new_el)
        print(my_list)
        break
    else:
        if my_list[el] < new_el < my_list[el + 1]:
            my_list.insert((el + 1), new_el)
            print(my_list)
            break
        else:
            if new_el == my_list[el]:
                new_el_num = my_list.count(new_el)
                my_list.insert((el + new_el_num), new_el)
                print(my_list)
                break

'''6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя.'''

my_list = (input('Напишите характеристики товара через пробел  в формате название цена количество единица измерения:')).split()
struc, name_list, price_list, quan_list, unit_list = [], [], [], [], []
n = 1
for el in range(0, len(my_list), 4):
    temp_dict = {'Название': my_list[el], 'Цена': int(my_list[el + 1]), 'Количество': int(my_list[el + 2]), 'Ед. измерения': my_list[el + 3]}
    temp_tup = (n, temp_dict)
    struc.append(temp_tup)
    n += 1
    name_list.append(my_list[el])
    price_list.append(my_list[el + 1])
    quan_list.append(my_list[el + 2])
    unit_list.append(my_list[el + 3])
print(struc)
my_dict = {'Название': name_list, 'Цена': price_list, 'Количество': quan_list, 'Ед. измерения': unit_list}
print(my_dict)








