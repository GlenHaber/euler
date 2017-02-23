"""
Anagramic squares

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number:
1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes
are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""
from collections import defaultdict

with open('p098_words.txt') as f:
    words = [word.replace('"', '') for word in f.read().split(',')]
words_by_length = defaultdict(list)
for word in words:
    words_by_length[len(word)].append(word)


def are_anagrams(a, b):
    return sorted(a) == sorted(b)


def find_anagram_pairs(words):
    pairs = []
    for i, a in enumerate(words, start=1):
        for b in words[i:]:
            if are_anagrams(a, b):
                pairs.append((a, b))
    return pairs


pairs = {k: find_anagram_pairs(v) for k, v in words_by_length.items()}
# Remove zero-length items
pairs = {k: v for k, v in pairs.items() if v}


def form(word):
    chars = sorted(set(word), key=lambda ch: word.index(ch))
    return tuple(chars.index(ch) for ch in word)


def gen_squares(limit):
    n = 1
    while n ** 2 < limit:
        yield n ** 2
        n += 1


squares = set(gen_squares(10 ** max(pairs)))
square_forms = defaultdict(set)
for s in squares:
    square_forms[form(str(s))].add(s)

biggest = 0
for length, ps in sorted(pairs.items(), reverse=True):
    for a, b in ps:
        form_a, form_b = form(a), form(b)
        if form_a not in square_forms or form_b not in square_forms:
            continue
        for option_a in square_forms[form_a]:
            mapping = dict(zip(a, str(option_a)))
            if mapping[b[0]] == '0':
                continue
            option_b = int(''.join(mapping[ch] for ch in b))
            if option_b in squares and max(option_a, option_b) > biggest:
                biggest = max(option_a, option_b)
print(biggest)
