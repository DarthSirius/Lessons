str_example = "Fibonacci numbers are strongly related to the golden ratio: Binet's formula expresses the nth Fibonacci number in terms of n and the golden ratio, and implies that the ratio of two consecutive Fibonacci numbers tends to the golden ratio as n increases."

def first_letters_counter(s):
    alphabet_str = "abcdefghijklmnopqrstuvwqyz"
    letters_dict = {letter: 0 for letter in alphabet_str}

    words_list = s.lower().split()
    for word in words_list:
        letters_dict[word[0]] += 1
    return letters_dict

print(first_letters_counter(str_example))