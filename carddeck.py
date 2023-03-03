import random

class DiscardPile:
    def __init__(self, *, show_top_card=False):
        self._cards = []
        self._show_top = show_top_card
        self.unfreeze()

    def freeze(self):
        self._frozen = True

    def unfreeze(self):
        self._frozen = False

    def add(self, card):
        self._cards.append(card)

    def remove(self):
        if not self._frozen:
            return self._cards.pop()
        else:
            raise Exception("Discard pile is frozen")

    def show_top(self):
        if not self._show_top:
            raise Exception("This game does not support viewing top card of discard pile")
        return self._cards[-1]


class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit


    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        # Card('rank', 'suit')
        return f"Card('{self.rank}', '{self.suit}')"

class CardDeck:  # inherits from 'object'
    CLUB = '\u2663'
    DIAMOND = '\u2666'
    HEART = '\u2665'
    SPADE = '\u2660'
    SUITS = CLUB, DIAMOND, HEART, SPADE
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __str__(self):
        return type(self).__name__

    def __init__(self, dealer):   # constructor
        self._dealer = dealer  # store data in instance
        self._make_deck()

    def __len__(self):
        return len(self.cards)

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def _spam(self):  # private/protected
        pass

    def get_dealer(self):  # getter method
        return self._dealer

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0)

    @property
    def dealer(self):   # getter property
        return self._dealer
    # dealer = property(dealer)

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            type_name = type(dealer).__name__
            raise TypeError(f"Dealer must be str, not {type_name}")