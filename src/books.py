
class Book:

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.genre: str = genre
        self.isbn: str = isbn

    def __str__(self) -> str:
        return (f"Book(title='{self.title}', author='{self.author}', "
                f"year={self.year}, genre='{self.genre}', isbn='{self.isbn}')")

    def __repr__(self) -> str:
        return (f"Book({self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn})")


class ElectronicBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, memory_weight: float) -> None:
        super().__init__(title, author, year, genre, isbn)
        self.memory_weight: float = memory_weight

    def __str__(self) -> str:
        return (f"ElectronicBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, genre='{self.genre}', isbn='{self.isbn}', weight='{self.memory_weight} MB')")

    def __repr__(self) -> str:
        return f"ElectonicBook({self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn}, {self.memory_weight})"


class StudentBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, subject: str, class_number: int) -> None:
        super().__init__(title, author, year, genre, isbn)
        self.subject: str = subject
        self.class_number: int = class_number

    def __str__(self) -> str:
        return (f"StudentBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, genre='{self.genre}', isbn='{self.isbn}'), subject='{self.subject}', class_number='{self.class_number}'")

    def __repr__(self) -> str:
        return f"StudentBook({self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn}, {self.subject}, {self.class_number})"


class BookCollection:
    def __init__(self, items: None | list = None) -> None:
        if items is None:
            self._items: list = []
        else:
            self._items = items

    def __getitem__(self, key: int | slice):
        if isinstance(key, int):
            if key < 0 or key >= len(self._items):
                raise IndexError(
                    "Ошибка: попытка обратиться по несуществующему индексу")
            return self._items[key]
        if isinstance(key, slice):
            return BookCollection(self._items[key])
        raise TypeError(
            f"Ошибка: тип должен быть int или slice а не {type(key)}")

    def __setitem__(self, index: int, value: Book) -> None:
        self._items[index] = value

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def add_book(self, book: Book) -> None:
        """метод для добавления книги в коллекцию

        Args:
            book (Book): книга
        """
        self._items.append(book)

    def remove_book(self, book: Book) -> None:
        """метод для удаления книги из коллекции

        Args:
            book (Book): книга, которую пользователь хочет удалить

        Raises:
            ValueError: ошибка, если книги для удаления не существует
        """
        if book not in self._items:
            raise ValueError(f"Элемента {book} не в коллекции")
        self._items.remove(book)

    def clear_books(self) -> None:
        """метод для отчистки коллекции
        """
        self._items = []

    def is_empty(self) -> bool:
        """проверяет пустая ли коллекция

        Returns:
            bool: True если коллекция пустая False иначе
        """
        return len(self._items) == 0

    def __contains__(self, item: Book) -> bool:
        return item in self._items

    def __eq__(self, other: object) -> bool:
        """сравнение двух коллекций по содержимому

        Args:
            other: другой объект

        Returns:
            bool: True если коллекции содержат одинаковые книги
        """
        if not isinstance(other, BookCollection):
            return False
        return self._items == other._items

    def __str__(self) -> str:
        return f'{self._items}'


class IndexDict:
    def __init__(self) -> None:
        self._isbns: dict[str, Book] = {}
        self._authors: dict[str, list[Book]] = {}
        self._years: dict[int, list[Book]] = {}

    def add_to_indexes(self, book: Book) -> None:
        """добавляет книжку в индексы

        Args:
            book (Book): книга
        """
        self._isbns[book.isbn] = book

        if book.author not in self._authors:
            self._authors[book.author] = []
        self._authors[book.author].append(book)

        if book.year not in self._years:
            self._years[book.year] = []
        self._years[book.year].append(book)

    def remove_from_indexes(self, book: Book) -> None:
        """удаление книги из индексов

        Args:
            book (Book): книга
        """
        if book.isbn in self._isbns:
            del self._isbns[book.isbn]

        if book.author in self._authors:
            self._authors[book.author].remove(book)
            if not self._authors[book.author]:
                del self._authors[book.author]

        if book.year in self._years:
            self._years[book.year].remove(book)
            if not self._years[book.year]:
                del self._years[book.year]

    def search_book(self, criteria_key: str, criteria_value: str):
        """метод для поиска книги по критерию и его значению

        Args:
            criteria_key (str): критерий поиска
            criteria_value (str): значение критерия поиска (например год выпуска, имя автора или идентификационный номер)

        Raises:
            TypeError: ошибка если год не целое число
            ValueError: ошибка если criteria_key неизвестный

        Returns:
            _type_: _description_
        """
        if criteria_key == 'isbn':
            return self._isbns.get(criteria_value, None)
        elif criteria_key == 'author':
            return self._authors.get(criteria_value, None)
        elif criteria_key == 'year':
            if not criteria_value.isdigit():
                raise TypeError("Год должен быть целым числом")
            return self._years.get(int(criteria_value), None)

        else:
            raise ValueError(
                f"Ошибка: неизвестный критерий для поиска {criteria_key}")

    def clear_index(self):
        """
        Очищает индексы

        """
        self._isbns.clear()
        self._authors.clear()
        self._years.clear()

    def __getitem__(self, key: str) -> dict:
        if key == 'isbn':
            return self._isbns

        elif key == 'author':
            return self._authors

        elif key == 'year':
            return self._years
        else:
            raise KeyError(f"Неизвестный ключ индекса: {key}")

    def __contains__(self, book: Book) -> bool:
        return book.isbn in self._isbns or (book.author in self._authors and book in self._authors[book.author]) or (book.year in self._years and book in self._years[book.year])


class Library:
    def __init__(self) -> None:
        self.book_collection = BookCollection()
        self.index_dict = IndexDict()

    def add_book(self, book: Book) -> None:
        """добавляет книгу в индексы

        Args:
            book (Book): книга для добавления
        """
        self.book_collection.add_book(book)
        self.index_dict.add_to_indexes(book)

    def remove_book(self, book: Book) -> None:
        """удаляет книгу из индексов

        Args:
            book (Book): книга для удаления

        Raises:
            ValueError: ошибка, если книги для удаления не существует
        """
        if book in self.book_collection and book in self.index_dict:
            self.book_collection.remove_book(book)
            self.index_dict.remove_from_indexes(book)
        else:
            raise ValueError(f"Невозжно удалить несуществующую книгу {book}")

    def search_by_criteria(self, criteria_key: str, criteria_value: str) -> Book | list[Book] | None:
        """поиск книги по заданным критериям

        Args:
            criteria_key (str): критерий поиска (isbn, author, year)
            criteria_value (str): значение для поиска

        Returns:
            Book | list[Book] | None: книга или список книг если найдены, иначе None
        """
        return self.index_dict.search_book(criteria_key, criteria_value)

    def __bool__(self) -> bool:
        """проверка пустая ли библиотека

        Returns:
            bool: True если библиотека не пустая
        """
        return len(self.book_collection) > 0

    def search_book(self, book: Book) -> Book | None:
        """поиск книги в библиотеке по объекту

        Args:
            book (Book): книга для поиска

        Returns:
            Book | None: книга если найдена, иначе None
        """
        if book in self.book_collection:
            return book
        return None

    def clear_lib(self) -> None:
        """очищает библиотеку
        """
        self.book_collection = BookCollection()
        self.index_dict = IndexDict()

    def show_lib(self) -> BookCollection:
        """возвращает коллекцию книг в библиотеке

        Returns:
            BookCollection: коллекция книг в библиотеке
        """
        return self.book_collection
