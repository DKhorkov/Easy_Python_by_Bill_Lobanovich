# Task - 1:
class Thing:
    pass


print(Thing)
example = Thing()
print(example)


# Task - 2:
class Thing2:
    letters = 'abc'  # Без метода инициализации, ибо переменная тут просто для хранения информации.


print(Thing2.letters)


# Task - 3:
class Thing3:
    def __init__(self):
        self.letters = 'xyz'


thing3 = Thing3()
print(thing3.letters)


# Tasks 4 - 6:
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'This element\'s name is {self.name}, it\'s symbol is {self.symbol} and number is {self.number}.')


args_for_element_class = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# hydrogen = Element(args_for_element_class['name'],
#                    args_for_element_class['symbol'], args_for_element_class['number'],)
# Можно использовать словарь как представлено выше, однако куда эффективнее делать
# это с использование именованных аргументов:
hydrogen = Element(**args_for_element_class)
hydrogen.dump()

# Tasks 7-8:
print(hydrogen)


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def __str__(self):
        return f'This element\'s name is {self.__name}, it\'s symbol is {self.__symbol} and number is {self.__number}.'


print(hydrogen := Element(**args_for_element_class))

# Task - 9:
class Bear:
    @staticmethod
    def eats():
        return 'berries'


class Rabbit:
    @staticmethod
    def eats():
        return 'clover'


class Octothopre:
    @staticmethod
    def eats():
        return 'campers'


bear = Bear()
print(bear.eats())
rabbit = Rabbit()
print(rabbit.eats())
octothorpe = Octothopre()
print(octothorpe.eats())

# Task - 10:
class Laser:
    @staticmethod
    def does():
        return 'disintegrate'


class Claw:
    @staticmethod
    def does():
        return 'crush'


class SmartPhone:
    @staticmethod
    def does():
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print(self.laser.does())
        print(self.claw.does())
        print(self.smartphone.does())


robot = Robot()
robot.does()
