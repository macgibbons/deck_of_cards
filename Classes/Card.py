class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
    ]

    def __init__(self, val, suit):
        if suit in Card.suits:
            self.suit = suit
        else:
            raise ValueError(f"{suit} is not a valid suit")
        if val in Card.card_values:
            self.val = val
        else:
            raise ValueError(f"{val} is not a valid card value")
    def __repr__(self):
        return f"{self.val} of {self.suit}"



