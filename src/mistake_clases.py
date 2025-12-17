from src.books import Book, BookCollection, Library, IndexDict


class BookCollectionMistake1(BookCollection):
    def add_book(self, book: Book) -> None:
        """метод для добавления книги в коллекцию
        ЗАБЫТА РЕАЛИЗАЦИЯ
        Args:
            book (Book): книга
        """
        pass


class LibraryMistake1(Library):
    def __init__(self) -> None:
        super().__init__()
        self.book_collection = BookCollectionMistake1()


class BookMistake2(Book):
    def __eq__(self, other: object) -> None:
        """
        НЕРЕАЛИЗОВАН
        """
        pass


class BookCollectionMistake2(BookCollection):
    def __eq__(self, other: object) -> bool:
        """
        НЕВЕРНАЯ РЕАЛИЗАЦИЯ
        Args:
            other (object): обьект для сравнения

        Returns:
            bool: True если содержимое коллекций одинаковое
        """
        if not isinstance(other, BookCollection):
            return False
        return self._items == other._items


class BookCollectionMistake3(BookCollection):
    def __getitem__(self, key: int | slice):
        if isinstance(key, int):
            if key < 0 or key >= len(self._items):
                raise IndexError(
                    "Ошибка: попытка обратиться по несуществующему индексу")
            return self._items[key]
        if isinstance(key, slice):
            # возвращает не обьект BookCollection, а сам список
            return self._items[key]
        raise TypeError(
            f"Ошибка: тип должен быть int или slice а не {type(key)}")


class BookCollectionMistake4(BookCollection):
    def __init__(self, items=[]) -> None:
        self._items = items  # type: ignore


class IndexDictMistake5(IndexDict):
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
            return self._years.get(criteria_value, None)  # type: ignore

        else:
            raise ValueError(
                f"Ошибка: неизвестный критерий для поиска {criteria_key}")


class LibraryMistake5(Library):
    def __init__(self) -> None:
        super().__init__()
        self.index_dict = IndexDictMistake5()
