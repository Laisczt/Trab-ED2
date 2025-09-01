from enum import Enum
import random

class Suits(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

class Ranks(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.name.title()} of {self.suit.name.title()}"

cards = []
deck = []

def initCards():
    global cards
    for s in Suits:
        for r in Ranks:
            cards.append(Card(s,r))

def readCardsFromDeck():
    global deck
    for i in deck:
        print(str(i))



def main():
    global deck, cards
    initCards()
    deck = cards.copy()
    random.shuffle(deck)
    readCardsFromDeck()

if __name__ == "__main__":
    main()

