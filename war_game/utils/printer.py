from rich.console import Console
from rich.text import Text
from war_game.inventory.card import Card

class Printer:

    def __init__(self):
        self.console = Console()

    def print(self, card1: Card, card2: Card, round_number: int, outcome: str):
        card1_text = Text()
        card1_text.append(card1.suit, style=card1.color)
        card1_text.append(" " + card1.rank)
        card2_text = Text()
        card2_text.append(card2.suit, style=card2.color)
        card2_text.append(" " + card2.rank)
        self.console.print(f"{round_number}) ", card1_text, " -- ", card2_text, f" {outcome} ")
