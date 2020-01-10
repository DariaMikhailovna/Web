import pytest
import import_src
import random
from ticket import Ticket


def test_init():
    def test(seed):
        random.seed(seed)
        ticket = Ticket()
        assert ticket.numbers is not None
        valid_numbers = list(range(1, 91))
        valid_numbers.append(None)
        for numbers in ticket.numbers:
            for number in numbers:
                assert number in valid_numbers
                if number:
                    valid_numbers.remove(number)
        for numbers in ticket.numbers:
            assert numbers.count(None) == 4
        for k in range(9):
            for i in range(len(ticket.numbers)):
                if ticket.numbers[i][k]:
                    assert (k * 10) < ticket.numbers[i][k] <= (k * 10 + 10)

    for number in range(1000):
        test(number)


test_ticket = '''\
  +--+--+--+--+--+--+--+--+--+
a |05|17|..|..|42|..|69|..|86|
  +--+--+--+--+--+--+--+--+--+
b |07|20|23|..|..|51|..|..|84|
  +--+--+--+--+--+--+--+--+--+
c |06|13|21|..|..|..|62|72|..|
  +--+--+--+--+--+--+--+--+--+
    1  2  3  4  5  6  7  8  9 \
'''


def test_str():
    random.seed(123)
    ticket = Ticket()
    assert str(ticket) == test_ticket
