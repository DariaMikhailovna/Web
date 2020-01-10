import pytest
from fixtures import *


def test_init(get_game):
    assert get_game.win_state.value == 0
    assert len(get_game.players) == 2
    assert get_game.master is not None
