from src.simulation import run_simulation


def main() -> None:

    steps = 20
    print("Приветствую в симуляции управления библиотекой\nПо умолчанию количество шагов в первой симуляции равно 20")
    while steps:
        run_simulation(steps)
        try:
            steps = int(input(
                "Введите количество шагов в симуляции (для окончания программы введите 0): "))
        except TypeError:
            print("Количество шагов должно быть целым числом")


if __name__ == "__main__":
    main()
