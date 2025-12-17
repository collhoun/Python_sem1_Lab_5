from src.mistake_clases import BookCollectionMistake2, BookMistake2, BookCollectionMistake3, BookCollectionMistake4, LibraryMistake5
from src.books import Book
from src.simulation import run_simulation


def mistake_1(steps: int = 5, seed: None | int = 1) -> None:
    run_simulation(steps, seed)


def mistake_2() -> None:
    book1 = BookMistake2("1984", "George Orwell", 1949,
                         "Dystopian", "1234567890")
    book2 = BookMistake2("1984", "George Orwell", 1949,
                         "Dystopian", "1234567890")
    book3 = BookMistake2("Brave New World", "Aldous Huxley",
                         1932, "Science Fiction", "0987654321")
    book4 = BookMistake2("Brave New World", "Aldous Huxley",
                         1932, "Science Fiction", "0987654321")
    book_collection1 = BookCollectionMistake2()
    book_collection2 = BookCollectionMistake2()
    book_collection1.add_book(book1)
    book_collection1.add_book(book3)
    book_collection2.add_book(book4)
    book_collection2.add_book(book2)
    print(book_collection2 == book_collection1)  # False


def mistake_3() -> None:
    book1 = Book("1984", "George Orwell", 1949, "Dystopian", "1234567890")
    book2 = Book("1984", "George Orwell", 1949, "Dystopian", "1234567890")
    book3 = Book("Brave New World", "Aldous Huxley",
                 1932, "Science Fiction", "0987654321")
    book4 = Book("Brave New World", "Aldous Huxley",
                 1932, "Science Fiction", "0987654321")
    book_collection1 = BookCollectionMistake3()
    book_collection1.add_book(book1)
    book_collection1.add_book(book3)
    book_collection1.add_book(book4)
    book_collection1.add_book(book2)
    new_coll = book_collection1[:3]
    new_coll.add_book(book1)  # type: ignore
    print(new_coll)


def mistake_4() -> None:
    book1 = Book("1984", "George Orwell", 1949, "Dystopian", "1234567890")
    book_collection1 = BookCollectionMistake4()
    book_collection2 = BookCollectionMistake4()
    book_collection1.add_book(book1)
    print(book_collection1)
    print(book_collection2)


def mistake_5() -> None:
    book1 = Book("1984", "George Orwell", 1949, "Dystopian", "1234567890")
    book2 = Book("Brave New World", "Aldous Huxley",
                 1932, "Science Fiction", "0987654321")
    book_lib = LibraryMistake5()
    book_lib.add_book(book1)
    book_lib.add_book(book2)
    year = input("Введите год по которому вы хотите найти книгу: ")
    print(book_lib.search_by_criteria('year', year))


if __name__ == '__main__':
    mistake_5()
