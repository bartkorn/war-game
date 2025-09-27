from war_game.inventory.stack import Stack


class Player:

    def __init__(self, stack: Stack):
        self._cards = stack

    @property
    def cards(self) -> Stack:
        return self._cards

    def has_cards(self) -> bool:
        return self._cards.count_cards() > 0

    def shuffle_deck(self) -> None:
        self._cards.shuffle_deck()
