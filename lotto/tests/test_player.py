import pytest
import import_src
from player import ComputerPlayer
from ticket import Ticket


def test_move():
    player = ComputerPlayer(Ticket())
    for i in range(len(player.ticket.numbers)):
        for j in range(len(player.ticket.numbers[i])):
            if type(player.ticket.numbers[i][j]) == int:
                player.move(player.ticket.numbers[i][j])
                assert player.ticket.numbers[i][j] == 'XX'
