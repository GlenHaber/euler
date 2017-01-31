"""
Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
of 192 and (1,2,3). The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5). What is the largest 1 to 9 pandigital
9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
# If n > 1, then at least two numbers need to form the product, meaning n is 4 digits and 2*n is 5 digits. This sets the
# integer's ceiling at 9999.
ceiling = 10000


def form_concatenated_product(n):
    s = ''
    i = 1
    while len(s) < 9:
        s += str(i * n)
        i += 1
    return int(s)


def is_pandigital(n):
    return sorted(str(n)) == list('123456789')


print(form_concatenated_product(192))
print(form_concatenated_product(9))

products = (form_concatenated_product(n) for n in range(1, ceiling))

print('Answer:', max(filter(is_pandigital, products)))
