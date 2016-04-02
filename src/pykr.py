import random

suits = ["Hearts","Diamonds","Clubs","Spades"]
ranks = ["Deuce","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        return "deck with " + str(len(self.cards)) + " cards"

    def random_card(self):
        x = random.randint(1, len(self.cards))
        card = self.cards[x-1]
        self.cards.remove(card)
        return card


class Card: 
    def __init__(self, suit, rank):
        self.suit = suit     
        self.rank = rank
    
    def __str__(self):
        return self.name()

    def name(self):
        return self.rank + " of " + self.suit

def run():
    deck = Deck()
    print deck.random_card()
    print deck.random_card()


if __name__ == "__main__":
    run()





