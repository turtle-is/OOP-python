"""Итоговое задание
Выбрать сущности, для которых можно реализовать наследование.

Должны быть реализованы как минимум один базовый и дочерний класс.
В базовом классе должны быть реализованы конструктор __init__, магические методы __str__ и __repr__.
В дочернем классе либо унаследовать, либо расширить конструктор базового класса, унаследовать или перегрузить магические методы __str__ и __repr__..
Количество атрибутов и методов для каждого класса выбираете самостоятельно.
В дочернем классе необходимо унаследовать как минимум один метод и перегрузить один метод (помимо магических методов __str__ и __repr__).
При перегрузке метода обосновать причину, указав её в документации к методу.
Если считаете необходимым, то некоторые атрибуты и методы можно сделать непубличными.
Причину инкапсуляции указать или в виде комментариев для атрибутов или в документации для методов.
Все аргументы и выходные результаты методов должны иметь аннотацию типов.
Для всех классов и методов должна быть написана документация.
Дополнительно
Саму реализацию методов писать необязательно.
Но если считаете возможным описать как бы работали методы, можно представить их реализацию в виде python кода."""



class Predatory: 
    def __init__(self, species: str):
        self.species = None
        self.init_species(species)

    def init_species(self, species: str):
        if not isinstance(species, str):
            raise TypeError
        self.species = species
        
    # Магический метод для представления объекта в виде строки
    def __str__(self) -> str:
        return f"Predatory {self.species}"

    # Магический метод для представления объекта в виде репрезентации
    def __repr__(self) -> str:
        return f"Predatory({self.species})"


class Manul(Predatory):
    def __init__(self, species: str, weight: float):
        super().__init__(species)
        self.weight = weight
        
    # Перегрузка  метода для представления объекта в виде строки
    def __str__(self) -> str:
        return f"Manul {self.species}, weight: {self.weight} kg"

    # Унаследованный  метод для представления объекта в виде репрезентации

    def hunt(self) -> str:
        """
        Метод охоты для манула.
        
        Возвращаемое значение:
        - str: Результат охоты.
        """
        return "The Manul is hunting!"

    
class Bobcat(Predatory):
    def __init__(self, species: str, age: int):
        super().__init__(species)
        self.age = age
        
    # Перегрузка метода для представления объекта в виде строки
    def __str__(self) -> str:
        return f"Bobcat {self.species}, age: {self.age} years"

    # Унаследованный метод для представления объекта в виде репрезентации

    def sleep(self) -> str:
        """
        Метод сна для рыси.
        
        Возвращаемое значение:
        - str: Результат сна.
        """
        return "The Bobcat is sleeping!"


if __name__ == "__main__":
   
    manul = Manul("Manul cat", 8)
    print(manul)  # Вывод: Manul Manul cat, weight: 8 kg
    print(manul.hunt())  # Вывод: The Manul is hunting!

    bobcat = Bobcat("Lynx", 5)
    print(bobcat)  # Вывод: Bobcat Lynx, age: 5 years
    print(bobcat.sleep())  # Вывод: The Bobcat is sleeping()
