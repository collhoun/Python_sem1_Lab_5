import pytest
from src.books import BookCollection


def test_empty_coll_init():
    collection = BookCollection()
    assert len(collection) == 0
    assert collection.is_empty()


def test_len_empty_collection():
    collection = BookCollection()
    assert len(collection) == 0


def test_collection_init_with_items(book_1, book_2):
    books = [book_1, book_2]
    collection = BookCollection(books)
    assert len(collection) == 2
    assert not collection.is_empty()


def test_add_many_books(book_1, book_2, book_3):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(book_2)
    collection.add_book(book_3)
    assert len(collection) == 3
    assert book_1 in collection and book_2 in collection and book_3 in collection


def test_add_double_books(book_1):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(book_1)
    assert len(collection) == 2


def test_add_diffetn_books_types(book_1, electronic_book, student_book):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(electronic_book)
    collection.add_book(student_book)
    assert len(collection) == 3


def test_remove_exist_book(book_1, book_2):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(book_2)
    collection.remove_book(book_1)
    assert len(collection) == 1
    assert book_1 not in collection
    assert book_2 in collection


def test_remove_nonexistent_bookr(book_1, book_2):
    collection = BookCollection()
    collection.add_book(book_1)
    with pytest.raises(ValueError) as e:
        collection.remove_book(book_2)
    assert f"Элемента {book_2} не в коллекции" == e.value.args[0]


def test_remove_from_empty_collection(book_1):
    collection = BookCollection()
    with pytest.raises(ValueError) as e:
        collection.remove_book(book_1)
    assert f"Элемента {book_1} не в коллекции" == e.value.args[0]


def test_remove_one_duplicate(book_1):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(book_1)
    collection.remove_book(book_1)
    assert len(collection) == 1
    assert book_1 in collection


def test_getitem_by_valid_index(book_1, book_2):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(book_2)
    assert collection[0] == book_1
    assert collection[1] == book_2


def test_getitem_by_invalid_index(book_1):
    collection = BookCollection()
    collection.add_book(book_1)
    with pytest.raises(IndexError) as e:
        _ = collection[1000]
    assert "Ошибка: попытка обратиться по несуществующему индексу" == e.value.args[0]


def test_getitem_by_negative_index(book_1):
    collection = BookCollection()
    collection.add_book(book_1)
    with pytest.raises(IndexError):
        _ = collection[-1]


def test_getitem_by_invalid_type(book_1):
    collection = BookCollection()
    collection.add_book(book_1)
    with pytest.raises(TypeError) as e:
        _ = collection[collection]  # type: ignore
    assert f"Ошибка: тип должен быть int или slice а не {type(collection)}" == e.value.args[
        0]


def test_getitem_slice(book_1, book_2, book_3):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(book_2)
    collection.add_book(book_3)

    sliced = collection[0:2]
    assert isinstance(sliced, BookCollection)
    assert len(sliced) == 2
    assert sliced[0] == book_1
    assert sliced[1] == book_2


def test_setitem_val_index(book_1, book_2):
    collection = BookCollection()
    collection.add_book(book_1)
    collection[0] = book_2
    assert collection[0] == book_2


def test_setitem_out_of_range(book_1, book_2):
    collection = BookCollection()
    collection.add_book(book_1)
    with pytest.raises(IndexError):
        collection[10] = book_2


def test_removes_all_books(book_1, book_2, book_3):
    collection = BookCollection()
    collection.add_book(book_1)
    collection.add_book(book_2)
    collection.add_book(book_3)

    collection.clear_books()
    assert len(collection) == 0
    assert collection.is_empty()


def test_clear_empty_coll():
    collection = BookCollection()
    collection.clear_books()
    assert len(collection) == 0


def test_not_contains_nonexistent_book(book_1, book_2):
    collection = BookCollection()
    collection.add_book(book_1)
    assert book_2 not in collection


def test_is_empty_on_empty_coll():
    collection = BookCollection()
    assert collection.is_empty()


def test_len_non_empty_coll(books_list):
    collection = BookCollection()
    for book in books_list:
        collection.add_book(book)
    assert len(collection) == len(books_list)


def test_equal_empty_colls():
    col1 = BookCollection()
    col2 = BookCollection()
    assert col1 == col2


def test_equal_collections_with_same_books(book_1, book_2):
    col1 = BookCollection()
    col1.add_book(book_1)
    col1.add_book(book_2)

    col2 = BookCollection()
    col2.add_book(book_1)
    col2.add_book(book_2)

    assert col1 == col2


def test_not_equal_colls(book_1, book_2, book_3):
    col1 = BookCollection()
    col1.add_book(book_1)

    col2 = BookCollection()
    col2.add_book(book_2)
    col2.add_book(book_3)

    assert col1 != col2


def test_not_equal_with_diff_type(book_1):
    collection = BookCollection()
    collection.add_book(book_1)
    assert collection != [book_1]
    assert collection != book_1
