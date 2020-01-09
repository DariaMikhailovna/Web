import pytest
import import_src
from game import Game


def test_init():
    game = Game()
    assert game.win_state.value == 0
    assert len(game.players) == 2
    assert game.master is not None
