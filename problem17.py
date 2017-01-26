"""
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total. If all the numbers from one to 1000 (one thousand) inclusize were written out in words, how many
letters would be used?
"""

ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {
    0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen',
    5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'
}
tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}


def word(number):
    s = ''
    digits = list(map(int, str(number)))
    try:
        s += ones[digits[-3]] + 'hundred'
        if any(digits[-2:]):
            s += 'and'
    except IndexError:
        pass
    # Special case: Teens
    try:
        if digits[-2] == 1:
            s += teens[digits[-1]]
        else:
            s += tens[digits[-2]] + ones[digits[-1]]
    except IndexError:
        s += ones[digits[-1]]
    return s


def number_length(number):
    return len(word(number).replace(' ', ''))


print(number_length(342))
print(number_length(115))

print(sum(number_length(n) for n in range(1, 1000)) + len('onethousand'))
