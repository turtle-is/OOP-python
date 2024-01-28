"""Есть два типа книг - бумажная и аудио.
Для всех типов хранения книг у них есть: - название (name) - автор (author)

У бумажной книги есть количество страниц (pages) целочисленного типа данных. У аудио книги есть её продолжительность (duration) как числа с плавающей запятой.

Для классов Book, PaperBook, AudioBook примените наследование.
Исходя из кода подумайте когда методы __str__ и __repr__ могут быть унаследованы, а когда перегружены в дочерних классах. И исправьте это
Атрибуты name и author изменяться не могут, поэтому напишите для них свойства, которые не позволят изменять эти атрибуты.
Так как на pages и duration накладываются ограничения по типу и допустимым значениям, напишите для них свойства с проверками при присвоении им значений."""


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Количество страниц должно быть положительным целым числом")

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float) and value > 0:
            self._duration = value
        else:
            raise ValueError("Продолжительность должна быть положительным числом с плавающей запятой")

    def __str__(self):
        return f"Аудио книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

if __name__ == '__main__':
    # Создание экземпляров классов
    book = Book("Преступление и наказание", "Федор Достоевский")
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    audio_book = AudioBook("Гарри Поттер и философский камень", "Джоан Роулинг", 8.5)

    # Вывод информации о книгах
    print(book)
    print(paper_book)
    print(audio_book)
