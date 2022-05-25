"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def predict_number_less20(number: int = 1) -> int:
    """Угадываем число, ограничивая рамки подбора методом деления интервала пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Переменная счетчик
    
    min_interval = 1 # Минимальное значение рассматриваемого интервала
    max_interval = 101 # Максимальное значение рассматриваемого интервала

    while True:
        count += 1
        mid_interval = int(( min_interval + max_interval ) / 2) # делим интервал поиска пополам

        if mid_interval > number: # если середина интервала больше числа, устанавливаем ее за верхнюю границу интервала
            max_interval = mid_interval
        elif mid_interval < number: # если середина интервала меньше числа, устанавливаем ее за нижнюю границу интервала
            min_interval = mid_interval
        else:
            break

    return count


def score_game(game_core_v2) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_number_less20(number)) # добавляем в список количество попыток

    score = int(np.mean(count_ls)) # вычисляем среднее арифметическое списка
    print(f"Наш алгоритм угадывает число в среднем за:{score} попыток")
    
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_number_less20)
