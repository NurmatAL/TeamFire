from random import shuffle
from pprint import pprint


card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['червы', 'бубны', 'трефы', 'пики']

class DeckOfCards:

  def __init__(self, number):
    self.suit, self.value = divmod(number, 13)

  def __str__(self):
    return suit[self.suit] + ' ' + card[self.value]

  def __repr__(self):
    return str(self)


class Deck:

  singleton = None

  def __new__(cls):
    if cls.singleton:
      return cls.singleton
    else:
      obj = super().__new__(cls)
      cls.singleton = obj
      return obj

  def __init__(self):
    self.cards = [DeckOfCards(i) for i in range(52)]
    self.shuffle()

  def __iter__(self):
    return iter(self.cards)

  def shuffle(self):
    shuffle(self.cards)

  def __str__(self):
    return f'{self.cards}'

  def remove(self, card):

        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

deck = Deck()

pprint([card for card in deck])