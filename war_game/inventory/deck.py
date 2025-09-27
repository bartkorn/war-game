import random
from war_game.inventory.card import Card


class Deck:

    def __init__(self, suits: tuple, ranks: tuple, values: tuple):
        self.all_cards: list[Card] = []
        for suit in suits:
            for rank in ranks:
                if suit in ["♥", "♦"]:
                    self.all_cards.append(Card(suit, rank, values[rank], "red"))
                else:
                    self.all_cards.append(Card(suit, rank, values[rank], "black"))

    def shuffle(self) -> None:
        random.shuffle(self.all_cards)

    def split(self) -> tuple:
        return self.all_cards[:len(self.all_cards)//2], self.all_cards[len(self.all_cards)//2:len(self.all_cards)]
