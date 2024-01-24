import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)
    
    def shuffleDeck(self):
        random.shuffle(self.cards)

    def displayDeck(self):
        for index, card in enumerate(self.cards):
            print(f"{index+1}° card {card.suit} {card.value}")