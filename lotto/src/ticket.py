import random

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
