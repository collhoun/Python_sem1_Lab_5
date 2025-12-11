import pytest
from src.books import Book, IndexDict


def test_init_creates_indexes():
    index_dict = IndexDict()
    assert len(index_dict['isbn']) == 0
    assert len(index_dict['author']) == 0
    assert len(index_dict['year']) == 0


def test_add_some_books_same_author(book_2, book_3):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_2)
    index_dict.add_to_indexes(book_3)
    assert len(index_dict['author']['Фёдор Достоевский']) == 2
    assert book_2 in index_dict['author']['Фёдор Достоевский']
    assert book_3 in index_dict['author']['Фёдор Достоевский']


def test_add_books_same_year(book_1):
    book_same_year = Book("Новая книга", "Другой автор",
                          1863, "Жанр", "isbn-123")
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    index_dict.add_to_indexes(book_same_year)
    assert len(index_dict['year'][1863]) == 2


def test_add_duplicate_isbn_overwrites(book_1):
    duplicate_book = Book(
        "другое название", "другой автор", 2020, "Жанр", book_1.isbn)
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    index_dict.add_to_indexes(duplicate_book)
    assert index_dict['isbn'][book_1.isbn].title == "другое название"


def test_remove_existing_book(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    index_dict.remove_from_indexes(book_1)

    assert book_1.isbn not in index_dict['isbn']
    assert book_1.author not in index_dict['author']
    assert book_1.year not in index_dict['year']


def test_remove1(book_2):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_2)
    index_dict.remove_from_indexes(book_2)

    assert book_2.author not in index_dict['author']


def test_remove2(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    index_dict.remove_from_indexes(book_1)

    assert book_1.year not in index_dict['year']


def test_remove_one_of_some_same_author(book_2, book_3):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_2)
    index_dict.add_to_indexes(book_3)
    index_dict.remove_from_indexes(book_2)

    assert book_2.author in index_dict['author']
    assert len(index_dict['author']['Фёдор Достоевский']) == 1
    assert book_3 in index_dict['author']['Фёдор Достоевский']


def test_remove_from_empty_indexes(book_1):
    index_dict = IndexDict()
    index_dict.remove_from_indexes(book_1)
    assert len(index_dict['isbn']) == 0


def test_search_by_isbn(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)

    result = index_dict.search_book('isbn', book_1.isbn)
    assert result == book_1


def test_search_by_isbn_not_found(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    result = index_dict.search_book('isbn', 'non-existent-isbn')
    assert result is None


def test_search_by_author(book_2, book_3):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_2)
    index_dict.add_to_indexes(book_3)

    result = index_dict.search_book('author', 'Фёдор Достоевский')
    assert book_2 in result
    assert book_3 in result


def test_search_by_author_not_found():
    index_dict = IndexDict()
    result = index_dict.search_book('author', 'Несуществующий автор')
    assert result is None


def test_search_by_year(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)

    result = index_dict.search_book('year', str(book_1.year))
    assert book_1 in result


def test_search_by_year_not_found():
    index_dict = IndexDict()
    result = index_dict.search_book('year', '99431243432123199')
    assert result is None


def test_search_invalid_criteria(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)

    with pytest.raises(ValueError) as e:
        index_dict.search_book('invalid_criteria', 'value')
    assert "Ошибка: неизвестный критерий для поиска invalid_criteria" == e.value.args[0]


def test_getitem_isbn(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)

    isbn_index = index_dict['isbn']
    assert book_1.isbn in isbn_index


def test_getitem_author(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    author_index = index_dict['author']
    assert book_1.author in author_index


def test_getitem_year(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    year_index = index_dict['year']
    assert book_1.year in year_index


def test_getitem_invalid_key():
    index_dict = IndexDict()

    with pytest.raises(KeyError) as e:
        _ = index_dict['fldksmf,dsnklmfsdkjnl']
    assert "Неизвестный ключ индекса: fldksmf,dsnklmfsdkjnl" == e.value.args[0]


def test_contains_exist_book(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    assert book_1 in index_dict


def test_not_contains_nonexist_book(book_1, book_2):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    assert book_2 not in index_dict


def test_clear_index_empties_all_indexes(book_1, book_2, book_3):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    index_dict.add_to_indexes(book_2)
    index_dict.add_to_indexes(book_3)

    index_dict.clear_index()

    assert len(index_dict['isbn']) == 0
    assert len(index_dict['author']) == 0
    assert len(index_dict['year']) == 0


def test_add_and_search_some_books(book_1, book_2, book_3, electronic_book):
    """Тест: добавление и поиск нескольких книг"""
    index_dict = IndexDict()
    books = [book_1, book_2, book_3, electronic_book]

    for book in books:
        index_dict.add_to_indexes(book)

    found_isbn = index_dict.search_book('isbn', book_1.isbn)
    assert found_isbn == book_1

    year_1863_books = index_dict.search_book('year', '1863')
    assert book_1 in year_1863_books


def test_year_by_search(book_1):
    index_dict = IndexDict()
    index_dict.add_to_indexes(book_1)
    result = index_dict.search_book('year', '1863')
    assert result is not None
    assert book_1 in result
