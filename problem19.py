"""
Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Let's use the Doomsday algorithm!
from datetime import date


def doomsday(year):
    # Century - Only bother considering 1800 to 2199. Variable names taken from
    # https://en.wikipedia.org/wiki/Doomsday_rule#Finding_a_year.27s_Doomsday
    century, y = year // 100, year % 100
    try:
        anchor = {18: 5, 19: 3, 20: 2, 21: 0}[century]
    except KeyError:
        raise ValueError('Doomsday is too lazy for that year')
    a, b = y // 12, y % 12
    c = b // 4
    d = (a + b + c + anchor) % 7
    return d


def is_leap_year(year):
    return year % 400 == 0 or \
           year % 4 == 0 and not year % 100 == 0


def start_of_months(year):
    doom = doomsday(year)
    starts = [
        doom - (3 if is_leap_year(year) else 2),  # January 3rd, 4th on leap year
        doom - (0 if is_leap_year(year) else 6),  # Last day of February
        doom - 6,  # March 0
        doom - 3,  # 4/4
        doom - 8,  # 5-9
        doom - 5,  # 6/6
        doom - 10,  # 7/11
        doom,  # 8/8
        doom - 4,  # 9-5
        doom - 9,  # 10/10
        doom - 6,  # 11-7
        doom - 11  # 12/12
    ]
    return [s % 7 for s in starts]


sundays = [start_of_months(y).count(0) for y in range(1901, 2001)]
print(sum(sundays))

# ...or, using datetime library
print(sum([1 for month in range(1, 13) for year in range(1901, 2001) if date(year, month, 1).weekday() == 6]))
