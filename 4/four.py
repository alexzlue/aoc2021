class Bingo():

    def __init__(self, rows):
        self.board = rows
        self.n = len(rows)
        self.called = [[False for _ in r] for r in rows]
        self.v_to_coord = {}
        for i in range(self.n):
            for j in range(self.n):
                self.v_to_coord[rows[i][j]] = (i, j)

    def add_called(self, v):
        if v not in self.v_to_coord:
            return False

        i, j = self.v_to_coord[v]
        self.called[i][j] = True
        return True
    
    def get_unmarked(self):
        return [self.board[i][j] for i in range(self.n) for j in range(self.n) if not self.called[i][j]]

    def is_bingo(self):
        for i in range(self.n):
            if all(self.called[i]):
                return True
        for j in range(self.n):
            column = [self.called[i][j] for i in range(self.n)]
            if all(column):
                return True
        return False

with open('4/input.txt') as f:
    numbers = f.readline().split(',')
    numbers = [int(n) for n in numbers]
    f.readline()
    board_vals = []
    for vals in f.read().split('\n\n'):
        board = []
        for row in vals.split('\n'):
            int_row = [int(r) for r in row.split()]
            board.append(int_row)
        board_vals.append(board)


def part_1():
    boards = [Bingo(board) for board in board_vals]
    first_bingo = None
    for num in numbers:
        if first_bingo is not None:
            break
        for board in boards:
            if board.add_called(num) and board.is_bingo():
                first_bingo = (num, board.get_unmarked())
                break
    return first_bingo[0] * sum(first_bingo[1])

def part_2():
    boards = [Bingo(board) for board in board_vals]
    board_nums = [i for i in range(len(boards))]
    last_bingo = None
    last = -1
    for board in boards:
        for i in range(len(numbers)):
            num = numbers[i]
            if board.add_called(num) and board.is_bingo():
                if i > last:
                    last = i
                    last_bingo = (num, board.get_unmarked())
                break
    return last_bingo[0] * sum(last_bingo[1])

print(part_1())
print(part_2())
