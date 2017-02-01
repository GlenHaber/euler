"""
Poker hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights
beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then
highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

Hand    Player 1            Player 2            Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
        Pair of Fives       Pair of Eights

2       5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
        Highest card Ace    Highest card Queen

3       2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds

4       4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from collections import namedtuple

values = dict(zip('23456789TJQKA', range(2, 15)))

Card = namedtuple('Card', ['value', 'suit'])


def score_hand(cards):
    """Return a tuple with the hand type and tiebreaker score"""
    # Royal flush
    hand_values = [c.value for c in cards]
    hand_values = {c: hand_values.count(c) for c in hand_values}
    is_flush = len({c.suit for c in cards}) == 1
    is_straight = {v - min(hand_values) for v in hand_values} == {0, 1, 2, 3, 4}
    # All hands of the same type use the same for tiebreaker. Sort twice, once by value, then by count
    tiebreaker = sorted(sorted(hand_values.keys(), reverse=True), key=lambda k: hand_values[k], reverse=True)
    if is_flush and is_straight:
        if set(hand_values) == {values[v] for v in 'TJQKA'}:  # Royal flush
            return 9, tiebreaker
        else:  # Straight flush
            return 8, tiebreaker
    if max(hand_values.values()) == 4:  # Four of a kind
        return 7, tiebreaker
    if sorted(hand_values.values()) == [2, 3]:  # Full house
        return 6, tiebreaker
    if is_flush:  # Flush
        return 5, tiebreaker
    if is_straight:  # Straight
        return 4, tiebreaker
    if max(hand_values.values()) == 3:  # Three of a kind
        return 3, tiebreaker
    if list(hand_values.values()).count(2) == 2:  # Two pair
        return 2, tiebreaker
    if 2 in hand_values.values():  # One pair (actually "at least" one pair, but higher hands have already been checked
        return 1, tiebreaker
    return 0, tiebreaker


if __name__ == '__main__':
    test_hands = map(lambda hand: [Card(values[c[0]], c[1]) for c in hand.split()],
                     ['5H 5C 6S 7S KD 2C 3S 8S 8D TD',
                      '5D 8C 9S JS AC 2C 5C 7D 8S QH',
                      '2D 9C AS AH AC 3D 6D 7D TD QD',
                      '4D 6S 9H QH QC 3D 6D 7H QD QS',
                      '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'])
    wins = [0, 0]
    for hand in test_hands:
        p1 = score_hand(hand[:5])
        p2 = score_hand(hand[5:])
        if p1 > p2:
            wins[0] += 1
        else:
            wins[1] += 1
    assert wins == [3, 2]

    wins = [0,0]
    for deal in open('p054_poker.txt'):
        cards = [Card(values[c[0]], c[1]) for c in deal.split()]
        p1 = score_hand(cards[:5])
        p2 = score_hand(cards[5:])
        assert p1 != p2
        if p1 > p2:
            wins[0] += 1
        else:
            wins[1] += 1
    print(wins[0])
