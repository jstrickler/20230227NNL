from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck() # call in base class
        for i in range(2):
            joker = Card("Joker", "")
            self._cards.append(joker)



