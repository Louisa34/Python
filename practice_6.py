'''1. Создать класс TrafficLight (светофор).'''
import time


class TrafficLight:
    __color_r = 'red'
    __color_y = 'yellow'
    __color_g = 'green'

    def running(self):
        print(self.__color_r)
        time.sleep(7)
        print(self.__color_y)
        time.sleep(5)
        print(self.__color_g)
        time.sleep(6)


tl = TrafficLight()
tl.running()

'''2. Реализовать класс Road (дорога).'''


class Road:
    def __init__(self, _length, _width):
        self.ln = _length
        self.wd = _width

    def asf_mass(self):
        mass = self.ln * self.wd * 25 * 0.05 * 0.001
        return f'Масса асфальта составила {mass} т'


my_par = Road(30, 6000)
print(my_par.asf_mass())

'''3. Реализовать базовый класс Worker (работник).'''


class Worker:
    def __init__(self, name, surname, position, wage, bonus, _income):
        self.nm = name
        self.snm = surname
        self.ps = position
        self.icm = _income
        self.wg = wage
        self.bn = bonus
        self.icm = {'wage': self.wg, 'bonus': self.bn}


class Position(Worker):
    def get_full_name(self):
        return f'Full name of worker is {self.nm} {self.snm}.'

    def get_total_income(self):
        tot_in = self.icm['wage'] + self.icm['bonus']
        return f'The total income of worker is {tot_in}'


my_worker_1 = Position('Criss', 'Rock', 'middle', 30000, 20000, 40000)
print(my_worker_1.get_full_name())
print(my_worker_1.icm)
print(my_worker_1.get_total_income())
my_worker_2 = Position('Mister', 'Incognito', 'junior', 20000, 20000, 35000)
print(my_worker_2.get_full_name())
print(my_worker_2.ps)
print(my_worker_2.get_total_income())

'''4. Реализуйте базовый класс Car.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.sp = speed
        self.cl = color
        self.nm = name
        self.pol = is_police

    def go(self):
        return f'Car is go!'

    def stop(self):
        return f'Car is stopped!'

    def turn(self):
        return f'Car is turned to the right!'

    def show_speed(self):
        return f'Cars speed is {self.sp} km/h.'


class TownCar(Car):
    def info(self):
        return f'Your car is {self.cl}'

    def show_speed(self):
        if self.sp > 60:
            return f'Cars speed is more over 60 km/h! Slow down!.'
        else:
            return f'Cars speed is {self.sp} km/h.'


class SportCar(Car):
    def info(self):
        return f'Your car is {self.cl}'

    def spor(self):
        return f'You have sport car with name {self.nm}!'


class WorkCar(Car):
    def info(self):
        return f'Your car is {self.cl}'

    def show_speed(self):
        if self.sp > 40:
            return f'Cars speed is more over 40 km/h! Slow down!.'
        else:
            return f'Cars speed is {self.sp} km/h.'


class PoliceCar(Car):
    def info(self):
        return f'Your car is {self.cl}'

    def poli(self):
        return f'You driving a police car.'


car_1 = TownCar(70, 'black', 'Lexus', False)
print(car_1.go())
print(car_1.info())
print(car_1.show_speed())

car_2 = PoliceCar(60, 'blue', 'Ford', True)
print(car_2.go())
print(car_2.info())
print(car_2.turn())
print(car_2.poli())

car_3 = WorkCar(60, 'brown', 'Audi', False)
print(car_3.go())
print(car_3.show_speed())

'''5. Реализовать класс Stationery (канцелярская принадлежность).'''


class Stationery:
    def __init__(self, title):
        self.tit = title

    def draw(self):
        return f'Запуск отрисовки -  {self.tit}!'


class Pen(Stationery):
    def draw(self):
        return f'Запущена отрисовка ручкой - {self.tit}!'


class Pencil(Stationery):
    def draw(self):
        return f'Запущена отрисовка карандашом - {self.tit}!'


class Handle(Stationery):
    def draw(self):
        return f'Запущена отрисовка маркером - {self.tit}!'


img_1 = Pen('Солнце')
print(img_1.draw())

img_2 = Pencil('Радуга')
print(img_2.draw())

img_3 = Pencil('Гора')
print(img_3.draw())
