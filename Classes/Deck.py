from Classes.Card import Card
from random import shuffle

class Deck: 

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
              for card in Card.card_values:
                    self.cards.append(Card(card, suit))
        
    def __repr__(self):
        return f'deck of {len(self.cards)} cards' 

    def count(self):
        return len(self.cards)          

    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealt!")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)
        
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("you must have a full deck to shuffle")
        shuffle(self.cards)
        