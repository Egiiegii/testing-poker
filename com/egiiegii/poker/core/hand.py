from typing import List

from com.egiiegii.poker.core.dataclasses import Card

HAND_MAX = 5


class Hand:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card):
        self.cards.append(card)
        if len(self.cards) > HAND_MAX:
            raise RuntimeError("Card over 5")

    def find_score(self):
        return max(self.cards)

    def get_card_name(self):
        return [card.name for card in self.cards]
