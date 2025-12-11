import pytest
from src.books import Book, ElectronicBook, StudentBook


@pytest.fixture(scope='session')
def book_1():
    return Book("Война и мир", "Лев Толстой", 1863,
                "Роман-эпопея", "978-5-4472-3750-9")


@pytest.fixture(scope='session')
def book_2():
    return Book("Преступление и наказание", "Фёдор Достоевский",
                1866, "Психологический роман", "978-5-17-145155-1")


@pytest.fixture(scope='session')
def book_3():
    return Book("Братья Карамазовы", "Фёдор Достоевский",
                1880, "Философский роман", "978-5-17-136080-8")


@pytest.fixture(scope='session')
def electronic_book():
    return ElectronicBook("1984", "Джордж Оруэлл", 1949,
                          "Антиутопия", "978-5-04-103628-1", 1.2)


@pytest.fixture(scope='session')
def student_book():
    return StudentBook('Алгебра и начала анализа', 'Колягин', 2011,
                       'Учебник', '978-5-09-022250-1', 'Математика', 11)


@pytest.fixture(scope='session')
def books_list(book_1, book_2, book_3, electronic_book, student_book):
    return [book_1, book_2, book_3, electronic_book, student_book]
