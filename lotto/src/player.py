class Player:
    def __init__(self, ticket):
        self.ticket = ticket

    def move(self, curr_number):
        raise NotImplementedError()


class HumanPlayer(Player):
    def move(self, number):
        for i in range(len(self.ticket.numbers)):
            for j in range(len(self.ticket.numbers[i])):
                if number == self.ticket.numbers[i][j]:
                    self.ticket.numbers[i][j] = 'XX'
                    break


class ComputerPlayer(Player):
    def move(self, curr_number):
        for i in range(len(self.ticket.numbers)):
            for j in range(len(self.ticket.numbers[i])):
                if curr_number == self.ticket.numbers[i][j]:
                    self.ticket.numbers[i][j] = 'XX'
                    break
