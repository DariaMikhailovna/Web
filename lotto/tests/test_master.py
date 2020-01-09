import pytest
import import_src
import random
from master import Master

master = Master()


def test_next_number():
    def test(seed):
        random.seed(seed)
        numbers = []
        for i in range(10):
            number = master.next_number()
            assert type(number) is int
            assert 0 < number < 91
            assert number not in numbers
            numbers.append(number)
    for i in range(8):
        test(i)


def test_get_tickets():
    def test(seed):
        random.seed(seed)
        tickets = master.get_tickets()
        assert len(tickets) == 2
        assert tickets[0].numbers != tickets[1].numbers

    for i in range(10):
        test(i)
