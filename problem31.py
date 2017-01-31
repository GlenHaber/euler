"""
Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
values = [200, 100, 50, 20, 10, 5, 2]

i = 0
for two_pound in range(2):
    print(two_pound)
    total = 200 * two_pound
    for one_pound in range((200 - total) // 100 + 1):
        total = 200 * two_pound + 100 * one_pound
        for fifty_pence in range((200 - total) // 50 + 1):
            total = 200 * two_pound + 100 * one_pound + 50 * fifty_pence
            for twenty_pence in range((200 - total) // 20 + 1):
                total = 200 * two_pound + 100 * one_pound + 50 * fifty_pence + 20 * twenty_pence
                for ten_pence in range((200 - total) // 10 + 1):
                    total = 200 * two_pound + 100 * one_pound + 50 * fifty_pence + 20 * twenty_pence + 10 * ten_pence
                    for five_pence in range((200 - total) // 5 + 1):
                        total = 200 * two_pound + 100 * one_pound + 50 * fifty_pence + 20 * twenty_pence + 10 * ten_pence + 5 * five_pence
                        for two_pence in range((200 - total) // 2 + 1):
                            i += 1
print(i)
