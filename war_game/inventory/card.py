class Card:

    def __init__(self, suit: str, rank: str, value: int, color: str):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.color = color

    def __str__(self) -> str:
        return f"{self.suit} {self.rank}"
