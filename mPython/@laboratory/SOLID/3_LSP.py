# =======================================================
# Liskov Substitution Principle
"""
Принцип подстановки Лисков гласит что обьекты подклассов должны
быть взаимозаменяемыми с обьектами суперкласса без
изменения правильности программы
...
Подклассы должны быть взаимозаменяемыми с суперклассами
"""
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        # Логика полёта воробья
        pass

class Penguin(Bird):
    def swim(self):
        # Логика плавания пингвина
        pass
# =======================================================
""" НЕ ПРАВИЛЬНО """
class Figure:
    def get_area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = witdth
        self.height = height

    def get_area(self):
        return self.width * self.height
# =======================================================
""" ПРАВИЛЬНО """
# В пайтоне по-умолчанию нет функционала для работы с абстрактными классами и методами
from abc import ABC, abstractmethod

# Специально делаем абстрактный класс он наследуется от класса ABC
class Figure(ABC):
    @abstractmethod # Указываем что метод абстрактный
    def get_area(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side

    # Переопределяем абстрактный метод
    def area(self):
        return self.side ** 2

class Regtangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
# =======================================================
""" ТАК ТОЖЕ ПРАВИЛЬНО """
class Figure:
    def get_area(self):
        raise NotImplementedError("Subclasses should implement this method")
    
class Square(Figure):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
# =======================================================