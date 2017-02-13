"""
Posscode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode. For
example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
possible secret passcode of unknown length.
"""
from itertools import permutations
from time import time

start = time()

rules = set()
digits = set()
with open('p079_keylog.txt') as rule_list:
    for rule in rule_list:
        rules.update({tuple(rule[0:2]), tuple(rule[1:3])})
        digits.update(tuple(rule.strip()))


def check_rule(passcode, rule):
    return passcode.index(rule[0]) < passcode.index(rule[1])


assert check_rule('123', ('1', '3'))

for p in permutations(digits):
    if all(check_rule(p, rule) for rule in rules):
        print(''.join(p))
        break
print(time() - start)