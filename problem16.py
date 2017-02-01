"""
Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
def digital_sum(n):
    return sum(map(int, str(n)))

if __name__ == '__main__':
    print(digital_sum(2 ** 15))
    print(digital_sum(2 ** 1000))