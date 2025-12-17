import random
import time
from src.mistake_clases import LibraryMistake1
from src.constants import BOOKS_OBJECTS, POSSIBLE_EVENTS, EVENT_WEIGHTS


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """функция запуска симуляции работы библиотеки

    Args:
        steps (int, optional): количество шагов в симуляции. Defaults to 20.
        seed (int | None, optional): сид для генерации одних и тех же событий. Defaults to None.
    """

    if seed is not None:
        random.seed(seed)
    rng = random.Random(seed)

    lib = fill_the_lib_randomly()
    for _ in range(steps):
        event = rng.choices(POSSIBLE_EVENTS, EVENT_WEIGHTS)[0]
        print(f"Текущее состояние библиотеки:\n {lib.show_lib()}\n")
        time.sleep(2)

        try:
            if event == POSSIBLE_EVENTS[0]:
                book = rng.choice(BOOKS_OBJECTS)
                lib.add_book(book)
                print(f"Книга {book} добавлена в библиотеку\n")
            elif event == POSSIBLE_EVENTS[1]:
                book_to_del = rng.choice(BOOKS_OBJECTS)
                lib.remove_book(book_to_del)
                print(f"Книга {book_to_del} удалена из библиотеки\n")
            elif event == POSSIBLE_EVENTS[2]:
                if lib:
                    search_key = input(
                        "Введите критерий поиска (year, author, isbn): \n")
                    search_value = input(
                        f"Введите значение для поиска по {search_key}: \n")
                    result = lib.search_by_criteria(search_key, search_value)
                    if result:
                        print(
                            f'Книги,найденные по критерию "{search_key}" и значению "{search_value}" - {result}\n')
                    else:
                        print(
                            f'Книги по критерию "{search_key}" и значению "{search_value}" не найдены\n ')
            elif event == POSSIBLE_EVENTS[3]:
                lib.clear_lib()
                print("Библиотека очищена\n")
            elif event == POSSIBLE_EVENTS[4]:
                book = rng.choice(BOOKS_OBJECTS)
                result = lib.search_book(book)
                if result:
                    print(
                        f"Попытка найти книгу{book}: результат -  книга найдена!!!\n")
                else:
                    print(
                        f"Попытка найти книгу{book}: результат -  нет в библиотеке\n")
        except Exception as e:
            print(e)


def fill_the_lib_randomly(books_number: int = 10, seed: int | None = None) -> LibraryMistake1:
    """заполняет библиотеку случайными книгами 
    НЕПРАВИЛЬНО ВЕРСИЯ ЗАПОЛНЕНИЯ БИБЛИОТЕКИ!!!!!!!!!

    Args:
        books_number (int, optional): начально еоличество книг в библиотеке. Defaults to 10.
        seed (int | None, optional): сид. Defaults to None.

    Returns:
        Library: обьект библиотеки
    """
    lib = LibraryMistake1()
    if seed is not None:
        random.seed(seed)
    rng = random.Random(seed)
    for _ in range(books_number):
        lib.add_book(rng.choice(BOOKS_OBJECTS))

    return lib
