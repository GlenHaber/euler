"""
Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import string
from math import floor, sqrt


def is_triangle_number(num):
    n = floor(sqrt(2 * num))
    return n * (n + 1) == 2 * num


letter_values = {letter: score for score, letter in enumerate(string.ascii_uppercase, start=1)}


def word_score(word):
    return sum(letter_values[letter] for letter in word)


def is_triangle_word(word):
    return is_triangle_number(word_score(word))

print(is_triangle_word('SKY'))

with open('p042_words.txt') as f:
    words = (word.replace('"', '') for word in f.read().split(','))
    print(len([word for word in words if is_triangle_word(word)]))
