import pytest
import random
import import_src
from ticket import Ticket
from game import Game
from player import ComputerPlayer


@pytest.fixture()
def sample_ticket():
    random.seed(123)
    return Ticket()


@pytest.fixture()
def get_game():
    return Game()


@pytest.fixture()
def player():
    return ComputerPlayer(Ticket())
