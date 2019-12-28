from enum import Enum
from master import *
from player import *


class WinState(Enum):
    NA = 0
    WIN = 1
    LOSE = 2
    DISQUALIFIED = 3


class Game:
    def __init__(self):
        self.master = Master()
        tickets = Master.get_tickets()
        self.human_player = HumanPlayer(tickets[0])
        self.computer_player = ComputerPlayer(tickets[1])
        self.win_state = WinState.NA

    def __str__(self):
        return 'Билет противника:' + '\n' + str(self.computer_player.ticket) + '\n' + 'Ваш билет:' + '\n' + str(self.human_player.ticket)

    def player_move(self, player, number):
        player.move(number)
        return self.master.is_honest(number)

    def move(self, coords):
        if coords[0] not in self.human_player.ticket.row_labels or coords[1] not in self.human_player.ticket.column_labels:
            print('Вы ввели неверные координаты')
            return
        if coords != 0:
            i = self.human_player.ticket.row_labels.index(coords[0])
            j = self.human_player.ticket.column_labels.index(coords[1])
            number = self.human_player.ticket.numbers[i][j]
            if type(number) != int:
                print('Вы ввели неверные координаты')
                return
            if not self.player_move(self.human_player, number):
                self.win_state = WinState.DISQUALIFIED
        self.player_move(self.computer_player, self.master.curr_number)
        if len(self.computer_player.ticket.numbers) == 0:
            self.win_state = WinState.LOSE
        if len(self.human_player.ticket.numbers) == 0:
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
            print()
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
