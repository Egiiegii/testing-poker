"""
dataclasses.py contains the win or lose logic
"""
from typing import List

from com.egiiegii.poker.core.dataclasses import Card
from com.egiiegii.poker.core.hand import Hand, HAND_MAX
import random


class PokerGame(object):
    def __init__(self, player_number=2):
        self.player_number = player_number
        hands = []
        for _ in range(player_number):
            hands.append(Hand())
        self.hands = hands

    def shuffle(self):
        for i in range(HAND_MAX * self.player_number):
            self.hands[i % self.player_number].add_card(self.pick_card())

    def winner(self) -> List[int]:
        score = []
        for idx, hand in enumerate(self.hands):
            score.append(hand.find_score())
        max_score = max(score)
        return [i for i, j in enumerate(score) if j == max_score]

    def get_winner(self)-> str:
        winner_list = self.winner()
        if len(winner_list) == 1:
            return "Winner player {}".format(1)
        else:
            return "Tie player {}".format(" ".join(str(winner_list)))

    def print(self):
        for idx, hand in enumerate(self.hands):
            print("Player {}, hand: {}".format(idx, hand.get_card_name()))

    @classmethod
    def pick_card(cls):
        return random.choice(list(Card))


if __name__ == '__main__':
    game = PokerGame()
    game.shuffle()
    game.print()
    print(game.get_winner())
