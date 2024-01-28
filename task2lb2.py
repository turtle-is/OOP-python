"""Написать класс Library, конструктор которого будет инициализировать следующие атрибуты:

books - Список книг
Конструктор должен принимать необязательный аргумент со значением по умолчанию. Если пользователь его не передал, то библиотека инициализируется с пустым списком книг.

В классе должен быть объявлен метод get_next_book_id.
Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
Если книг в библиотеке нет, то вернуть 1.
Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.

В классе должен быть объявлен метод get_index_by_book_id.
Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
Если книга существует, то вернуть индекс из списка.
Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"

В конструкторе класса Library для аргумента books используйте аргумент по умолчанию
Вспомните какая встроенная функция, умеет возвращать пары индекс-значение от последовательности."""


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1]["id"] + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book["id"] == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == "__main__":
    # Создаем объект класса Library
    library = Library()

    # Добавляем несколько книг
    library.books.append({"id": 1, "title": "Book 1"})
    library.books.append({"id": 2, "title": "Book 2"})
    library.books.append({"id": 3, "title": "Book 3"})

    # Проверяем метод get_next_book_id
    next_book_id = library.get_next_book_id()
    print(f"Следующий идентификатор для книги: {next_book_id}")

    # Проверяем метод get_index_by_book_id
    book_id = 2
    book_index = library.get_index_by_book_id(book_id)
    print(f"Индекс книги с идентификатором {book_id}: {book_index}")
     
     
