from enum import Enum
import random
from collections import defaultdict


class WinState(Enum):
    NA = 0
    WIN = 1
    LOSE = 2


class Master:
    def __init__(self):
        self.valid_numbers = list(range(1, 90))
        self.curr_number = None

    def is_honest(self, numb):
        if numb == self.curr_number:
            return True
        else:
            return False

    def next_number(self):
        self.curr_number = random.choice(self.valid_numbers)
        self.valid_numbers.remove(self.curr_number)
        return self.curr_number

    def get_count_valid_numbers(self):
        return len(self.valid_numbers)

    @staticmethod
    def get_tickets(count):
        tickets = []
        while len(tickets) < count:
            ticket = Ticket()
            is_repeat = False
            for t in tickets:
                count_math = 0
                for numb in ticket.numbers:
                    if numb in t.numbers:
                        count_math += 1
                if count_math == 15:
                    is_repeat = True
                    break
            if not is_repeat:
                tickets.append(ticket)
        for ticket in tickets:
            var = [['a', 'b', 'c'] for _ in range(10)]
            for numb in ticket.numbers:
                if numb < 10:
                    i = (numb - 1) // 10
                else:
                    i = numb // 10
                tmp = random.choice(var[i])
                var[i].remove(tmp)
                index = ticket.grid.index(tmp) + 3 * (i + 1)
                if numb < 10:
                    numb = '0' + str(numb)
                else:
                    numb = str(numb)
                ticket.grid = ticket.grid[:index] + numb + ticket.grid[index + 2:]

        return tickets


class Player:
    def __init__(self, ticket):
        self.ticket = ticket

    def move(self, coords):
        self.ticket.cross_out(coords)


class Ticket:
    def __init__(self):
        self.numbers = []
        by_first_digit = defaultdict(int)
        valid_numbers = list(range(1, 90))
        while len(self.numbers) < 15:
            numb = random.choice(valid_numbers)
            if by_first_digit[numb // 10] < 3:
                by_first_digit[numb // 10] += 1
                valid_numbers.remove(numb)
                self.numbers.append(numb)
        with open('ticket.txt', 'r') as f:
            self.grid = f.read()

    def __str__(self):
        return self.grid

    def cross_out(self, coords):
        if coords[0] not in ['a', 'b', 'c'] or coords[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Вы ввели неверные координаты')
            return
        index = self.grid.index(coords[0]) + 3 * int(coords[1])
        numb = int(self.grid[index:index + 2])
        # if Master.is_honest(numb, self):
        #     self.numbers.remove(numb)
        self.grid = self.grid[:index] + 'XX' + self.grid[index + 2:]


class Game:
    def __init__(self):
        self.master = Master()
        tickets = Master.get_tickets(2)
        self.ticket = tickets[0]
        self.player = Player(tickets[1])
        self.win_state = WinState.NA

    def __str__(self):
        return 'Билет противника:' + '\n' + str(self.ticket) + '\n' + 'Ваш билет:' + '\n' + str(self.player.ticket)

    def move(self, coords):
        if coords != 0:
            self.player.move(coords)
        if self.master.curr_number in self.ticket.numbers:
            self.ticket.numbers.remove(self.master.curr_number)
            index = self.ticket.grid.index(str(self.master.curr_number))
            self.ticket.grid = self.ticket.grid[:index] + 'XX' + self.ticket.grid[index + 2:]
        if len(self.ticket.numbers) == 0:
            self.win_state = WinState.LOSE
        if len(self.player.ticket.numbers) == 0:
            self.win_state = WinState.WIN


def main():
    game = Game()
    print('Добро пожаловать в игру ЛОТО!')
    print('Сверху находится билет противника, а снизу Ваш')
    print('Я буду крутить барабан и печатать выпадающие числа')
    print('А Вы должны вводить координаты чисел, которые хотите зачеркнуть')
    print('(координаты вида а2: буква - строка, цифра - колонка')
    print('(напечатайте 0 если ничего не нужно зачеркивать)')
    print('По правилам, зачеркивать можно только выпавшие числа')
    print('Но Вы можете мухлевать, а я могу это заметить')
    print('Ну, поехали!')
    while True:
        if game.master.get_count_valid_numbers == 0:
            print('Числа в барабане кончились, ничья!')
            break
        if game.win_state == WinState.WIN:
            print('YOU WIN')
            break
        if game.win_state == WinState.LOSE:
            print('GAME OVER')
            break
        print(game)
        print(f'Следующее число: {game.master.next_number()}')
        coords = input('Введите координаты для зачеркивания: ')
        game.move(coords)


if __name__ == '__main__':
    main()
