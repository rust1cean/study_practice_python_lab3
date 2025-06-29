import numpy as np
import pandas as pd

"""
Задание 1 (Вариант 2)

Напишите функцию, которая возвращает Series заполненный случайным
образом из 15 значений. При этом все элементы Series меньше среднего
арифметического заменить на заданное константное значение.
"""


def create_series():

    LOWEST: int = 10
    ARRAY_SIZE: int = 15
    MAX: int = 100

    random_nums = np.random.randint(
        # If `high` is None -> `low` is `high`
        # `high` is None by default.
        low=MAX,
        size=ARRAY_SIZE,
    )
    artithmetic_mean = random_nums.mean()
    random_nums = np.array(
        list(map(lambda x: LOWEST if x < artithmetic_mean else x, random_nums))
    )
    series = pd.Series(random_nums)

    return series


def main():
    try:
        print(create_series())

    except ValueError:
        print("Expected number, got string.")


if __name__ == "__main__":
    main()
