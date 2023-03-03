from carddeck import CardDeck, DiscardPile
from jokerdeck import JokerDeck


# client code

d1 = CardDeck('Bruce')
d2 = CardDeck('Clark')

print(d1)    # print(str(d1))
#   str(d1) ==>  CardDeck.__str__(d1)

# NAUGHTY!!
# print(f"d1._dealer: {d1._dealer}")

dealer = d1.get_dealer()
print(f"dealer: {dealer}")

print(f"d1.dealer: {d1.dealer}")

d1.dealer = "Tony"
print(f"d1.dealer: {d1.dealer}")

try:
    d1.dealer = 1234
except TypeError as err:
    print(err)
else:
    print(f"d1.dealer: {d1.dealer}")

d1.shuffle()
print(f"d1.cards: {d1.cards}")

dp = DiscardPile(show_top_card=True)
for i in range(5):
    card = d1.draw()
    print(card.rank, card.suit)
    dp.add(card)

print()

x = dp.remove()
print(f"x: {x}")
x = dp.remove()
print(f"x: {x}")

print(f"dp.show_top(): {dp.show_top()}")
print('-' * 60)

j1 = JokerDeck('Jimmy')
j1.shuffle()
print(f"j1: {j1}")
print(f"j1.cards: {j1.cards}")

for i in range(5):
    d = j1.draw()
    print(d.rank, d.suit)
print()

print(f"len(d1): {len(d1)}")
print(f"len(j1): {len(j1)}")


