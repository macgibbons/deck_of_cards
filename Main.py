from Classes.Card import Card
from Classes.Deck import Deck

# instance of deck
deck = Deck()

# shuffle the deck
deck.shuffle()

# deal a single card
card = deck.deal_card()
print(card)

# deal a hand
hand = deck.deal_hand(5)
print(hand)