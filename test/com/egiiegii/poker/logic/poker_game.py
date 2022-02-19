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
        assert len(reality) == expect_len
        assert reality[0] == expect

    def test_high_card_tie(self):
        pick_card_mock = MagicMock()
        pick_card_mock.side_effect = [
            Card.ACE, Card.ACE,
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
        expect_len = 2
        expects = [0, 1]
        assert len(reality) == expect_len
        for expect in expects:
            assert expect in reality

    def test_high_card_one_pair_win(self):
        pick_card_mock = MagicMock()
        pick_card_mock.side_effect = [
            Card.ACE, Card.JACK,
            Card.JACK, Card.QUEEN,
            Card.TEN, Card.NINE,
            Card.TWO, Card.TWO,
            Card.THREE, Card.TWO
        ]

        poker_game = PokerGame()
        poker_game.pick_card = pick_card_mock
        poker_game.shuffle()
        poker_game.print()
        reality = poker_game.winner()
        expect_len = 1
        expect = 1
        assert len(reality) == expect_len
        assert reality[0] == expect

    def test_high_card_one_pair_win_2(self):
        pick_card_mock = MagicMock()
        pick_card_mock.side_effect = [
            Card.ACE, Card.JACK,
            Card.JACK, Card.QUEEN,
            Card.TEN, Card.NINE,
            Card.TEN, Card.TWO,
            Card.THREE, Card.TWO
        ]

        poker_game = PokerGame()
        poker_game.pick_card = pick_card_mock
        poker_game.shuffle()
        poker_game.print()
        reality = poker_game.winner()
        expect_len = 1
        expect = 0
        assert len(reality) == expect_len
        assert reality[0] == expect

    def test_high_card_one_pair_tie(self):
        pick_card_mock = MagicMock()
        pick_card_mock.side_effect = [
            Card.ACE, Card.JACK,
            Card.JACK, Card.QUEEN,
            Card.TEN, Card.TEN,
            Card.TEN, Card.TEN,
            Card.THREE, Card.TWO
        ]

        poker_game = PokerGame()
        poker_game.pick_card = pick_card_mock
        poker_game.shuffle()
        poker_game.print()
        reality = poker_game.winner()
        expect_len = 2
        expects = [0, 1]
        assert len(reality) == expect_len
        for expect in expects:
            assert expect in reality
