"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v2(number: int = 1) -> int:
    """Угадываем число ограничивая рамки подбора

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Переменная счетчик
    
    min = 1 # Минимальное значение рассматриваемого интервала
    max = 101 # Максимальное значение рассматриваемого интервала

    while True:
        count += 1
        mid = int(( min + max ) / 2)

        if mid > number:
            max = mid
        elif mid < number:
            min = mid
        else:
            break

    return count


def score_game(game_core_v2) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v2(number))

    score = int(np.mean(count_ls))
    print(count_ls)
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v2)
