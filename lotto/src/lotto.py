from enum import Enum
import random


class WinState(Enum):
    NA = 0
    WIN = 1
    LOSE = 2
    DISQUALIFIED = 3


grid_pattern = '''\
  +--+--+--+--+--+--+--+--+--+
a |..|..|..|..|..|..|..|..|..|
  +--+--+--+--+--+--+--+--+--+
b |..|..|..|..|..|..|..|..|..|
  +--+--+--+--+--+--+--+--+--+
c |..|..|..|..|..|..|..|..|..|
  +--+--+--+--+--+--+--+--+--+
    1  2  3  4  5  6  7  8  9 \
'''


class Master:
    def __init__(self):
        self.valid_numbers = list(range(1, 90))
        self.curr_number = None

    def is_honest(self, number):
        if number == self.curr_number:
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
    def get_tickets():
        tickets = []
        ticket1 = Ticket()
        tickets.append(ticket1)
        while True:
            ticket2 = Ticket()
            if ticket1.numbers != ticket2.numbers:
                tickets.append(ticket2)
                break
        return tickets


class Player:
    def __init__(self, ticket):
        self.ticket = ticket

    def move(self, coords, master):
        number = self.ticket.cross_out(coords)
        if number:
            return master.is_honest(number)
        else:
            return True
#
#
# class HumanPlayer(Player):
#     def move(self, curr_number):
#         pass
#
#
# class ComputerPlayer(Player):
#     def move(self, curr_number):
#         pass


class Ticket:
    row_labels = ['a', 'b', 'c']
    column_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        valid_numbers = list(range(1, 90))
        self.numbers = [[None] * 9 for _ in range(3)]
        for i in range(len(self.numbers)):
            count = 0
            while count < 5:
                j = random.randint(0, 8)
                while not self.numbers[i][j]:
                    number = random.randint(j * 10 + 1, j * 10 + 10)
                    if number in valid_numbers:
                        self.numbers[i][j] = number
                        count += 1
                        valid_numbers.remove(number)

    def __str__(self):
        grid = grid_pattern
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if not self.numbers[i][j]:
                    continue
                index = 31 * ((i + 1) * 2 - 1) + (j + 1) * 3
                if type(self.numbers[i][j]) == int and self.numbers[i][j] < 10:
                    numb = '0' + str(self.numbers[i][j])
                else:
                    numb = str(self.numbers[i][j])
                grid = grid[:index] + numb + grid[index + 2:]
        return grid

    def cross_out(self, coords):
        if coords[0] not in self.row_labels or coords[1] not in self.column_labels:
            print('Вы ввели неверные координаты')
            return
        i = self.row_labels.index(coords[0])
        j = self.column_labels.index(coords[1])
        number = self.numbers[i][j]
        if type(number) != int:
            print('Вы ввели неверные координаты')
            return
        self.numbers[i][j] = 'XX'
        return number


class Game:
    def __init__(self):
        self.master = Master()
        tickets = Master.get_tickets()
        self.ticket = tickets[0]
        self.player = Player(tickets[1])
        self.win_state = WinState.NA

    def __str__(self):
        return 'Билет противника:' + '\n' + str(self.ticket) + '\n' + 'Ваш билет:' + '\n' + str(self.player.ticket)

    def move(self, coords):
        if coords != 0:
            if not self.player.move(coords, self.master):
                self.win_state = WinState.DISQUALIFIED

        for i in range(len(self.ticket.numbers)):
            for j in range(len(self.ticket.numbers[i])):
                if self.master.curr_number == self.ticket.numbers[i][j]:
                    self.ticket.numbers[i][j] = 'XX'
                    break
        if len(self.ticket.numbers) == 0:
            self.win_state = WinState.LOSE
        if len(self.player.ticket.numbers) == 0:
            self.win_state = WinState.WIN

    def run(self):
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
            if self.master.get_count_valid_numbers == 0:
                print('Числа в барабане кончились, ничья!')
                break
            if self.win_state == WinState.WIN:
                print('YOU WIN')
                break
            if self.win_state == WinState.LOSE:
                print('YOU LOSE')
                break
            if self.win_state == WinState.DISQUALIFIED:
                print('DISQUALIFIED')
                print('Вас впоймали на жульничестве')
                break
            print(self)
            print(f'Следующее число: {self.master.next_number()}')
            coords = input('Введите координаты для зачеркивания: ')
            self.move(coords)


if __name__ == '__main__':
    Game().run()
