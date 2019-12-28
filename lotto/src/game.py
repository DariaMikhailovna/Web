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
        self.players = []
        self.players.append(HumanPlayer(tickets[0]))
        self.players.append(ComputerPlayer(tickets[1]))
        self.win_state = WinState.NA

    def __str__(self):
        return '\n'.join(map(str, self.players))

    def player_move(self, player, curr_number):
        number = player.move(curr_number)
        if number:
            return self.master.is_honest(number)
        return True

    def move(self):
        for player in self.players:
            if not self.player_move(player, self.master.curr_number):
                self.win_state = WinState.DISQUALIFIED
            if len(player.ticket.numbers) == 0:
                if type(player) is HumanPlayer:
                    self.win_state = WinState.WIN
                else:
                    self.win_state = WinState.LOSE

    def run(self):
        print('Добро пожаловать в игру ЛОТО!')
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
            self.move()


if __name__ == '__main__':
    Game().run()
