scary_func = lambda num: 'divided by 2 and 3' \
    if num % 6 == 0 \
    else 'divided by 2' if num % 2 == 0 \
    else 'divided by 3' if num % 3 == 0 \
    else 'not divided by 2 nor 3'
print(scary_func(5679))