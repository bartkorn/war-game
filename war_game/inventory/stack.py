import random
from war_game.inventory.card import Card


class Stack:

    def __init__(self):
        self.cards: list[Card] = []

    def add_cards(self, cards: list[Card] or None) -> None:
        if cards:
            self.cards += cards

    def get_one(self) -> Card:
        return self.cards.pop()

    def has_cards(self) -> bool:
        return len(self.cards) > 0

    def shuffle_deck(self) -> None:
        random.shuffle(self.cards)

    def count_cards(self) -> int:
        return len(self.cards)

    def purge(self) -> list[Card]:
        cards = self.cards.copy()
        self.cards = []
        return cards
