def is_triplet(a, b, c):
    a, b, c = sorted([a, b, c])
    return a ** 2 + b ** 2 == c ** 2


def find_special_triplet(sum_):
    for a in range(1, sum_ - 1):
        for b in range(a, sum_):
            c = sum_ - a - b
            if is_triplet(a, b, c):
                return a, b, c


a, b, c = find_special_triplet(1000)
print(a, b, c)
print(a * b * c)
