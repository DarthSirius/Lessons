# Из модуля time импортируем функцию time
from time import time
 
def time_decorator(func):
    def decorated_func(*args, **kwargs):
        # Получаем время на момент начала вычисления
        start = time()
        result = func(*args, **kwargs)
        # Получаем время на момент окончания вычисления
        end = time()
        # Считаем длительность вычисления
        delta = end - start
        # Печатаем время работы функции
        print("Runtime:", delta)
        return result
    return decorated_func

@time_decorator
def root(value, n=2):
    result = value ** (1/n)
    return result
 
print(root(81))


users_list = ['admin', 'ivan', 'ivan_ivan']

def deco(func):
    def wrapper():
        user = input('Enter username:')
        if user in users_list:
            print('OK!')
            func()
        else:
            print('User '+user+' not found!')
            return None
    return wrapper

@ deco
def get_data_from_database():
    print("Super secure data from database")

get_data_from_database()
