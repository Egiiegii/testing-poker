from typing import List
from collections import Counter
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
        # 2oos deesh ijil modnudig bugdin gargana
        # ter dundasa unduriig ni olno
        # undur modondeere one pair iin score iig nemne. +13
        counter = Counter(self.cards)
        pairs = []
        for (key, value) in counter.most_common():
            if value > 1:
                pairs.append(key)

        if len(pairs) > 0:
            score = max(pairs) + 13
        else:
            score = max(self.cards)
        return score

    def get_card_name(self):
        return [card.name for card in self.cards]
