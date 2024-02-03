from typing import Union


class Tree:
    """Конструктор класса"""
    def __init__(self, variety: str):
        if not isinstance(variety, str):
            raise TypeError
        self.variety = variety

    """Метод проверяет наличие листьев у дерева в зависимости от времени года
        метод содержит аргумент season - время года"""
    def has_leaves(self, season: str) -> bool:
        if not isinstance(season, str):
            raise TypeError
        if season == "summer":
            return True
        elif season == "winter":
            return False
        elif season == "autumn":
            return False
        elif season == "spring":
            return True
class Person:
    """Конструктор класса"""
    def __init__(self, name: str, gender: str, age: int):
        self.name = None
        self.init_name(name)
        self.gender = None
        self.init_gender(gender)
        self.age = None
        self.init_age(age)

    """метод инициилизации с проверкой атрибута name"""
    def init_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    """метод инициилизации с проверкой атрибута gender"""
    def init_gender(self, gender: str):
        if not isinstance(gender, str):
            raise TypeError
        self.gender = gender

    """метод инициилизации с проверкой атрибута age"""
    def init_age(self, age: int):
        if not isinstance(age, int):
            raise TypeError
        self.age = age


    """Метод выводит сообщение представления экземпляра Person
        метод не имеет аргументов, выводит атрибуты name и age"""
    def performance(self) -> None:
         """>>> person1.performance()
         Привет, меня зовут Rayan Gosling, мне 30 лет"""
         
         print(f"Привет, меня зовут {self.name}, мне {self.age} лет")

class Car:
    """Конструктор класса"""
    def __init__(self, color: str, weight: int, producer: str, driver: str):
        self.color = None
        self.init_color(color)
        self.weight = None
        self.init_weight(weight)
        self.producer = None
        self.init_producer(producer)
        self.driver = None
        self.init_driver(driver)

    """метод инициилизации с проверкой атрибута color"""
    def init_color(self, color: str):
        if not isinstance(color, str):
            raise TypeError
        self.color = color

    """метод инициилизации с проверкой атрибута weight"""
    def init_weight(self, weight: Union[int, float]):
        if not isinstance(weight, (int, float)):
            raise TypeError
        self.weight = weight

    """метод инициилизации с проверкой атрибута producer"""
    def init_producer(self, producer: str):
        if not isinstance(producer, str):
            raise TypeError
        self.producer = producer

    """метод инициилизации с проверкой атрибута driver"""
    def init_driver(self, driver:str):
        if not isinstance(driver, str):
            raise TypeError
        self.driver = driver


    """Метод выводит значения атрибутов класса"""
    def get_info(self) -> None:
         print(f"Цвет: {self.color}\n Вес: {self.weight}\n Марка: {self.producer}\n Водитель: {self.driver}")

    """Метод отвечает за гудок автомобиля"""
    def sound(self) -> None:
        print("!!!BIP-BIP-BIP!!!")


if __name__ == "__main__":

    tree1 = Tree("Сосна")
    print("Наличие листьев зимой: ", tree1.has_leaves("winter"))

    person1 = Person("Rayan Gosling", "male", 30)
    person1.performance()

    car1 = Car("Black", 2340, "Ваз-2109", "Rayan Gosling")
    car1.get_info()
    car1.sound()
