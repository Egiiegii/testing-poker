import unittest
from unittest.mock import MagicMock

from com.egiiegii.poker.core.dataclasses import Card
from com.egiiegii.poker.logic.poker_game import PokerGame


class PokerGameTest(unittest.TestCase):
    def test_high_card(self):
        pick_card_mock = MagicMock()
        pick_card_mock.side_effect = [
            Card.ACE, Card.KING,
            Card.JACK, Card.QUEEN,
            Card.TEN, Card.NINE,
            Card.TWO, Card.TWO,
            Card.THREE, Card.THREE
        ]

        poker_game = PokerGame()
        poker_game.pick_card = pick_card_mock
        poker_game.shuffle()
        poker_game.print()
        reality = poker_game.winner()
        expect_len = 1
        expect = 0
        print(reality)
        assert len(reality) == expect_len
        assert reality[0] == expect
