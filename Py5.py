scary_func = lambda num: 'divided by 2 and 3' \
    if num % 6 == 0 \
    else 'divided by 2' if num % 2 == 0 \
    else 'divided by 3' if num % 3 == 0 \
    else 'not divided by 2 nor 3'
print(scary_func(5679))

full_func = lambda *args, **kwargs: (args, kwargs)
 
print(full_func(1,5,6,7,name='Ivan', age=25))
# Будет напечатано:
# ((1, 5, 6, 7), {'name': 'Ivan', 'age': 25})