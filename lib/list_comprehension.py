#!/usr/bin/env python3

def return_evens(num_list):
    pass
    result_list = [n for n in num_list if n % 2 == 0]
    return result_list


def make_exclamation(sentence_list):
    pass
    result_list = [f"{s}!" for s in sentence_list]
    return result_list

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))