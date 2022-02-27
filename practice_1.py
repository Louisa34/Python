'''1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,затем выведите на экран.'''

word_1 = 'Hello'
word_2 = 'world'
word_3 = '!'
word_4 = word_2 + word_3
print(word_1, word_4)
number = 2022
num_with = str(number) + word_3
print(word_1, num_with)
fs_input = input('Write some message:')
sc_input = str(input('Write some number:'))
print("This is your text ...")
print('This is for generations:' + fs_input, 'From ' + sc_input + ' year')

'''2. Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.'''

sec_inp = int(input('Write the time in seconds:'))
hours = sec_inp // 3600
minuts_1 = sec_inp - hours * 3600
minuts = minuts_1 // 60
seconds = minuts_1 - minuts * 60
print(f'чч:{hours} мм:{minuts} сс:{seconds}')

'''3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.'''

n_inp = input('Write a number N:')
sum = int(n_inp) + int(n_inp*2) + int(n_inp*3)
print(f'N + NN + NNN = {sum}')

'''4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

n_inp = int(input('Write integer positive number N:'))
num_d = 0
temp_b = 0
while n_inp > 0:
    temp_d = n_inp % 10
    n_inp = n_inp // 10
    temp_l = temp_d
    if temp_l > temp_b:
        temp_b = temp_l
    else:
        temp_b = temp_b
print(f'The biggest digital is {temp_b}')

'''5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма. 
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. 
Выведите соответствующее сообщение.'''
'''6. Если фирма отработала с прибылью, вычислите рентабельность выручки. 
Это отношение прибыли к выручке. 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника'''

profit_inp = float(input('Write a profit of firm:'))
cost_inp = float(input('Write a loss of firm:'))
if profit_inp > cost_inp:
    print('Финансовый результат: фирма работает с прибылью.')
    profit_rev = (profit_inp - cost_inp) / profit_inp
    print(f'Рентабельность фирмы составила {profit_rev}')
    num_empl = int(input('Введите количество сотрудников фирмы:'))
    prof_per_empl = profit_inp / num_empl
    print(f'Прибыль фирмы в расчете на одного сотрудника составила {prof_per_empl} ')
elif profit_inp < cost_inp:
    print('Финансовый результат: фирма работает в убыток.')

'''Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. 
Требуется определить номер дня, на который результат спортсмена составит не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.'''

firs_km = int(input('Введите количество км первого дня:'))
goal_km = int(input('Введите количество км, которое хотелось бы пробегать за день:'))
one_day_km = firs_km
days = 0
temp_km = 0
while one_day_km <= goal_km:
    one_day_km = round((one_day_km + temp_km*0.1), 2)
    temp_km = one_day_km
    days += 1
    print(f'{days} день:{one_day_km}')
print(f'На {days} день вы будете пробигать желаемые {goal_km} км.')
