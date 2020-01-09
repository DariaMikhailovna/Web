from ticket import *


class Master:
    def __init__(self):
        self.valid_numbers = list(range(1, 90))
        self.curr_number = None

    def is_honest(self, number):
        return number == self.curr_number

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
