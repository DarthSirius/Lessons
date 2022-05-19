#ваш код здесь
squares_generator = (x**2 for x in range(1, 11))
print(type(squares_generator))
print(squares_generator)

for _ in range(5):
    print(next(squares_generator))