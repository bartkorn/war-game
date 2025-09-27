from war_game.inventory.stack import Stack
from war_game.inventory.player import Player
from war_game.inventory.card import Card
from war_game.inventory.deck import Deck
from war_game.utils.printer import Printer
import war_game.config as config

printer = Printer()


def game():

    player1, player2, stack = initiate()

    is_war = False
    rounds = 0

    while player1.has_cards() and player2.has_cards():
        rounds += 1

        is_war = round(player1, player2, stack, rounds)

        while is_war and player1.has_cards() and player2.has_cards():
            rounds += 1

            stack.add_cards([player1.cards.get_one(), player2.cards.get_one()])
            if not player1.has_cards() or not player2.has_cards():
                break
            is_war = round(player1, player2, stack, rounds, is_war)

    score = f"Player 1 has [{player1.cards.count_cards()}] cards, while Player 2 has [{player2.cards.count_cards()}] cards."
    winner = " Player 1 won !" if player1.cards.count_cards() > player2.cards.count_cards() else " Player 2 won !"
    print(score + winner)


def contest(card1: Card, card2: Card, stack: Stack, round_number: int, in_war = False):

    playing_cards = [card1, card2]
    current_stack = []

    if card1.value > card2.value:
        printer.print(card1,card2, round_number, "P1 wins !")
        if in_war:
            current_stack = stack.purge()
        return False, (current_stack + playing_cards, None, None)
    elif card1.value < card2.value:
        printer.print(card1,card2, round_number, "P2 wins !")
        if in_war:
            current_stack = stack.purge()
        return False, (None, current_stack + playing_cards, None)
    else:
        printer.print(card1,card2, round_number, "War !")
        return True, (None, None, playing_cards)


def round(player1: Player, player2: Player, stack: Stack, round_number: int, in_war = False) -> bool:
    war, result = contest(player1.cards.get_one(), player2.cards.get_one(), stack, round_number, in_war)
    player1.cards.add_cards(result[0])
    player2.cards.add_cards(result[1])
    stack.add_cards(result[2])
    return war


def initiate() -> tuple[Player, Player, Stack]:

    deck = Deck(config.SUITS, config.RANKS, config.VALUES)
    deck.shuffle()

    stack1 = Stack()
    stack2 = Stack()
    stack1.add_cards(deck.split()[0])
    stack2.add_cards(deck.split()[1])

    player1 = Player(stack1)
    player2 = Player(stack2)
    stack = Stack()

    player1.shuffle_deck()
    player2.shuffle_deck()

    return player1, player2, stack


if __name__ == "__main__":
    game()