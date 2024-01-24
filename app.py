from deck import Deck
from card import Card
from constans import SUITES, VALUES

def fillPokerDeck():
    pokerDeck = Deck()  
    for suite in SUITES:
        for value in VALUES:
            pokerDeck.addCard(Card(suite, value))
    return pokerDeck
    

def main():
    pokerDeck = fillPokerDeck()
    print("\nstarting Deck:\n")
    pokerDeck.displayDeck()
    pokerDeck.shuffleDeck()
    print("\nAfter Shuffling:\n")
    pokerDeck.displayDeck()

if __name__ == '__main__':
    main()
