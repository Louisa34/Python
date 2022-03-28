'''1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.'''

# with open('ex_1.txt', 'w', encoding='utf-8') as file:
#     while True:
#         my_str = input('Write a word:')
#         if my_str == '':
#             break
#         else:
#             file.write(my_str + '\n')

'''2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.'''

# with open('ex_2.txt', 'r', encoding='utf-8') as file:
#     f = file.readlines()
#     print(f'File has {len(f)} strings')
#     for i in range(0, len(f)):
#         new_list =  list(f[i].split(' '))
#         print(f'{i +1} string has {len(new_list)} words')

'''3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.'''

# with open('ex_3.txt', 'w+', encoding='utf-8') as file:
#     i = 0
#     while i < 10:
#         em_str = input('Write an employees last name and salary:')
#         file.write(em_str + '\n')
#         i += 1
#     file.seek(0)
#     new_list = file.readlines()
#     print(f'List of employees which salary less then 20 thousands:')
#     all_sal = 0.0
#     for j in range(0, 10):
#         new_str = new_list[j].split('\n')
#         name_sal = new_str[0].split(' ')
#         if float(name_sal[1]) < 20000.00:
#             print(name_sal[0])
#         all_sal = all_sal + float(name_sal[1])
#     mid_sal = all_sal / 10
#     print(f'The avarage salary of employees is {mid_sal}')

'''4. Создать (не программно) текстовый файл. Напишите программу, открывающую файл на чтение и считывающую построчно 
данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.'''

# num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять' }
# with open('ex_4.txt', 'r', encoding='utf') as file:
#     with open('ex_4_1.txt', 'w', encoding='utf-8') as n_file:
#         str_line = file.readlines()
#         for i in range(0, len(str_line)):
#             new_num = str_line[i].split(' - ')
#             n_file.write(f'{num_dict[new_num[0]]} - {i + 1}\n')

'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''

# from functools import reduce
#
# with open('ex_5.txt', 'w+', encoding='utf-8') as file:
#     file.write(input('Write a numbers with space:'))
#     file.seek(0)
#     str_list = file.readline().split(' ')
#     num_list = [float(str_list[i]) for i in range(0, len(str_list))]
#     my_sum = reduce(lambda a,b:a + b, num_list)
#     print(f'Sum = {my_sum}')

'''6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.'''

# from functools import reduce
#
#
# def summa(a, b):
#     return a + b
#
#
# with open('ex_6.txt', 'r', encoding='utf-8') as file:
#     my_st = [':', '(', ')', '-', '\n', ',', '.']
#     new_list = []
#     for line in file:
#         # print(line, end='')
#         for j in range(0, len(my_st)):
#             temp_line = line.replace(my_st[j], ' ')
#             line = temp_line
#         new_list.append(line)
#     end_list = []
#     for i in range(0, len(new_list)):
#         end_list.append(new_list[i].split())
#     sub_dict = {}
#     for k in range(0, len(end_list)):
#         for t in range(0, len(end_list[k])):
#             num_str_list = [int(end_list[k][p]) for p in range(1, len(end_list[k]), 2)]
#         sub_sum = reduce(summa, num_str_list)
#         up_date = [(end_list[k][0], sub_sum)]
#         sub_dict.update(up_date)
#     print(sub_dict)

'''7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков). Итоговый список сохранить в виде json-объекта в соответствующий файл.'''

# import json
#
# with open('ex_7.json', 'w') as f_json:
#     with open('ex_7.txt', 'r', encoding='utf-8') as file:
#         f_line = file.readlines()
#         firm_dict, av_bonus_dict = {}, {}
#         temp = 0
#         for i in range(0, len(f_line)):
#             line_list = f_line[i].replace('\n', '')
#             line_list = f_line[i].split()
#             bonus = int(line_list[len(line_list) - 2]) - int(line_list[len(line_list) - 1])
#             if bonus > 0:
#                 all_bonus = bonus + temp
#                 temp = all_bonus
#             up_date = [(line_list[0], bonus)]
#             firm_dict.update(up_date)
#         up_date_1 = [('average_profit', all_bonus)]
#         av_bonus_dict.update(up_date_1)
#         end_list = [firm_dict, av_bonus_dict]
#         json.dump(end_list, f_json)
