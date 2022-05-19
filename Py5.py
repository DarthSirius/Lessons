# Объявляем функцию для расчёта суммы вклада
# Аргумент years принимает число лет, на которое рассчитан вклад
def deposit_years(money, interest, years):
    interest = 1 + interest/100
    # Вместо while используем цикл for с range
    for year in range(years):
        money = round(interest * money, 2)
        # Выдаём полученную сумму вклада
        yield money
bank3 = deposit_years(10000, 10, 3)
sums = list(bank3)
print(sums)

stroka = "adddddaabaaaa"

def gen(str):
    max_c = 0
    counter = 1
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            counter += 1
        else:
            counter = 1
        if counter > max_c:
            max_c = counter
    return max_c
print(gen(stroka))
