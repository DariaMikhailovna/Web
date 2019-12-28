class Player:
    def __init__(self, ticket):
        self.ticket = ticket

    def __str__(self):
        return self.title + '\n' + str(self.ticket)

    def move(self, curr_number):
        raise NotImplementedError()


class HumanPlayer(Player):
    title = 'Ваш билет:'

    def move(self, curr_number):
        coords = input('Введите координаты для зачеркивания: ')
        if coords == '0':
            return None
        if coords[0] not in self.ticket.row_labels or coords[1] not in self.ticket.column_labels:
            print('Вы ввели неверные координаты')
            return None
        i = self.ticket.row_labels.index(coords[0])
        j = self.ticket.column_labels.index(coords[1])
        number = self.ticket.numbers[i][j]
        if type(number) != int:
            print('Вы ввели неверные координаты')
            return None
        self.ticket.numbers[i][j] = 'XX'
        return number


class ComputerPlayer(Player):
    title = 'Билет противника:'

    def move(self, curr_number):
        for i in range(len(self.ticket.numbers)):
            for j in range(len(self.ticket.numbers[i])):
                if curr_number == self.ticket.numbers[i][j]:
                    self.ticket.numbers[i][j] = 'XX'
                    break
