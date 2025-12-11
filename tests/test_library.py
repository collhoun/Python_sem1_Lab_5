import pytest
from src.books import Library, BookCollection, IndexDict


def test_init():
    lib = Library()
    assert isinstance(lib.book_collection, BookCollection)
    assert isinstance(lib.index_dict, IndexDict)
    assert len(lib.book_collection) == 0
    assert not lib


def test_add_some_books(book_1, book_2, book_3):
    lib = Library()
    lib.add_book(book_1)
    lib.add_book(book_2)
    lib.add_book(book_3)

    assert len(lib.book_collection) == 3
    assert all(book in lib.book_collection for book in [
        book_1, book_2, book_3])


def test_add_and_check_indexes(book_1):
    lib = Library()
    lib.add_book(book_1)
    assert book_1 in lib.book_collection
    assert book_1.isbn in lib.index_dict['isbn']
    assert book_1.author in lib.index_dict['author']
    assert book_1.year in lib.index_dict['year']


def test_add_duplicate_books(book_1):
    lib = Library()
    lib.add_book(book_1)
    lib.add_book(book_1)
    assert len(lib.book_collection) == 2


def test_remove_exist_book(book_1, book_2):
    lib = Library()
    lib.add_book(book_1)
    lib.add_book(book_2)
    lib.remove_book(book_1)
    assert len(lib.book_collection) == 1
    assert book_1 not in lib.book_collection
    assert book_2 in lib.book_collection


def test_remove_removes(book_1):
    lib = Library()
    lib.add_book(book_1)
    lib.remove_book(book_1)
    assert book_1 not in lib.book_collection
    assert book_1 not in lib.index_dict


def test_remove_nonexistent_book(book_1, book_2):
    lib = Library()
    lib.add_book(book_1)
    with pytest.raises(ValueError, match="Невозжно удалить"):
        lib.remove_book(book_2)


def test_remove_from_empty_library(book_1):
    lib = Library()
    with pytest.raises(ValueError):
        lib.remove_book(book_1)


def test_remove_only_from_collection_not_in_index(book_1, book_2):
    lib = Library()
    lib.add_book(book_1)
    lib.book_collection.add_book(book_2)

    with pytest.raises(ValueError):
        lib.remove_book(book_2)


def test_search_by_isbn_found(book_1):
    lib = Library()
    lib.add_book(book_1)

    result = lib.search_by_criteria('isbn', book_1.isbn)
    assert result == book_1


def test_search_by_isbn_not_found(book_1):
    lib = Library()
    lib.add_book(book_1)

    result = lib.search_by_criteria('isbn', 'non-existent')
    assert result is None


def test_search_by_author_found(book_2, book_3):
    lib = Library()
    lib.add_book(book_2)
    lib.add_book(book_3)

    result = lib.search_by_criteria('author', 'Фёдор Достоевский')
    assert book_2 in result
    assert book_3 in result


def test_search_by_author_not_found():
    lib = Library()
    result = lib.search_by_criteria('author', 'Несуществующий')
    assert result is None


def test_search_by_year_found(book_1):
    lib = Library()
    lib.add_book(book_1)
    result = lib.search_by_criteria('year', str(book_1.year))
    assert book_1 in result


def test_search_by_year_not_found():
    lib = Library()
    result = lib.search_by_criteria('year', '9999')
    assert result is None


def test_search_invalidd_criteria(book_1):
    lib = Library()
    lib.add_book(book_1)
    with pytest.raises(ValueError):
        lib.search_by_criteria('invalid', 'value')


def test_search_book_found(book_1):
    lib = Library()
    lib.add_book(book_1)
    result = lib.search_book(book_1)
    assert result == book_1


def test_search_book_not_found(book_1, book_2):
    lib = Library()
    lib.add_book(book_1)
    result = lib.search_book(book_2)
    assert result is None


def test_clear_removes_all_books(book_1, book_2, book_3):
    lib = Library()
    lib.add_book(book_1)
    lib.add_book(book_2)
    lib.add_book(book_3)
    lib.clear_lib()
    assert len(lib.book_collection) == len(lib.index_dict['isbn']) == len(
        lib.index_dict['author']) == len(lib.index_dict['year']) == 0


def test_clear_empty_library():
    lib = Library()
    lib.clear_lib()
    assert len(lib.book_collection) == 0


def test_bool_non_empty_library(book_1):
    lib = Library()
    lib.add_book(book_1)
    assert lib


def test_show_lib_returns_collection(book_1):
    lib = Library()
    lib.add_book(book_1)
    collection = lib.show_lib()
    assert book_1 in collection


def test_library(book_1, book_2):
    lib = Library()
    lib.add_book(book_1)
    lib.add_book(book_2)

    lib.add_book(book_1)
    assert len(lib.book_collection) == 3

    lib.remove_book(book_1)
    assert len(lib.book_collection) == 2

    found = lib.search_by_criteria('isbn', book_1.isbn)
    assert found is None

    lib.clear_lib()
    assert not lib

    result = lib.search_by_criteria('isbn', book_1.isbn)
    assert result is None


def test_book_types_in_library(book_1, electronic_book, student_book):
    lib = Library()
    lib.add_book(book_1)
    lib.add_book(electronic_book)
    lib.add_book(student_book)

    assert len(lib.book_collection) == 3

    found_usualt = lib.search_by_criteria('isbn', book_1.isbn)
    found_electronic = lib.search_by_criteria('isbn', electronic_book.isbn)
    found_student = lib.search_by_criteria('isbn', student_book.isbn)

    assert found_usualt == book_1
    assert found_electronic == electronic_book
    assert found_student == student_book
